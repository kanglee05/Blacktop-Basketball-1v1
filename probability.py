
# Function to calculate the chance of making a shot based on the user's level
def shot_success_chance(level):
    if level == "3-point line":
        return 0.25
    elif level == "mid-range":
        return 0.45
    elif level == "floater":
        return 0.70
    elif level == "layup/dunk":
        return 0.90


# Function to calculate the chance of computer scoring based on difficulty
def computer_shot_success_chance(difficulty):
    if difficulty == "easy":
        return 0.25
    elif difficulty == "medium":
        return 0.50
    elif difficulty == "hard":
        return 0.75


# Function to calculate the chance of the computer stealing the ball
def steal_chance(difficulty, action):
    if difficulty == "easy":
        return 0.1 if action == "dribble" else 0.2
    elif difficulty == "medium":
        return 0.2 if action == "dribble" else 0.4
    elif difficulty == "hard":
        return 0.3 if action == "dribble" else 0.6

