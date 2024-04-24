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

# Read input from a file and return a list of tuples containing shape and outcome
def read_input(input_file):
    game_round = []
    with open(input_file, 'r') as file:
        for line in file:
            shape, outcome = line.strip().split()
            game_round.append((shape, outcome))
    return game_round

# Calculate the total score of the game based on the provided rules
def calculate_score(game_round):
    scores = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    total_score = sum(scores.get(shape + outcome, 0) for shape, outcome in game_round)
    return total_score

# Main function to run the program
def main():
    input_file = "CSF101-CAP/input_5_cap1.txt"
    game_round = read_input(input_file)
    total_round_score = calculate_score(game_round)
    print("Total Score:", total_round_score)

