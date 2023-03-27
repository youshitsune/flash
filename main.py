import sys
import random
import os

def main(filename):
    with open(filename, "r") as f:
        ctx = f.read()
    ctx = ctx.split(";")
    flashcards = []
    for i in ctx:
        flashcards.append((i.split("-")[0], i.split("-")[1]))
    os.system("clear")
    while True:
        flashcard = random.choice(flashcards)
        print()
        print("Q:")
        print(flashcard[0])
        print()
        user_input = input(":")
        if user_input == "e" or user_input == "exit" or user_input == "quit" or user_input == "q":
            break
        else:
            os.system("clear")
            print()
            print("A:")
            print(flashcard[1])
            print()
            user_input = input(":")
            if user_input == "e" or user_input == "exit" or user_input == "quit" or user_input == "q":
                break
            else:
                os.system("clear")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("HELP: python3 main.py <path_to_file>")
    else:
        main(sys.argv[1])
