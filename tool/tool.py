import pandas as pd
import os
import argparse
import unicodedata
from enum import Enum
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
    if verb == "kuru" or verb == "suru":
        return True
    if verb.endswith('eru') or verb.endswith('iru'):
        return True
    return False
class VerbForm(Enum):
    PLAIN_PRESENT = 1
    PLAIN_PAST = 2
    TE_FORM = 3
    VOLITIONAL_FORM = 4
    POTENTIAL_FORM = 5
    CAUSATIVE_FORM = 6
    PASSIVE_FORM = 7
    IMPERATIVE_FORM = 8
    CONDITIONAL_FORM = 9
    PROVISIONAL_FORM = 10
    TAI_FORM = 11
    NEGATIVE_FORM = 12
    POLITE_PRESENT = 13
    POLITE_PAST = 14
    POLITE_VOLITIONAL_FORM = 15
    POLITE_POTENTIAL_FORM = 16
    POLITE_CAUSATIVE_FORM = 17
    POLITE_PASSIVE_FORM = 18
    POLITE_IMPERATIVE_FORM = 19
    POLITE_CONDITIONAL_FORM = 20
    POLITE_PROVISIONAL_FORM = 21
    POLITE_TAI_FORM = 22
    POLITE_NEGATIVE_FORM = 23

def conjugate_verb(verb, form):
    if isIchidan(verb):
        verb = verb[:-2]
        if form == VerbForm.PLAIN_PRESENT:
            return verb + 'ru'
        elif form == VerbForm.PLAIN_PAST:
            return verb + 'ta'
        elif form == VerbForm.TE_FORM:
            return verb + 'te'
        elif form == VerbForm.VOLITIONAL_FORM:
            return verb + 'yo'
        elif form == VerbForm.POTENTIAL_FORM:
            return verb + 'ru'
        elif form == VerbForm.CAUSATIVE_FORM:
            return verb + 'seru'
        elif form == VerbForm.PASSIVE_FORM:
            return verb + 'rareru'
        elif form == VerbForm.IMPERATIVE_FORM:
            return verb + 'ro'
        elif form == VerbForm.CONDITIONAL_FORM:
            return verb + 'ba'
        elif form == VerbForm.PROVISIONAL_FORM:
            return verb + 'tara'
        elif form == VerbForm.TAI_FORM:
            return verb + 'tai'
        elif form == VerbForm.NEGATIVE_FORM:
            return verb + 'nai'
        elif form == VerbForm.POLITE_PRESENT:
            return verb + 'masu'
        elif form == VerbForm.POLITE_PAST:
            return verb + 'mashita'
        elif form == VerbForm.POLITE_VOLITIONAL_FORM:
            return verb + 'mashou'
        elif form == VerbForm.POLITE_POTENTIAL_FORM:
            return verb + 'masu'
        elif form == VerbForm.POLITE_CAUSATIVE_FORM:
            return verb + 'seru'
        elif form == VerbForm.POLITE_PASSIVE_FORM:
            return verb + 'rareru'
        elif form == VerbForm.POLITE_IMPERATIVE_FORM:
            return verb + 'nasai'
        elif form == VerbForm.POLITE_CONDITIONAL_FORM:
            return verb + 'masu'
        elif form == VerbForm.POLITE_PROVISIONAL_FORM:
            return verb + 'tara'
        elif form == VerbForm.POLITE_TAI_FORM:
            return verb + 'tai'
        elif form == VerbForm.POLITE_NEGATIVE_FORM:
            return verb + 'masen'
        else:
            return "Invalid form"
    else:
        #todo godan verb
        return "Not implemented yet"

print(conjugate_verb('taberu',VerbForm.POLITE_PRESENT))