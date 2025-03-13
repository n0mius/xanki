#!/usr/bin/python   
# ███▄▄▄▄    ▄██████▄    ▄▄▄▄███▄▄▄▄    ▄█  ███    █▄     ▄████████ 
# ███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ ███  ███    ███   ███    ███ 
# ███   ███ ███    ███ ███   ███   ███ ███▌ ███    ███   ███    █▀  
# ███   ███ ███    ███ ███   ███   ███ ███▌ ███    ███   ███        
# ███   ███ ███    ███ ███   ███   ███ ███▌ ███    ███ ▀███████████ 
# ███   ███ ███    ███ ███   ███   ███ ███  ███    ███          ███ 
# ███   ███ ███    ███ ███   ███   ███ ███  ███    ███    ▄█    ███ 
#  ▀█   █▀   ▀██████▀   ▀█   ███   █▀  █▀   ████████▀   ▄████████▀                                                      
# [XANKI] V 1.2
# made by nomius@420blaze.it

import random
import argparse
import difflib

def read_flashcards(file_path):
    flashcards = []
    with open(file_path, 'r') as file:
        flashcard = {'question': '', 'answer': ''}
        is_reading_question = False

        for line in file:
            line = line.strip()

            if line == "#Q":
                is_reading_question = True
            elif line == "#A":
                is_reading_question = False
            elif line == "#END":
                flashcards.append(flashcard)
                flashcard = {'question': '', 'answer': ''}
            else:
                if is_reading_question:
                    flashcard['question'] += line
                else:
                    flashcard['answer'] += line

    return flashcards

def compare_similarity(answer, user_input):
    s = difflib.SequenceMatcher(None, answer, user_input)
    return s.ratio() * 100

def main():
    parser = argparse.ArgumentParser(description="Flashcard Reader")
    parser.add_argument("-f", "--file", required=True, help="Path to the flashcards file")
    args = parser.parse_args()

    flashcards = read_flashcards(args.file)

    random.shuffle(flashcards)

    while True:
        for flashcard in flashcards:
            flashcard['question'] = flashcard['question'].replace('\\n\\', '\n')
            flashcard['answer'] = flashcard['answer'].replace('\\n\\', '\n')
            print('\n')
            print(str(flashcard['question']))
            print('\n' *2)
            user_input = input(": ")
            similarity_percentage = compare_similarity(flashcard['answer'], user_input)
            print('\n', flashcard['answer'])
            print(f"----[ similarity: {similarity_percentage:.2f}% ]----")
            input()
            print('\n' * 3)

if __name__ == "__main__":
    main()
