from typing import Any, Optional, Dict, List
from urllib import request, response
import requests
from player import CLASH_ROYALE_API_KEY
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

CLASH_ROYALE_API_KEY: str = os.getenv("CLASH_ROYALE_API")
MONGO_URL: str = os.getenv("MONGO_URL")

API_KEY: str = f'{CLASH_ROYALE_API_KEY}'
BASE_URL: str = 'https://api.clashroyale.com/v1'

client: MongoClient = MongoClient(f'{MONGO_URL}')
db = client['clash_royale']
collection = db['leaderboards']

headers: Dict[str, str] = {
    'Authorization': f'Bearer {API_KEY}'
}

def main() -> None:
    leaderboard_id : Optional[int] = fetch_leaderboard()

    if leaderboard_id is None:
        return

    ranking: Optional[List[Dict[str, Any]]] = get_ranking(leaderboard_id)

    if ranking:
        top_players = filter_top_players(ranking['items'], limit=40)

        collection.insert_many(top_players)

        print(f"Top {len(top_players)} players inserted.")

        # Store in MongoDB

    return None


def filter_top_players(players: List[Dict[str, Any]], limit: int = 40) -> List[Dict[str, Any]]:
    return players[:min(len(players), limit)]


def get_ranking(leaderboard_id : int) -> str | None:
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



def get_leaderboard_id(res : Dict[str, Any]) -> Optional[int]:
    try:
        return int(res['items'][0]['id'])
    except (KeyError, ValueError, TypeError) as exp:
        print(f"Error converting id: {exp}")
        return None


if __name__ == "__main__":
    main()