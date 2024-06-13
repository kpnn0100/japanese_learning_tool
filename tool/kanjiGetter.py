import re
import os

def extract_kanji(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    kanji = re.findall(r'[\u4e00-\u9faf]', text)
    kanji = list(set(kanji))  # Remove duplicates
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(kanji))

# Usage example
folder_path = os.path.dirname(os.path.abspath(__file__))
file_name = "../resource/n5_words.csv"
input_file = os.path.join(folder_path, file_name)
output_file = 'kanji_n5.txt'
extract_kanji(input_file, output_file)
