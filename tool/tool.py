import pandas as pd
import os
import argparse
import unicodedata
from enum import Enum
from define import *
import pykakasi

# Initialize pykakasi
kakasi = pykakasi.kakasi()

current_path = os.path.abspath(__file__)
csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'hiragana.csv')
hiragana_table = pd.read_csv(csv_path)
furigana_to_romaji = {}
for index, row in hiragana_table.iterrows():
    furigana = row['furigana']
    romaji = row['romaji']
    furigana_to_romaji[furigana] = romaji

def get_romaji(furigana):
    romaji = kakasi.convert(furigana)
    romaji_text = ''.join([item['hepburn'] for item in romaji])
    return romaji_text
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


def open_word_data_as_dataframe(index):
    current_path = os.path.abspath(__file__)
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'jlpt', f"n{index}.csv")
    df = pd.read_csv(csv_path)
    return df
def save_dataframe(dataframe, index):
    current_path = os.path.abspath(__file__)
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'jlpt', f"n{index}.csv")
    dataframe.to_csv(csv_path, index=False)
    return dataframe
def add_romaji_column_to_dataframe(dataframe):
    romaji_list = []
    for index, row in dataframe.iterrows():
        furigana = row['furigana']
        if furigana == None:
            furigana = row['kanji']
        romaji = get_romaji(furigana)
        romaji_list.append(romaji)
    dataframe['romaji'] = romaji_list
    return dataframe
def rename_column(dataframe, old_column_name, new_column_name):
    dataframe.rename(columns={old_column_name: new_column_name}, inplace=True)
    return dataframe
index = 1
data = open_word_data_as_dataframe(index)
data = rename_column(data,"expression","kanji")
data = rename_column(data,"reading","furigana")
data = add_romaji_column_to_dataframe(data)
save_dataframe(data,index)

