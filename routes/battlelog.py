from typing import List, Optional
from urllib import response
import requests
from configuration.config import (
    BASE_URL, 
    HASH_URL_ENCODE,
    players_battlelog_collection,
    headers
    )


def insert_players_battlelog(tag) -> None:
    battlelog = get_battlelog(tag[1:])

    players_battlelog_collection.insert_many(battlelog)

    return None


def get_battlelog(tag: str) -> Optional[List]:
    # Get battlelog list
    url: str = f'{BASE_URL}/players/{HASH_URL_ENCODE}{tag}/battlelog'
    res: response = requests.get(url, headers=headers)

    # Error check
    if res.status_code != 200:
        print(f'Failed to get player battlelog: {res.status_code}')
        print(f'{res.reason}')
        return None

    # Return list
    return list(res.json())