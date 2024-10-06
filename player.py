import requests
import pymongo
from config import BASE_URL, HASH_URL_ENCODE, headers, db

player_collection = db['players']


def insert_player_into_db(player):
    # Removing Hash from tag string
    tag_without_hash = player['tag'][1:]

    # Fetch player info
    player_info = get_player_info(tag_without_hash)

    # Add to collection
    player_collection.insert_one(player_info)


def get_player_info(player_tag: str):
    url = f'{BASE_URL}/players/{HASH_URL_ENCODE}{player_tag}'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        print(f'Failed to fetch player info: {res.status_code}')
        print(f'{res.reason}')
        return None
