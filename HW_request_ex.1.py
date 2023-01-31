import requests


def smart_hero(heroes_names):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    request = requests.get(url=url)
    all_data = request.json()

    heroes_dict = {}
    for superhero in all_data:
        if superhero['name'] in heroes_names:
            # chars_name = superhero.get('name')
            chars_powerstats = superhero.get('powerstats')
            chars_intelligence = chars_powerstats.get('intelligence')
            heroes_dict.setdefault(superhero['name'], chars_intelligence)

    heroes_dict_max_v = max(heroes_dict.values())
    heroes_dict_max_k = max(heroes_dict.keys())

    print(f'Самый умный супергерой - {heroes_dict_max_k}. Его интеллект равен {heroes_dict_max_v} pts.')
    # print(heroes_dict)


if __name__ == '__main__':
    smart_hero('Thanos, Captain America, Hulk')


# Второй вариант решения, более длинный


def smart_hero():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    request = requests.get(url=url)
    all_data = request.json()

    heroes_dict = {}
    for superhero in all_data:
        if superhero['name'] == 'Hulk':
            chars_powerstats = superhero.get('powerstats')
            chars_intelligence = chars_powerstats.get('intelligence')
            heroes_dict.setdefault(superhero['name'], chars_intelligence)

    for superhero in all_data:
        if superhero['name'] == 'Thanos':
            chars_powerstats = superhero.get('powerstats')
            chars_intelligence = chars_powerstats.get('intelligence')
            heroes_dict.setdefault(superhero['name'], chars_intelligence)

    for superhero in all_data:
        if superhero['name'] == 'Captain America':
            chars_powerstats = superhero.get('powerstats')
            chars_intelligence = chars_powerstats.get('intelligence')
            heroes_dict.setdefault(superhero['name'], chars_intelligence)

    heroes_dict_max_v = max(heroes_dict.values())
    heroes_dict_max_k = max(heroes_dict.keys())

    print(f'Самый умный супергерой - {heroes_dict_max_k}. Его интеллект равен {heroes_dict_max_v} pts.')


if __name__ == '__main__':
    smart_hero()
