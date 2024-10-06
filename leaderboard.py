from typing import Any, Optional, Dict, List
from urllib import request, response
import requests
from player import insert_player_into_db
import pymongo
from config import headers, db, BASE_URL, HASH_URL_ENCODE


def get_ranking():
    leaderboard_id = get_leaderboard_id()

    if leaderboard_id is None:
        return

    url : str = f'{BASE_URL}/leaderboard/{leaderboard_id}'
    res : response = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f'Failed to get leaderboard response info: {res.status_code}')
        print(f'{res.reason}')
        return None
    
    return res.json()


def filter_top_players(players, limit: int = 40):
    return players[:min(len(players), limit)]


def get_leaderboard_id() -> Optional[int]:
    url : str = f'{BASE_URL}/leaderboards'

    try:
        res: requests.Response = requests.get(url, headers=headers)
        res.raise_for_status()
    except requests.RequestException as exp:
        print(f'Failed to get leaderboard response info: {exp}')
        return None

    try:
        leaderboards = res.json()
        return int(leaderboards['items'][0]['id'])
    except (KeyError, ValueError, TypeError) as exp:
        print(f"Error converting id: {exp}")
        return None