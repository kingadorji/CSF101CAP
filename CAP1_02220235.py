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

def read_input(input_file):
    game_round = []
    try:
        with open(input_file, 'r') as file:
          for line in file:
                shape, outcome = line.strip().split()
                game_round.append((shape, outcome))
    except FileNotFoundError:
        print("Error: Input file not found.")
        return None
    except ValueError:
        print("Error: Input file is not formatted correctly.")
        return None
    return game_round

def calculate_score(game_round):
    if game_round is None:
        return 0
    scores = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    total_score = sum(scores.get(shape + outcome, 0) for shape, outcome in game_round)
    return total_score

def main():
    input_file = "CSF101-CAP/input_5_cap1.txt"
    game_round = read_input(input_file)
    if game_round is not None:
        total_round_score = calculate_score(game_round)
        print("Total Score:", total_round_score)
if __name__ == "__main__":
    main()
