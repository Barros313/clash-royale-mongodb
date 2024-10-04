from urllib import response
import requests
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

CLASH_ROYALE_API_KEY = os.getenv("CLASH_ROYALE_API")
print(CLASH_ROYALE_API_KEY)
MONGO_URI = os.getenv("MONGO_URI")

API_KEY = f'{CLASH_ROYALE_API_KEY}'
BASE_URL = 'https://api.clashroyale.com/v1'

client = MongoClient(f'{MONGO_URI}')
db = client['clash_royale']
collection = db['players']

headers = {
    'Authorization': f'Bearer {API_KEY}'
}


def main():
    player_tag = 'VRRYUQ8V0'

    player_info = get_player_info(player_tag)

    if (player_info):
        store_player_info(player_info)

    return None


def get_player_info(player_tag):
    url = f'{BASE_URL}/players/%23{player_tag}'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        print(f'Failed to fetch player info: {res.status_code}')
        print(f'{res.reason}')
        return None


def store_player_info(player_data):
    collection.insert_one(player_data)
    print('Player data inserted into MongoDB')


if __name__ == "__main__":
    main()