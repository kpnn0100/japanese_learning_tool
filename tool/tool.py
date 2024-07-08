import pandas as pd
import os
import argparse
import unicodedata
from enum import Enum
from define import *
current_path = os.path.abspath(__file__)
csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'hiragana.csv')
hiragana_table = pd.read_csv(csv_path)
furigana_to_romaji = {}
for index, row in hiragana_table.iterrows():
    furigana = row['furigana']
    romaji = row['romaji']
    furigana_to_romaji[furigana] = romaji

def get_romaji(furigana):
    romaji = ""
    double = False
    for char in furigana:
        if char in 'ゃゅょ':
            if len(romaji)>2:
                if romaji[len(romaji)-3:]=="shi" or romaji[len(romaji)-3:]=="chi":
                    romaji = romaji[:-1]
                    romaji += furigana_to_romaji[char][1]
                elif romaji[len(romaji)-2:]=="ji":
                    romaji = romaji[:-1]
                    romaji += furigana_to_romaji[char][1]
                else:
                    romaji = romaji[:-1]
                    romaji += furigana_to_romaji[char]
            elif len(romaji)>1:
                if romaji[len(romaji)-2:]=="ji":
                    romaji = romaji[:-1]
                    romaji += furigana_to_romaji[char][1]
                else:
                    romaji = romaji[:-1]
                    romaji += furigana_to_romaji[char]

            None
        elif char == 'っ':
            double = True
            None
        else:
            if double:
                romaji += furigana_to_romaji[char][0]
                double = False
            romaji += furigana_to_romaji[char]
    return romaji
def isIchidan(verb):
    is_written_in_hiragana = True
    for char in verb:
        if char not in furigana_to_romaji:
            is_written_in_hiragana = False
    if is_written_in_hiragana:
        verb = get_romaji(verb)
    if verb == "kuru" or verb == "suru":
        return True
    if verb.endswith('eru') or verb.endswith('iru'):
        return True
    return False
def conjugate_verb(verb, form):
    if isIchidan(verb):
        verb=verb[:-2]
        verb+=form.ichidan_ending
        return verb
    else:
        verb=verb[:-1]
        verb+=form.godan_ending
        return verb
for form in JapaneseVerbForms:
    print(conjugate_verb('taberu',form.value))