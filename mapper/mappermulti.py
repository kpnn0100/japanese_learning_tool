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

def generate_random_sequence(hiragana_dict, length):
    latin_sequence = random.sample(list(hiragana_dict.keys()), length)
    hiragana_sequence = [hiragana_dict[latin] for latin in latin_sequence]
    return latin_sequence, hiragana_sequence

def main():
    script_dir = get_script_directory()
    hiragana_file = os.path.join(script_dir, "map.txt")
    hiragana_dict = load_hiragana(hiragana_file)
    print("\n--- Hiragana Learning ---")

    size = 10
    time_list = []

    while True:
        latin_sequence, hiragana_sequence = generate_random_sequence(hiragana_dict, size)
        start_time = time.time()

        user_input = input(f"Latin for {' '.join(hiragana_sequence)}\n       -> ")
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
        print("Average speed: {:.2f} character/s".format(np.sum(time_list)/len(time_list)/size))

if __name__ == "__main__":
    main()
