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

def load_Katakana(file_path):
    Katakana_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            latin, Katakana = line.strip().split()
            Katakana_dict[latin] = Katakana
    return Katakana_dict

def generate_random_sequence(Katakana_dict, length):
    latin_sequence = random.sample(list(Katakana_dict.keys()), length)
    Katakana_sequence = [Katakana_dict[latin] for latin in latin_sequence]
    return latin_sequence, Katakana_sequence

def main():
    script_dir = get_script_directory()
    Katakana_file = os.path.join(script_dir, "katakana_current_learning.txt")
    Katakana_dict = load_Katakana(Katakana_file)
    print("\n--- Katakana Learning ---")

    size = 10
    time_list = []

    while True:
        latin_sequence, Katakana_sequence = generate_random_sequence(Katakana_dict, size)
        start_time = time.time()

        user_input = input(f"Latin for {' '.join(Katakana_sequence)}\n       -> ")
        user_input_list = user_input.split()  # Split the input into a list of Latin characters
        correct = 0
        for i, latin in enumerate(latin_sequence):
            if len(user_input_list)<=i:
                break
            if user_input_list[i].lower() == latin.lower():
                correct += 1

        if correct == size:
            print(f"{GREEN}Correct!{RESET}\n")
        else:
            print(f"{RED}Incorrect. The correct sequence is '{' '.join(latin_sequence)}'.{RESET}\n")
            print(f"Correct word: {correct} / {size}")

        end_time = time.time()
        time_list.append(end_time - start_time)
        if len(time_list)>=size:
            time_list.pop(0)
        print("Average speed: {:.2f} character/s".format(len(time_list)*size / np.sum(time_list)))

if __name__ == "__main__":
    main()
