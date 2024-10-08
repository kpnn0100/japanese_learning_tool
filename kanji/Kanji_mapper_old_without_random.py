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
    ret = show_question(word['kanji'], word)
    if ret:
        correct += 1
    else:
        print(word)
        add_word_to_revision(word)

# Rest of your code goes here