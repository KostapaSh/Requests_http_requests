from pprint import pprint
import requests


def http_request():

    all_heros = ('Hulk', 'Captain America', 'Thanos')
    hero_intell = {}
    intelligence = 0
    smart_hero = ""

    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url = url)

    for hero in all_heros:
        for get_json in response.json():
            get_hero = get_json["name"]
            if hero == get_hero:
                hero_intell[get_hero] = get_json["powerstats"]["intelligence"]

    for key, values in hero_intell.items():
        if values > intelligence:
            smart_hero = key
            intelligence = values

    print(hero_intell)
    print(f"Самый умный герой {smart_hero}, интеллект {intelligence}")


http_request()


