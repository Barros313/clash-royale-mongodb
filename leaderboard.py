from typing import Any, Optional, Dict, List
from urllib import request, response
import requests
import pymongo
from config import headers, db, BASE_URL, HASH_URL_ENCODE

collection = db['players']

def main() -> None:
    leaderboard_id : Optional[int] = fetch_leaderboard()

    if leaderboard_id is None:
        return

    ranking: Optional[List[Dict[str, Any]]] = get_ranking(leaderboard_id)

    if ranking:
        top_players = filter_top_players(ranking['items'], limit=40)

        insert_players(top_players)

        print(f"Top {len(top_players)} players inserted.")

        # Store in MongoDB

    return None


def insert_players(top_players):
    for player in top_players:
        # Removing Hash from tag string
        tag_without_hash = player['tag'][1:]
        
        # Fetch player info
        player_info = get_player_info(tag_without_hash)
        # Add to collection
        collection.insert_one(player_info)


def get_player_info(player_tag: str):
    url = f'{BASE_URL}/players/{HASH_URL_ENCODE}{player_tag}'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        print(f'Failed to fetch player info: {res.status_code}')
        print(f'{res.reason}')
        return None


def filter_top_players(players, limit: int = 40):
    return players[:min(len(players), limit)]


def get_ranking(leaderboard_id: int) -> str | None:
    url : str = f'{BASE_URL}/leaderboard/{leaderboard_id}'
    res : response = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f'Failed to get leaderboard response info: {res.status_code}')
        print(f'{res.reason}')
        return None
    
    return res.json()


def fetch_leaderboard() -> Optional[int]:
    url : str = f'{BASE_URL}/leaderboards'

    try:
        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as exp:
        print(f'Failed to get leaderboard response info: {exp}')
        return None

    return get_leaderboard_id(response.json())



def get_leaderboard_id(res: Dict[str, Any]) -> Optional[int]:
    try:
        return int(res['items'][0]['id'])
    except (KeyError, ValueError, TypeError) as exp:
        print(f"Error converting id: {exp}")
        return None


if __name__ == "__main__":
    main()