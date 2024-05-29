import csv
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file path")
parser.add_argument("--output", help="output file path")
args = parser.parse_args()

input_file = args.input
output_file = args.output

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

hiragana_list = []
for line in lines:
    line = line.strip()
    if line:
        hiragana, romaji = line.split()
        hiragana_list.append([hiragana, romaji])

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(hiragana_list)
