import random


def is_valid_input(input_value, allowed_values=None):
    """ Validates input to be a positive integer and optionally checks if it's within allowed values. """
    try:
        value = int(input_value)
        if value <= 0:
            return False
        if allowed_values and value not in allowed_values:
            return False
        return True
    except ValueError:
        return False


def get_valid_input(prompt, error_message, allowed_values=None):
    """ Repeatedly prompts for input until valid based on criteria. """
    while True:
        response = input(prompt)
        if is_valid_input(response, allowed_values):
            return int(response)
        print(error_message)


def play_turn(player, pencils):
    """ Plays one turn of the game. """
    print("|" * pencils + f"\n{player}'s turn:")
    if player == "Jack":  # Assuming Jack is the AI player
        # AI strategy for making a move
        return min(pencils, (pencils - 1) % 4 or 1)
    else:
        return get_valid_input("Number of pencils to remove (1-3): ",
                               "Possible values: '1', '2' or '3'", [1, 2, 3])


def game(player_1, player_2):
    pencils = get_valid_input("How many pencils would you like to use:\n",
                              "The number of pencils should be numeric and positive")
    starter = input("Who will be the first (John, Jack):\n")
    while starter not in [player_1, player_2]:
        starter = input(f"Choose between '{player_1}' and '{player_2}':\n")

    current_player = starter
    while pencils > 0:
        remove = play_turn(current_player, pencils)
        pencils -= remove
        if pencils == 0:
            print(f"{current_player} wins!")
            return
        current_player = player_1 if current_player == player_2 else player_2


if __name__ == "__main__":
    game("John", "Jack")