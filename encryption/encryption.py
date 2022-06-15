import logo
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_message,shift_amount,type_message):
    text=''
    if type_message == "decode":
        shift_amount *= -1
    for letter in text_message: 
        if letter in alphabet:
            pos=alphabet.index(letter)
            pos=shift_amount+pos
            if pos>=len(alphabet):
                pos=pos-len(alphabet)
            elif pos <0:
                pos=len(alphabet)-abs(pos)
            new_letter=alphabet[pos]
            text+=new_letter
        else:
            text+=letter
    print(text)

def main():
    exit=True
    while exit:
        print(logo.logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift<27 and shift>0:
            caesar(type_message=direction,shift_amount=shift,text_message=text)
        else:
            print("shift should is between 0 to 27")
        answer=input('Would you repeat the program?(Yes or no)').lower()
        if answer=='yes':
            exit=False
        else:
            os.system('cls')
main()