import random
from colorama import init, Fore, Style

init(autoreset=True)

choices = ["Rock", "Paper", "Scissor"]

win_conditions = {
    "Rock": "Scissor",
    "Paper": "Rock",
    "Scissor": "Paper"
}


def exit_game(player_name, user_score, ai_score):

    print(Fore.YELLOW + "\nFinal Result:" + Style.RESET_ALL)

    print(Fore.GREEN + f"{player_name}: {user_score}" + Style.RESET_ALL)
    print(Fore.RED + f"Computer: {ai_score}" + Style.RESET_ALL)

    if user_score > ai_score:
        print(Fore.GREEN + "You won the challenge!" + Style.RESET_ALL)
    elif ai_score > user_score:
        print(Fore.RED + "Computer won challenge!" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "The Game ended in a tie!" + Style.RESET_ALL)

    print(Fore.MAGENTA + "Thank you for playing!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)

    exit()


def user_choice(player_name, user_score, ai_score):
    while True:
        choice = input(
            Fore.CYAN +
            "Choose Rock, Paper, or Scissor: " + Style.RESET_ALL).capitalize()

        if choice.lower() == "exit":
            exit_game(player_name, user_score, ai_score)

        if choice in choices:
            return choice

        print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)


def AI_choice():
    return random.choice(choices)


def play(player_name, user_score, ai_score):

    user = user_choice(player_name, user_score, ai_score)
    ai = AI_choice()

    print(Fore.MAGENTA + f"You chose: {user}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Computer chose: {ai}" + Style.RESET_ALL)

    if user == ai:
        print(Fore.BLUE + "It's a tie!" + Style.RESET_ALL)
        return "tie"

    elif win_conditions[user] == ai:
        print(Fore.GREEN + "You Win!" + Style.RESET_ALL)
        return "user"

    else:
        print(Fore.RED + "Computer Wins!" + Style.RESET_ALL)
        return "ai"


def ten_rounds(player_name):

    user_score = 0
    ai_score = 0

    for i in range(10):

        result = play(player_name, user_score, ai_score)

        if result == "user":
            user_score += 1

        elif result == "ai":
            ai_score += 1


    print(Fore.YELLOW + "\nFinal Result:" + Style.RESET_ALL)

    print(Fore.GREEN + f"{player_name}: {user_score}" + Style.RESET_ALL)
    print(Fore.RED + f"Computer: {ai_score}" + Style.RESET_ALL)


def Rock_Paper_Scissor():

    print(Fore.MAGENTA + "Welcome to Rock, Paper, Scissor!" + Style.RESET_ALL)

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    user_score = 0
    ai_score = 0

    while True:

        ten_rounds(player_name)

        result = play(player_name, user_score, ai_score)

        if result == "user":
            user_score += 1

        elif result == "ai":
            ai_score += 1

        print(Fore.GREEN + f"\n{player_name}: {user_score}" + Style.RESET_ALL)
        print(Fore.RED + f"Computer: {ai_score}\n" + Style.RESET_ALL)


        if user_score > ai_score:
            print(Fore.GREEN + "You won challenge!" + Style.RESET_ALL)

        elif ai_score > user_score:
            print(Fore.RED + "Computer won the challenge!" + Style.RESET_ALL)

        else:
            print(Fore.BLUE + "Game in a tie!" + Style.RESET_ALL)


        play_again = input(
            Fore.YELLOW + "Play again? (yes/no): " + Style.RESET_ALL
        ).lower()


        if play_again != "yes":
            print(Fore.MAGENTA + "Thank you for playing!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    Rock_Paper_Scissor()