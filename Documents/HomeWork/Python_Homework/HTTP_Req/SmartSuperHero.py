import json
import requests
from pprint import pprint

tok = {'Authorization': '2619421814940190'}
url = 'https://superheroapi.com/api/2619421814940190/search/'

Superlist = ['Hulk','Red Hulk', 'Captain America', 'Thanos','SuperMan']

hero_dict = {}


def superhero(realurl, Hero_chose, tok):
    for item in range(len(Hero_chose)):
        response = requests.get(realurl + Hero_chose[item], headers=tok)
        url_dict = response.json()
        data = url_dict["results"][0]
        for search in data.items():
            for hero in search:
                if 'intelligence' in hero:
                    hero_dict[Hero_chose[item]] = int(hero['intelligence'])
    smarter_hero = max(hero_dict, key=hero_dict.get)
    print(f'Самый умный герой из {Hero_chose} это {smarter_hero}')


if __name__ == "__main__":
    superhero(url, Superlist, tok)
