import requests


hero_names = ['Hulk', 'Blade', 'Thanos', 'Spock']
stat = 'intelligence'
result = {}
for hero_name in hero_names:
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero_name}')
    heroes = response.json()['results']
    for hero in heroes:
        if hero['name'] == hero_name:
            result[hero['name']] = int(hero['powerstats'][stat])
print(result)

v = list(result.values())
k = list(result.keys())
result = k[v.index(max(v))]
print(result)
