from scripts.battlelog import insert_players_battlelog
from scripts.clan_members import get_clan_members
from scripts.player import insert_player_into_db


def main():
    # Getting clan members
    clan_members = get_clan_members()
    # Exit if error
    if clan_members is None:
        return

    # Fetch each member information and battlelog than save into database
    for member in clan_members:
        insert_player_into_db(member)
        insert_players_battlelog(member['tag'])

    # Print success player insertion message
    print(f"Top {len(clan_members)} players inserted.")

    # Exit
    return None


# Call main function
if __name__ == "__main__":
    main()