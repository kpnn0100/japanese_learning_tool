import csv
import re
import pandas as pd

input_file = "/home/namdln/learning/japanese_learning_tool/word/n5_words.txt"
output_file = "/home/namdln/learning/japanese_learning_tool/word/n5_words.csv"

with open(input_file, "r") as file:
    lines = file.readlines()

dict = {
    "kanji": [],
    "furigana": [],
    "romaji": [],
    "meaning": []
}

df = pd.DataFrame(dict)
for line in lines:
    if len(line) <2:
        continue
    missing_kanji = False
    if line.startswith(' '):
        line = line[1:]
    elif line.startswith('	'):
        missing_kanji = True
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    data = re.sub(' +', ' ',line)
    data = data.strip().split(" ")
    if len(data) < 3:
        continue
    if len(data) < 4 and missing_kanji == False:
        continue
    i = 0

    kanji = data[i]
    if missing_kanji:
        i = -1
        kanji = " "
    furigana = data[i+1]
    romaji  = data[i+2]
    meaning = " ".join(data[i+3:])
    data = {
        "kanji": kanji,
        "furigana": furigana,
        "romaji": romaji,
        "meaning": meaning
    }
    df = df._append(data, ignore_index = True)

df.to_csv(output_file, index=False)

print("Conversion to CSV format is complete.")
