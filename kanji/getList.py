from kanjitool import *
from Config import *
import csv
data = getOldWords(learning_rate)
# Assuming `data` is a list of dictionaries
data["kanji" == " " or "kanji" == None] = data["furigana"]
data = data["kanji"]
filename = "kanji_data.csv"
with open("kanji_data.txt", "w") as file:
    for item in data:
        file.write(str(item) + "\n")