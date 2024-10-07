from typing import List, Optional
from urllib import response
import requests
from configuration.config import (
    headers, 
    BASE_URL, 
    HASH_URL_ENCODE
    )

CLAN_TAG: str = "#RY2JV0JC"

def get_clan_members() -> Optional[List]:
    # Get clan members json response
    url: str = f'{BASE_URL}/clans/{HASH_URL_ENCODE}{CLAN_TAG[1:]}/members'
    res: response = requests.get(url, headers=headers)
    
    # Check error
    if res.status_code != 200:
        print(f'Failed to get clan members response info: {res.status_code}')
        print(f'{res.reason}')
        return None
    
    # Return list of players
    return list(res.json()['items'])