from kanjitool import *
import os
import random
from Config import *

today_word_list = getOldWords(learning_rate)
all_word_list = getShuffledKanjiDataFrame()


# get random row form today_word_list
while True:
    print("---------------------")
    row = today_word_list.sample()
    noise_word = all_word_list.copy()
    #remove row from noise_word
    noise_word = noise_word.drop(row.index)
    # mode = random.randint(0, 2)
    mode = random.randint(2, 3)
    #if the word don't have kanji (kanji = " ") then mode should be minus
    if row['kanji'].values[0] == " ":
        mode = -mode-1
    # switch case for mode
    if mode == 0:
        print(f'which is the meaning of this word: \n')
        print(row['kanji'].values[0])
        print("Choose the correct meaning:")
        choices = noise_word.sample(n=number_of_noise_word)['meaning'].tolist()
        choices.append(row['meaning'].values[0])
        random.shuffle(choices)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_input = input("Enter the number of the correct meaning: ")
        while not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            user_input = input("Enter the number of the correct meaning: ")
        if int(user_input) == choices.index(row['meaning'].values[0]) + 1:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['meaning'].values[0]}")
    elif mode == 1:
        print(f'which is the kanji of this word: \n')
        print(f"\"{row['meaning'].values[0]}\"")
        print("Choose the correct kanji:")
        choices = noise_word.sample(n=number_of_noise_word)['kanji'].tolist()
        choices.append(row['kanji'].values[0])
        random.shuffle(choices)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_input = input("Enter the number of the correct kanji: ")
        while not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            user_input = input("Enter the number of the correct kanji: ")
        if int(user_input) == choices.index(row['kanji'].values[0]) + 1:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['kanji'].values[0]}")
    elif mode == 2:
        print(f'what is the romaji of this kanji: \n')
        print(row['kanji'].values[0])
        user_input = input("Enter the romaji: ")
        if user_input == row['romaji'].values[0]:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['romaji'].values[0]}")
    elif mode == 3:
        print(f'what is the romaji of this word: \n')
        print(row['meaning'].values[0])
        user_input = input("Enter the romaji: ")
        if user_input == row['romaji'].values[0]:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['romaji'].values[0]}")
    else:
        print()
    

# Rest of your code goes here