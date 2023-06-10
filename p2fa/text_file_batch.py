from pathlib import Path
from pandas import *

# Obtain .csv file from specific directory.
csv_file = '/Users/jasmeanfernando/Desktop/RAProgram/csv_files/SPRING_2022.csv'

# Read .csv file columns.
data = read_csv(csv_file)

# Convert columns to arraylists.
participants = data['Participant number'].tolist()
trials = data['Trial'].tolist()
transcripts = data['Transcription'].tolist()

# Loop through transcription column and generate an individual .txt file for each.
# Save .txt file in specific directory in the format of participant_trial.txt.
index = 0
for transcript_row in transcripts:
    # Initialize .txt file name.
    text_file_name = str(participants[index]) + "_" + str(trials[index]) + ".txt"

    # Find directory to save .txt file.
    directoryPath = Path('/Users/jasmeanfernando/PycharmProjects/BatchP2FA/p2fa/p2fa_input')
    filePath = directoryPath.joinpath(text_file_name)

    # Check if directory exists.
    if directoryPath.is_dir():
        # Check if .txt file already exists.
        if filePath.is_file():
            print('File already exists.')
        # Write and save .txt file.
        else:
            with open(directoryPath.joinpath(text_file_name), 'w') as file:
                file.write(str(transcript_row))
                print(str(transcript_row))
    else:
        print('Directory does not exist! Please create the directory first.')

    # Increment index to move along the participants and trials arraylists.
    index = index + 1