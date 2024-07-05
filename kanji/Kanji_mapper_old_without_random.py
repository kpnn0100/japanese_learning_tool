from kanjitool import *
import os
import random
from Config import *

depth = 0
depth = int(input("depth of the old lesson: "))
today_word_list = getOldWordsWithDepthAndShuffle(learning_rate, depth)
# get random row form today_word_list
correct = 0
total = 0
for index, word in today_word_list.iterrows():
    # switch case for mode
    if total != 0:
        print(f"correct: {correct}, total: {total}, rate: {correct/total}")
    total += 1
    print(word['kanji'])
    user_input = input("romaji: ")
    if user_input == word['romaji']:
        correct += 1
        printCorrect()
    else:
        printIncorrect(word['romaji'])
    print(word['meaning'])
    

# Rest of your code goes here