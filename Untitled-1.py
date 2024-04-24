################################
# Your Name: kinga Dorji
# Your Section :ICE 
# Your Student ID Number:02220235
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################

# Import numpy library
import numpy as np

# Define game constants
LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

# Read the input.txt file
def read_input(file_path):
# code here to read your input file
    with open("input_5_cap1.txt", "r") as file:
        # Read the file line by line
        lines = file.readlines()
        return lines
        
# solution
def calculate_score(round_score_list):
    # Calculate the total score
    total_score = np.sum(round_score_list)
    print("the total score is: ", total_score)
# implement your solution here.
# print your solution to output as: "the total score is: <score>"
# Other parts of code here to run your functions and printing of the input.
# Note: You may add parameters/arguments, return values to the functions above.

# Main logic of the game
def main_game():
    # Initialized the input file path
    file_path = "Users\MY-PC\Desktop\CSF101CAP-1\input_5_cap1.txt"
    # Initialized the game variable
    Rock = {"score": 1, "symbol": "A", "beat": "C" }
    Paper = {"score":2, "symbol": "B", "beat": "A"}
    Scissor = {"score": 3, "symbol": "C", "beat": "B"}
    round_score = 0
    round_score_list = []

    # Read the input file
    input_file= read_input(file_path)

    # Iterate thjrough the input file
    for line in input_file:
        print(line)
        opponent_input, condition = line.strip().split()
        # Get the player input 
        player_input = input("Enter your input: ")

        # Draw condition
        if condition == 'Y':
            # Check for draw condition
            if(player_input == opponent_input):
                # Calculate the score
                if player_input == Rock['symbol']:
                    round_score = Rock['score'] + DRAW_SCORE
                elif player_input == Paper['symbol']:
                    round_score = Paper['score'] + DRAW_SCORE
                elif player_input == Scissor['symbol']:
                    round_score = Scissor['score'] + DRAW_SCORE
            # Append the round score to the list
            round_score_list.append(round_score)

        # Lose Condition
        elif condition == 'X':
            # check for lost condition
            if opponent_input == Rock['symbol'] and player_input == Rock['beat']:
                round_score = Rock['score'] + LOSE_SCORE
            elif opponent_input == Paper['symbol'] and player_input == Paper['beat']:
                round_score = Paper['score'] + LOSE_SCORE
            elif opponent_input == Scissor['symbol'] and  player_input == Scissor['beat']:
                round_score = Scissor['score'] + LOSE_SCORE
            # Append the round score to the list
            round_score_list.append(round_score)
        
        # Win condition
        elif condition == 'Z':
            # Check for win condition
            if player_input == Rock['symbol']  and Rock['beat'] == opponent_input:
                round_score = Rock['score'] + WIN_SCORE
            if player_input == Paper['symbol']  and Paper['beat'] == opponent_input:
                round_score = Paper['score'] + WIN_SCORE
            if player_input == Scissor['symbol']  and Scissor['beat'] == opponent_input:
                round_score = Scissor['score'] + WIN_SCORE
            
            # Append the win round score to the list
            round_score_list.append(round_score)

    # Calculate the total score
    calculate_score(round_score_list)
        
# Run the main game
main_game()