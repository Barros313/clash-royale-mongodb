import requests
import pymongo
from config import BASE_URL, HASH_URL_ENCODE, db, headers


collection = db['teste']

def main():
    url = f'{BASE_URL}/players/{HASH_URL_ENCODE}RJLU02Y/battlelog'
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f'Failed to get player battlelog: {res.status_code}')
        print(f'{res.reason}')
        return None

    battlelog = res.json()

    collection['battlelog'].insert_many(battlelog)


if __name__ == "__main__":
    main()