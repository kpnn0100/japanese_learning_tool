import random

# ANSI escape codes for colored output
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def load_hiragana(file_path):
    hiragana_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            latin, hiragana = line.strip().split()
            hiragana_dict[latin] = hiragana
    return hiragana_dict

def main():
    hiragana_file = "source.txt"
    hiragana_dict = load_hiragana(hiragana_file)
    print("\n--- Hiragana Learning ---")
    latin_list = list(hiragana_dict.keys())

    while True:
        random.shuffle(latin_list)
        hiragana = random.choice(list(hiragana_dict.values()))
        correct_latin = [k for k, v in hiragana_dict.items() if v == hiragana][0]
        
        user_input = input(f"Latin for '{hiragana}': ")

        if user_input.lower() == correct_latin.lower():
            print(f"{GREEN}Correct!{RESET}\n")
        else:
            print(f"{RED}Incorrect. The correct answer is '{correct_latin}'.{RESET}\n")

if __name__ == "__main__":
    main()
