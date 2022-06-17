import art
import random

global choose_number
choose_number=random.randint(1,100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def dificulty():
    mode=input("Do you prefer mode 'easy'(10 attempt) or 'hard'(5 attempt) ")
    if mode=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def main():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempt=dificulty()
    while attempt > 0:
        person_number=int(input("What is the number? "))
        if person_number > choose_number:
            print(f"The number {person_number} is too high")
        elif person_number < choose_number:
            print(f"The number {person_number} is too low")
        else:
            print(f"The number {person_number} is the answer")
            break
        print(f"You have {attempt} attempt")
        attempt-=1
    if attempt==0:
        print(f"You lose 😭. The answer is {attempt}")
main()