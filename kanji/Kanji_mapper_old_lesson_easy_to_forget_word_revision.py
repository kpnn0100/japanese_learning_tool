from kanjitool import *
import os
import random
from Config import *

today_word_list = getShuffledEzToForget()
all_word_list = getShuffledEzToForget()
# get random row form today_word_list
correct = 0
total = 0
for index, word in today_word_list.iterrows():
    # switch case for mode
    if total != 0:
        print(f"correct: {correct}, total: {total}, rate: {correct/total}")
    total += 1
    ret = show_question(word['kanji'], word['romaji'], word['meaning'],word['kanji'])
    if ret:
        correct += 1
# Rest of your code goes here