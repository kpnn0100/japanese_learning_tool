import os
import pandas as pd
import googletrans
import threading
from concurrent.futures import ThreadPoolExecutor
import time


folder_path = os.path.dirname(os.path.abspath(__file__))
file_name = "../resource/n5_kanji.txt"
input_file = os.path.join(folder_path, file_name)

# Read the input file
with open(input_file, 'r') as f:
    kanji_characters = f.read().strip()
translator = googletrans.Translator()
# Look up the meaning of each kanji character
meanings = []
df = pd.DataFrame()
lock = threading.Lock()
counter = 0
def lookup_meaning(kanji):
    global df, executor, lock, counter
    try:
        meaning = translator.translate(kanji, src='zh-CN', dest='en').text

        lock.acquire()
        try:
            new_row = {'Kanji': kanji, 'Meaning': meaning}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            counter += 1
            print(f"Counter: {counter}")
        finally:
            lock.release()
        print(f"Kanji: {kanji}, Meaning: {meaning}")
    except Exception as e:
        print(f"Error occurred while looking up the meaning of kanji '{kanji}': {str(e)}")
        meanings.append(None)
        executor.submit(lookup_meaning, kanji)  # Retry the task

threads = []
# Define the maximum number of threads in the thread pool
max_threads = 4

# Create a thread pool executor
executor = ThreadPoolExecutor(max_workers=max_threads)

# Submit tasks to the thread pool
for kanji in kanji_characters:
    executor.submit(lookup_meaning, kanji)

# Shutdown the executor and wait for all tasks to complete
executor.shutdown(wait=True)

# Create a DataFrame to store the kanji characters and their meanings
print(df)

# Wait for all threads to finish
for t in threads:
    t.join()
    

# Create a DataFrame to store the kanji characters and their meanings
df.to_csv('kanji_meanings.csv', index=False)
print(df)