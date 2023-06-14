import requests


def get_game_information():
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f"https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=es-ES&country=EC&allowCountries=EC"
    r = requests.get(url, headers=user_agent)

    print(r.json())


get_game_information()





