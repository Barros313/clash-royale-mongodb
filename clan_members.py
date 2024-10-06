from typing import Any, Optional, Dict, List
from urllib import request, response
import requests
import battlelog
from player import insert_player_into_db
import pymongo
from config import headers, db, BASE_URL, HASH_URL_ENCODE

CLAN_TAG = "#RY2JV0JC"

def get_clan_members() -> List:
    # Get clan members json response
    url: str = f'{BASE_URL}/clans/{HASH_URL_ENCODE}{CLAN_TAG[1:]}/members'
    res: response = requests.get(url, headers=headers)

    # Check error
    if res.status_code != 200:
        print(f'Failed to get leaderboard response info: {res.status_code}')
        print(f'{res.reason}')
        return None
    
    # Return list of players
    return list(res.json()['items'])