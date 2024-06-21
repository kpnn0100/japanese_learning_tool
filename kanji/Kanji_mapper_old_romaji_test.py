from kanjitool import *
import os
import random
from Config import *

depth = 0
depth = int(input("Enter the depth of the old lesson: "))
today_word_list = []
if depth == 0:
    today_word_list = getOldWords(learning_rate)
else:
    today_word_list = getOldWordsWithDepth(learning_rate, depth)
all_word_list = getShuffledKanjiDataFrame()
# get random row form today_word_list
while True:
    print("---------------------")
    row = today_word_list.sample()
    noise_word = all_word_list.copy()
    #remove row from noise_word
    print(f'guess the meaning: \n')
    print(row['romaji'].values[0])
    user_input = input()
    print(row['meaning'].values[0])
    user_input = input("continue...")
    

# Rest of your code goes here