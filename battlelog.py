from typing import List
import requests
import pymongo
from config import (
    BASE_URL, 
    HASH_URL_ENCODE,
    db, 
    player_collection, 
    players_battlelog_collection,
    headers
    )


def insert_players_battlelog(tag):
    battlelog = get_battlelog(tag[1:])

    players_battlelog_collection.insert_many(battlelog)

    return None


def get_battlelog(tag: str) -> List:
    # Get battlelog list
    url = f'{BASE_URL}/players/{HASH_URL_ENCODE}{tag}/battlelog'
    res = requests.get(url, headers=headers)

    # Error check
    if res.status_code != 200:
        print(f'Failed to get player battlelog: {res.status_code}')
        print(f'{res.reason}')
        return None

    # Return list
    return list(res.json())