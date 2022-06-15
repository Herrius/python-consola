import random

from scipy import rand
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print('What do you choose?')
print('0 - Rock 1 - Paper 2 - Scissor')
choose=int(input("you choose: "))
computer=random.randint(0,2)

if(choose==0):
    if(computer==0):
        print(f"you: {rock}")
        print(f"computer {rock}")
        print("Draw")
    elif(computer==1):
        print(f"you: {rock}")
        print(f"computer {paper}")
        print("Lose")
    else:
        print(f"you: {rock}")
        print(f"computer {scissors}")
        print("Win")
else:
    if(choose==1):
        if(computer==0):
            print("Win")
        elif(computer==1):
            print("Draw")
        else:
            print("Lose")
    else:
        if(computer==0):
            print("Lose")
        elif(computer==1):
            print("Win")
        else:
            print("Draw")
