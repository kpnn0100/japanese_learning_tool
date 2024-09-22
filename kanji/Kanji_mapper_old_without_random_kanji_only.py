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
hiragana_furigana = ''.join(hiragana_table['furigana'])
katakana_furigana = ''.join(katakana_table['furigana'])
for index, word in today_word_list.iterrows():
    # switch case for mode
    new_kanji = ''
    for i in range(0, len(word['kanji'])):
        if word['kanji'][i] in hiragana_furigana or word['kanji'][i] in katakana_furigana:
            break
        new_kanji += word['kanji'][i]
    if new_kanji == '':
        continue
    if total != 0:
        print(f"correct: {correct}, total: {total}, rate: {correct/total}")
    total += 1
    ret = show_question(new_kanji, word)
    if ret:
        correct += 1

# Rest of your code goes here