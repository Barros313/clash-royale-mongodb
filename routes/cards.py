from typing import List, Optional
from urllib import response
import requests
from configuration.config import (
    BASE_URL,
    cards_collection,
    headers
    )


def insert_cards() -> int:
    cards_list = get_cards()
    if cards_list is None:
        return


    cards_collection.insert_many(cards_list)

    return len(cards_list)


def get_cards() -> Optional[List]:
    # Get battlelog list
    url: str = f'{BASE_URL}/cards'
    res: response = requests.get(url, headers=headers)

    # Error check
    if res.status_code != 200:
        print(f'Failed to get cards: {res.status_code}')
        print(f'{res.reason}')
        return None

    # Return list
    return list(res.json()['items'])