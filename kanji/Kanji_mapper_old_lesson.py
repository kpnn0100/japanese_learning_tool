from kanjitool import *
import os
import random
from Config import *

depth = 0
depth = int(input("depth of the old lesson: "))
today_word_list = []
if depth == 0:
    today_word_list = getOldWords(learning_rate)
else:
    today_word_list = getOldWordsWithDepth(learning_rate, depth)
all_word_list = getShuffledKanjiDataFrame()
# get random row form today_word_list
while True:
    row = today_word_list.sample()
    noise_word = all_word_list.copy()
    #remove row from noise_word
    noise_word = noise_word.drop(row.index)
    row = row.iloc[0]
    # mode = random.randint(0, 2)
    mode = random.randint(1, 2)
    question = ""
    if mode == 1:
        question = row['kanji']
    elif mode == 2:
        question = row['meaning']
    show_question(question,row)
    

# Rest of your code goes here