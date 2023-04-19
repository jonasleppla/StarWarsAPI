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
            height = character['height']
            characters.append({'name': name, 'height': height})
        page_num += 1
    else: #404 after page 83
        break

df = pd.DataFrame(characters)
df['height'] = df['height'].replace('unknown', '0').astype(int) # convert heights to integers
top10 = df.nlargest(10, 'height') # get the top 10 characters by height
top10 = top10.sort_values('height', ascending=False) # sort the top 10 by height in descending order
plt.bar(top10['name'], top10['height'])
plt.xticks(rotation=0)
plt.xlabel('Character')
plt.ylabel('Height')
plt.title('Top 10 Star Wars Characters by Height')
plt.show()
