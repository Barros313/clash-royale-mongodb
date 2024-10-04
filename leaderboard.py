from urllib import response
import requests
from player import CLASH_ROYALE_API_KEY
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
CLASH_ROYALE_API_KEY = os.getenv("CLASH_ROYALE_API")
MONGO_URI = os.getenv("MONGO_URI")

API_KEY = f'{CLASH_ROYALE_API_KEY}'
BASE_URL = 'https://api.clashroyale.com/v1'

client = MongoClient(f'{MONGO_URI}')
db = client['clash_royale']
collection = db['leaderboards']

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

def main():

    print(fetch_leaderboard())

    return None


def fetch_leaderboard():
    url = f'{BASE_URL}/leaderboards'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return get_leaderboard_id(res.json())

    print(f'Failed to get leaderboard response info: {res.status_code}')
    print(f'{res.reason}')

    return None


def get_leaderboard_id(response):
    return response['items'][0]['id']


if __name__ == "__main__":
    main()