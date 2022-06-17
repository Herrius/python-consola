import random
from art import logo, vs
from game_data import data
import os


def choose_data():
    temp = random.choice(data)
    data.remove(temp)
    return temp

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers,save):
  if a_followers["follower_count"] > b_followers["follower_count"]:
    save=a_followers
    return [guess == "A",save]
  else:
    save=b_followers
    return [guess == "B",save]

def main():
    score = 0
    end_game = False
    save = []
    data_a = choose_data()
    data_b = choose_data()
    # Imprimir los logos
    while not end_game:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        if len(save)>0:
            data_a=save
        else:
            data_a = choose_data()
        data_b = choose_data()
        # conseguir un dato de game_data
        print(f"Compare A: {format_data(data_a)}.")
        print(vs)
        print(f"Compare B: {format_data(data_b)}.")
        # verificar que no sean repetidos los dos datos seleccionados
        # pedir la respuesta
        answer = input(f"Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = check_answer(answer, data_a, data_b,save)
        if is_correct[0]:
            os.system('cls')
            score += 1
            save=is_correct[1]
        else:
            os.system('cls')
            print(f"Your lose. Current score: {score}")
            finish = input(f"Would you play again?(Y or N)").lower()
            if finish == 'n':
                end_game = True

    # Tener un contador que cuenta la puntuacion
main()
