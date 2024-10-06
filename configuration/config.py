import os
from typing import override
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get Clash Royale API Key
CR_API_KEY: str = os.getenv("CLASH_ROYALE_API")
# Get MongoDB URI String connection
MONGO_URI: str = os.getenv("MONGO_ATLAS_URI")
# Define API Base URL
BASE_URL: str = 'https://api.clashroyale.com/v1'

# Header with API Key
headers = {
    'Authorization': f'Bearer {CR_API_KEY}'
}

# MongoClient instance
client: MongoClient = MongoClient(f'{MONGO_URI}')
# Database selection
db = client['clash_royale']

# Collections
player_collection = db['players']
players_battlelog_collection = db['players_battlelog']


# Hashtag URL encoded
HASH_URL_ENCODE: str = '%23'