import requests

list_hero = ['Hulk', 'Captain America', 'Thanos']

def superhero(hero_list):
    all_heroes = {}
    for name_hero in hero_list:
        date_get = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name_hero}')
        intelligence_hero = date_get.json()['results'][0]['powerstats']['intelligence']
        dict_hero = {}
        dict_hero[name_hero] = intelligence_hero
        all_heroes.update(dict_hero)
    return all_heroes

heroes = superhero(list_hero)
max_iq = 0
for name, iq in heroes.items():
    if int(iq) >= max_iq:
        max_iq = int(iq)
        max_hero = name
print(f'Самый умный супергерой {max_hero} с уровнем интеллекта = {max_iq}')
