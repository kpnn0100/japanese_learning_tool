import pandas as pd
import os
import argparse
# Create a sample DataFrame
# Get the current file path
index_file = os.path.join(os.path.dirname(__file__), "index.txt")
def getShuffledKanjiDataFrame():
    current_path = os.path.abspath(__file__)

    # Get the relative path to the CSV file
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'n5_words.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Shuffle the DataFrame with a fixed seed
    shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return shuffled_df
learning_rate = 5 # Words per day

def getTodayWords():
    if not os.path.exists(index_file):
        with open(index_file, "w") as file:
            file.write("0")
            number = 0
    else:
        with open(index_file, "r") as file:
            number = int(file.read())
    if args.increment:
        number += 1
        with open(index_file, "w") as file:
            file.write(str(number))
        exit()
    df = getShuffledKanjiDataFrame()
    start = number * learning_rate
    end = start + learning_rate
    selected_words = df.iloc[start:end]
    print(selected_words)
    return selected_words

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--increment", action="store_true", help="Increment the index by 1")
args = parser.parse_args()
if not os.path.exists(index_file):
    with open(index_file, "w") as file:
        file.write("0")
        number = 0
else:
    with open(index_file, "r") as file:
        number = int(file.read())
if args.increment:
    number += 1
    with open(index_file, "w") as file:
        file.write(str(number))
