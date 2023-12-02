import random
import sys
import os
import time
import numpy as np
# ANSI escape codes for colored output
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
def get_script_directory():
    script_path = os.path.dirname(__file__)
    return script_path
def load_hiragana(file_path):
    hiragana_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            latin, hiragana = line.strip().split()
            hiragana_dict[latin] = hiragana
    return hiragana_dict

def main():
    script_dir = get_script_directory()
    hiragana_file = os.path.join(script_dir, "map.txt")
    hiragana_dict = load_hiragana(hiragana_file)
    print("\n--- Hiragana Learning ---")
    latin_list = list(hiragana_dict.keys())
    size = 10
    ma = 0
    time_list = [0] *size
    while True:
        random.shuffle(latin_list)
        hiragana = random.choice(list(hiragana_dict.values()))
        correct_latin = [k for k, v in hiragana_dict.items() if v == hiragana][0]
        start_time = time.time()
        user_input = input(f"Latin for '{hiragana}': ")
        correct = 0
        if user_input.lower() == correct_latin.lower():
            print(f"{GREEN}Correct!{RESET}\n")
        else:
            print(f"{RED}Incorrect. The correct answer is '{correct_latin}'.{RESET}\n")
        end_time = time.time()
        time_list.append(end_time-start_time)
        time_list.pop(0)
        print("average speed " + str(size/np.sum(time_list)) + " character/s")



if __name__ == "__main__":
    main()
