from leaderboard import filter_top_players, get_ranking
from player import insert_player_into_db


def main():
    # Getting top 40 players
    ranking = get_ranking()
    if ranking is None:
        return

    top_players = filter_top_players(ranking['items'], limit=40)
    for player in top_players:
        insert_player_into_db(player)

    print(f"Top {len(top_players)} players inserted.")

    return None



if __name__ == "__main__":
    main()