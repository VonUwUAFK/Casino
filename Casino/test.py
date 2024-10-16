import random
import json
import os

LEADERBOARD_FILE = 'leaderboard.json'

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f)

def add_score(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({'name': name, 'score': score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]  # Keep top 10
    save_leaderboard(leaderboard)

def display_leaderboard():
    leaderboard = load_leaderboard()
    print("Leaderboard:")
    for entry in leaderboard:
        print(f"{entry['name']}: {entry['score']}")

def get_bet(startingcash):
    bet = int(input("How much do you want to bet? "))
    if bet > startingcash:
        print("You’re too broke, loser")
        return None
    return bet

def play_roulettes(startingcash):
    bet = get_bet(startingcash)
    if bet is None:
        return startingcash
    print("Good luck!")
    colour = input("What colour, black or red? ")
    colors = ["black", "red"]
    choice2 = random.choice(colors)
    if choice2 == colour:
        print("You won!")
        startingcash += bet
    else:
        print("You lost")
        startingcash -= bet
    return startingcash

def play_slots(startingcash):
    fruits = [random.choice(["banana", "apple", "orange", "coconut"]) for _ in range(3)]
    print(*fruits)
    if fruits[0] == fruits[1] == fruits[2]:
        print("You hit the jackpot!")
        startingcash *= 2
    elif len(set(fruits)) < 3:
        print("You got a small win!")
        startingcash += 10
    else:
        print("You lost")
        startingcash -= 10
    return startingcash

def main():
    startingcash = 100
    player_name = input("Enter your name: ")

    while True:
        print("Welcome to my casino, you have:", startingcash, "cash")
        choice = input("Do you want to play roulettes, slots, view leaderboard, or exit? ")

        if choice == "roulettes":
            startingcash = play_roulettes(startingcash)
        elif choice == "slots":
            startingcash = play_slots(startingcash)
        elif choice == "leaderboard":
            display_leaderboard()
        elif choice == "exit":
            add_score(player_name, startingcash)
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

main()
