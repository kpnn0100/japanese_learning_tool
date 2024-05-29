import os
import pandas as pd

def create_dataframe(start, end):
    # Get the absolute path of the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'resource', 'n5_words.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Select the word range based on the start and end arguments
    selected_words = df.iloc[start-1:end]

    return selected_words

# Example usage
start_num = int(input("Enter the start number: ") or 0)
end_num = int(input("Enter the end number: ") or 10)
selected_df = create_dataframe(start_num, end_num)
print()
print(selected_df)