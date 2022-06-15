import random
import hangman.art_hangman as art_hangman,hangman.dictionary_hangman as dictionary_hangman

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_choose=random.choice(dictionary_hangman.word_list)
word_array=[]
lives=6

for x in word_choose:
    word_array.append('_')

end_of_game = False

print(art_hangman.logo)
while not end_of_game:
    progress=word_array.count('_')
    chara=input('Guess a letter: ').lower()

    for letter in range(len(word_choose)):
        if word_choose[letter]==chara:
            word_array[letter]=chara
    print(word_array)
    
    if chara in word_array:
        print(f"You have used the letter {chara}")

    if chara not in word_choose:
        print(f"You guessed {chara}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in word_array:
       end_of_game=True
       print("You win.")

    print(art_hangman.stages[lives])