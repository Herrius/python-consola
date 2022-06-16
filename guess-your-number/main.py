import art
import random

global choose_number
choose_number=random.randint(1,100)

def dificulty():
    mode=input("Do you prefer mode 'easy'(5 attempt) or 'hard'(10 attempt)")
    if mode=='easy':
        mode=10
    else:
        mode=5
    return mode

def main():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mode=dificulty()
    while mode > 0:
        person_number=input("What is the number? ")
        if person_number > choose_number:
            print(f"The number {person_number} is too high")
        elif person_number < choose_number:
            print(f"The number {person_number} is too low")
        else:
            print(f"The number {person_number} is the answer")
            break
        mode-=1

