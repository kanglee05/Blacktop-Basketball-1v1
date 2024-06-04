import random
import probability

user_score = 0
computer_score = 0
print("Welcome to Blacktop Basketball 1v1!")
difficulty = input("Choose difficulty level of opponent (easy, medium, hard): ").lower()
winning_score = int(input("What score do you want to play up to (max: 15)? "))
levels = ["3-point line", "mid-range", "floater", "layup/dunk"]
current_level = "3-point line"
user_possession = True

# Main game loop
while user_score < winning_score and computer_score < winning_score:
    if user_possession:
        print(f"\nYou are at the {current_level}.")
        action = input("Make your move, must shoot when at layup/dunk(shoot, dribble, crossover): ").lower()

        if action == "shoot":
            if random.random() < probability.shot_success_chance(current_level):
                points = 2 if current_level == "3-point line" else 1
                user_score += points
                print(f"You scored {points} points!")
                current_level = "3-point line"
            else:
                print("You missed the shot!")
                user_possession = False

        elif action == "dribble":
            if random.random() < probability.steal_chance(difficulty, action):
                print("The opponent stole the ball!")
                user_possession = False
            else:
                current_level = levels[levels.index(current_level) + 1]
                print(f"You moved to the {current_level}.")

        elif action == "crossover" and current_level in ["3-point line", "mid-range"]:
            if random.random() < probability.steal_chance(difficulty, action):
                print("The opponent stole the ball!")
                user_possession = False
            else:
                current_level = levels[levels.index(current_level) + 2]
                print(f"You moved to the {current_level}.")

        else:
            print("Invalid move, try again")

    else:
        if random.random() < probability.computer_shot_success_chance(difficulty):
            points = 2 if random.random() < 0.5 else 1
            computer_score += points
            print(f"The opponent scored {points} points!")
            user_possession = False
        else:
            print("The opponent missed the shot!")
            user_possession = True
        current_level = "3-point line"

    print(f"Score: You {user_score} - {computer_score} Opponent")

# Determine the winner
if user_score >= winning_score:
    print("Congratulations! You won the game!")
else:
    print("The opponent won the game, better luck next time!")
