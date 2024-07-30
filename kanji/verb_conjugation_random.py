from kanjitool import *
import os
import random
from Config import *

depth = 0
depth = int(input("depth of the old lesson: "))
today_word_list = getOldVerb(learning_rate, depth)
# get random row form today_word_list
while True:
    row = today_word_list.sample()
    base = random.choice(list(BaseForm))
    tense = random.choice(list(Tense))
    polarity = random.choice(list(Polarity))
    meaning = row['meaning'].values[0]
    form = conjugate_verb(row['kanji'].values[0], base, Formality.PLAIN, tense, polarity)
    print(f'form of this? {form}')
    print(f'answer: is {base.name} {tense.name} {polarity.name}')
    print(f'meaning? {meaning}')
    input("continue...")
    # mode = random.randint(0, 2)
    
    

# Rest of your code goes here