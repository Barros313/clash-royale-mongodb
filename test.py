from leaderboard import BASE_URL, CLASH_ROYALE_API_KEY, HASH_URL_ENCODE, MONGO_URL
import pymongo
from pymongo import MongoClient
import requests

headers = {
    'Authorization': f'Bearer {CLASH_ROYALE_API_KEY}'
}

client = MongoClient(f'{MONGO_URL}')
db = client['clash_royale']
collection = db['casa-da-agua']

def main():
    tags = list()

    tags.append("#RJLU02Y") #Vitu
    # tags.append() #Orany

    for tag in tags:
        insert_into_db(tag[1:])

    return None


def insert_into_db(tag):
    url= f'{BASE_URL}/players/{HASH_URL_ENCODE}{tag}'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        player = res.json()
        collection.insert_one(player)
        print(f"Inserted {player['name']}")


if __name__ == '__main__':
    main()