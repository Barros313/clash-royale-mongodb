from ast import Dict
from typing import Optional
import requests
from configuration.config import (
    BASE_URL, 
    HASH_URL_ENCODE, 
    headers, 
    player_collection
    )


def insert_player_into_db(player) -> None:
    # Get player tag
    tag_without_hash = player['tag'][1:]

    # Fetch player info
    player_info = get_player_info(tag_without_hash)

    # Add to collection
    player_collection.insert_one(player_info)

    return None


def get_player_info(player_tag: str) -> Optional[Dict]:
    url = f'{BASE_URL}/players/{HASH_URL_ENCODE}{player_tag}'
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f'Failed to fetch player info: {res.status_code}')
        print(f'{res.reason}')
        return None
    
    return res.json()
