import pandas as pd
import os
import argparse
# Create a sample DataFrame
# Get the current file path
index_file = os.path.join(os.path.dirname(__file__), "index.txt")
level = 5
number = 0
from gtts import gTTS
import os
import random
import pygame
import threading
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
# from tool.tool import *
def speak_japanese(phrase):
    pygame.mixer.init()
    tts = gTTS(text=phrase, lang='ja')
    audio_file = f'{phrase}.mp3'
    tts.save(audio_file)
    def play_audio():
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()
    thread = threading.Thread(target=play_audio)
    thread.start()
    thread.join()
    pygame.mixer.quit()
    os.remove(audio_file)
def show_question(show_word, row):
    print(show_word)
    user_input = input("romaji: ")
    # speak_japanese(speak_word)
    if user_input == row['romaji']:
        printCorrect()
        print(f"{row['hanviet']} {row['kanji']} {row['meaning']}")
        return True
    printIncorrect(row['romaji'])
    print(f"{row['hanviet']} {row['kanji']} {row['meaning']}")
    return False
    
def printCorrect():
    print("\033[92mCorrect!\033[0m" + "-------")
def printIncorrect(correct_answer):
    print("\033[91mIncorrect!\033[0m" )
    print(f"Answer is: {correct_answer} " + "-------")
def getShuffledEzToForget():
    current_path = os.path.abspath(__file__)

    # Get the relative path to the CSV file
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'revision.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    df.loc[df["kanji"] == " ", "kanji"] = df["furigana"]
    # Shuffle the DataFrame with a fixed seed
    shuffled_df = df.sample(frac=1).reset_index(drop=True)

    return shuffled_df
def getShuffledKanjiDataFrame():
    current_path = os.path.abspath(__file__)

    # Get the relative path to the CSV file
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'jlpt', f'n{level}.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    df = df.drop(columns=['tags'])
    df = df.drop(columns=['guid'])
    df.loc[df["kanji"] == " ", "kanji"] = df["furigana"]
    # Shuffle the DataFrame with a fixed seed
    shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return shuffled_df
def processIndexAndLevel():
    global number,level
    if not os.path.exists(index_file):
        with open(index_file, "w") as file:
            file.write("0\n5")
            number = 0
    else:
        with open(index_file, "r") as file:
            number = int(file.readline())
            level = int(file.readline())
    if args.increment:
        number += 1
        with open(index_file, "w") as file:
            file.write(str(number) + "\n" + str(level))
        exit()  
def getWordRange(start, end):
    df = getShuffledKanjiDataFrame()
    selected_words = df.iloc[start:end]
    return selected_words
def getTodayWords(learning_rate):
    start = number * learning_rate
    end = start + learning_rate
    selected_words = getWordRange(start, end)
    print(selected_words)
    return selected_words
def getOldWords(learning_rate):
    processIndexAndLevel()
    start = 0
    end = (number) * learning_rate

    if number == 0:
        end = learning_rate
    print (f"start: {start}, end: {end}")
    selected_words = getWordRange(start, end)
    print(selected_words.drop(columns=['romaji']))
    return selected_words
def getOldWordsWithDepth(learning_rate, depth):
    if depth == 0:
        return getOldWords(learning_rate)
    processIndexAndLevel()
    start = (number) * learning_rate-depth
    end = (number) * learning_rate

    if number == 0:
        end = learning_rate
    print (f"start: {start}, end: {end}")
    selected_words = getWordRange(start, end)
    print(selected_words.drop(columns=['romaji']))
    return selected_words
def getOldWordsWithDepthAndShuffle(learning_rate,depth):
    df = getOldWordsWithDepth(learning_rate,depth)
    return df.sample(frac=1).reset_index(drop=True)

def getOldVerb(learning_rate,depth):
    df = getOldWordsWithDepthAndShuffle(learning_rate,depth)
    # verb = pd.DataFrame(columns = ["kanji","furigana","meaning","tags","guid","romaji"])
    verb = pd.DataFrame()
    for index, row in df.iterrows():
        if str(row["meaning"]).startswith("to "):
            verb= pd.concat([verb, pd.DataFrame([row])], ignore_index=True) 
    return verb
def add_word_to_revision(row):
    current_path = os.path.abspath(__file__)

    # Get the relative path to the CSV file
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'revision.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    # check if the word is already in the revision
    if not df[df['kanji'] == row['kanji']].empty:
        return
    #use concat to add the row to the dataframe
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(csv_path, index=False)
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--increment", action="store_true", help="Increment the index by 1")
parser.add_argument("-p", "--decrement", action="store_true", help="Decrement the index by 1")
parser.add_argument("-u", "--up", action="store_true", help="Up to upper level")
parser.add_argument("-d", "--down", action="store_true", help="Down to lower level")
args = parser.parse_args()
def saveNumberAndLevel():
    with open(index_file, "w") as file:
        file.write(str(number) + "\n" + str(level))
if not os.path.exists(index_file):
    saveNumberAndLevel()
else:
    with open(index_file, "r") as file:
        number = int(file.readline())
        level = int(file.readline())
if args.increment:
    number += 1
    print(f"lesson {number}")
    saveNumberAndLevel()
if args.decrement:
    number -= 1
    number = max(0, number)
    print(f"lesson {number}")
    saveNumberAndLevel()
if args.up:
    level = level - 1
    level = min(5, level)
    level = max(1, level)
    print(f"level n{level}")
    saveNumberAndLevel()
if args.down:
    level += 1
    level = min(5, level)
    level = max(1, level)
    print(f"level n{level}")
    saveNumberAndLevel()
def save_learned_words():
    current_path = os.path.abspath(__file__)

    # Get the relative path to the CSV file
    csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', 'learned_word.csv')
    learned = getOldWordsWithDepth(10,0)
    learned.to_csv(csv_path, index=False)