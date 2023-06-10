import os, fnmatch

# Obtain specific directory where all the .txt and .wav files exist.
dir = '/Users/jasmeanfernando/PycharmProjects/BatchP2FA/p2fa/p2fa_input'

# Compile directory into an arraylist.
arglist = []
input_list = os.listdir(dir)

# Loop through the directory and generate a .TextGrid file for each.
# Save .TextGrid file in specific directory in the format of participant_trial.TextGrid.
for text_file in input_list:
    # Initialize .TextGrid name.
    text_grid_name = text_file.split(".")[0] + '.TextGrid'

    # Obtain current file name being evaluated in input_list (.txt file).
    current_file_name = text_file.split(".")[0] + '.txt'

    # Check if current_file_name (.txt) has a matching wave file (.wav) in directory.
    if fnmatch.fnmatch(text_file, '*.wav') and current_file_name in input_list:
        arglist.append([text_file, current_file_name, text_grid_name])
    elif fnmatch.fnmatch(text_file, '*.wav') and not current_file_name in input_list:
        print('No matching .txt file for ' + text_file + '; Skipping file...')

# Calls P2FA to generate .TextGrid files.
i = 0
for vars in arglist:
    print('Now creating...' + arglist[i][2])
    os.system('python3 align.py p2fa_input/' + arglist[i][0] + ' p2fa_input/' + arglist[i][1] + ' p2fa_output/' + arglist[i][2])
    i = i + 1