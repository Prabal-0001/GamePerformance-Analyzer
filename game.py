from database import GAMES


# Ask the user which game and display settings are being tested.
def get_game():
    games = GAMES

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

    # Convert the selected menu number into the corresponding game name.
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
