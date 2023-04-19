import requests
import pandas as pd
import matplotlib.pyplot as plt

page_num = 1
characters = []

while True: 
    url = f"https://swapi.dev/api/people/?page={page_num}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for character in data['results']:
            name = character['name']
            starship_urls = character['starships']
    
            # Make API call to get starship information and extract name and max_atmosphering_speed
            starships = []
            for url in starship_urls:
                response = requests.get(url)
                starship_data = response.json()
                starship_name = starship_data['name']
                max_speed = starship_data['max_atmosphering_speed']
                characters.append({'name': name, 'starship_name': starship_name, 'max_atmosphering_speed': max_speed})

        page_num += 1
    else: #404 after page 83
        break

df = pd.DataFrame(characters, columns=['name', 'starship_name', 'max_atmosphering_speed'])

character_colors = {
    'Luke Skywalker': 'orange',
    'Darth Vader': 'black',
    'Obi-Wan Kenobi': 'blue',
    'Anakin Skywalker': 'red',
    'Boba Fett': 'purple',
    'Grievous': 'darkgreen'
}
df = df.sort_values(by='max_atmosphering_speed')
fig, ax = plt.subplots(figsize=(10, 8))
for name, group in df.groupby('name'):
    if name in character_colors:
        color = character_colors[name]
        ax.scatter(group['max_atmosphering_speed'], group['name'], color=color, label=name)

ax.set_xlabel('Max Atmosphering Speed')
ax.set_ylabel('Character Name')
ax.set_title('Star Wars Characters and their Starship Speeds')
ax.legend()

plt.show()







