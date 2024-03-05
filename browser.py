import os

software = {'firefox': 'firefox', 'youtube': 'firefox https://youtube.com'}


def opening_fun(open_operation):
    if open_operation in software.keys():
        opening_command = os.system("firefox")
        return opening_command
    else:
        print("ERROR")


def extract_open_operation(input_audio):
    words = input_audio.split()  # Using  words to extract
    if 'open' in words:
        index = words.index('open')
        if index < len(words) - 1:  # Check if 'open' is not the last word
            open_operation = words[index + 1]
        else:
            print("No operation found after 'open'.")
    else:
        print("No operation found")
