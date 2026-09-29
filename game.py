import json

GAME_FILE = "data/games.json"

def load_games():
    with open(GAME_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def get_game():
    games = load_games()

    print("\n--- GAME CONFIGURATION ---")
    print("Available games:")
    for number, name in enumerate(games, start=1):
        print(f"{number}. {name}")

    while True:
        choice = input("Choose a game number: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(games):
                break
            print("Choose a valid number.")
        except ValueError:
            print("Enter a number.")

    game_name = list(games.keys())[choice - 1]

    resolution = input("Resolution (e.g. 1920x1080): ").strip()
    graphics = input("Graphics quality (Low/Medium/High/Ultra): ").strip().title()

    if graphics not in ["Low", "Medium", "High", "Ultra"]:
        graphics = "Medium"

    return {
        "name": game_name,
        "profile": games[game_name],
        "resolution": resolution,
        "graphics": graphics
    }
