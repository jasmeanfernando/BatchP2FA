"""
Class that imports pandas to enable production of transcription files (.txt) using .csv file.

.csv file contains written transcriptions of all the audio files (.wav) labeled p14,
which is the contrastive stress production cases collected by Language Acquisition and Processing Lab.

All transcription files (.txt) will be stored in P2FA's input_txt directory so that align.py can
be run for this data.
"""
from pathlib import Path
from pandas import *

# Obtain .csv file from local directory.
csv_file = '/Users/jasmeanfernando/Desktop/Research/P2FA/csv_files/FALL_2021.csv'

# Obtain local directory to store .txt file.
transcription_dir = Path('/Users/jasmeanfernando/PycharmProjects/BatchP2FA/p2fa/input_txt')

# Read .csv file.
column = read_csv(csv_file)

# Compile each column to a list.
participants = column["Participant number"].tolist()
trials = column["Trial"].tolist()
transcriptions = column["Transcription"].tolist()

# Generate transcription file (.txt) in the format of participant#_p14_trial#.txt.
index = 0
for text in transcriptions:
    # Initialize .txt file.
    text_file_name = str(participants[index]) + "_" + str(trials[index]) + ".txt"
    txt_path = transcription_dir.joinpath(text_file_name)

    # Base Case: Check if directory exists.
    if transcription_dir.is_dir():
        # Base Case: Check if .txt file /already/ exists.
        if txt_path.is_file():
            print("File already exists, cannot re-write.")
        else:
            # Write and store .txt file.
            with open(txt_path, 'w') as file:
                file.write(str(text))
                print(str(text))
    else:
        print("Directory does not exist.")

    # Use index to move to next row on .csv file.
    index = index + 1