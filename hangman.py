#this project requires two players One to type in the word, one to guess.
#import os because after player 1 chooses a word, we want to clear the sceen to avoid cheating
#system is to run commands, name is to find out the os so we issue the correct command
#WARNING: this is probably not very optimized
from os import system, name
from time import sleep


#this will be the letters for the word p1 enters
word_list = []
final_word = ''
#list of all attempted guesses
guessed_letters = []
#current letter being guessed
current_guess = ''
#status of the game
status = ''
mistakes = 0
#the amount of tries they get
max_guesses = 7
#blanks representing each of the letters
blanks = list("_" * len(word_list))

def clear ():
    #if windows
    if name == 'nt':
        _ = system('cls')
    #if literally anyone else
    else:
        _ = system('clear')

clear()

def break_word(word):
    #breaks the full string into a list
    for letter in word:
        word_list.append(letter)

def find_occurances(list, letter):
    global indices
    indices = []
    for idx, value in enumerate(list):
        if value == letter:
            indices.append(idx)
    return indices

def check_letter(letter):
    global mistakes
    clear()
    print(letter)
    #this will check the letter against word_list and guessed_letters
    if letter in guessed_letters:
        print('You already guessed that letter!')
        mistakes += 1
        sleep(1)

    if letter in word_list:
        find_occurances(word_list, letter)
        for num in indices:
            blanks[num] = word_list[num]
        print(blanks)
    
    guessed_letters.append(letter)

       

#get the word from p1, convert it to lowercase
#break the word into individual letters and clear the console
#set the status to ready
p1_input = input('Whats the word? ')
word = p1_input.lower()
final_word = word
break_word(word)
clear()
print(f'The word is, {word}, this screen will clear in two seconds')
sleep(2)
clear()
status = 'ready'
blanks = list("_" * len(word_list))

#ask if they're ready to start the game.
while status == 'ready' or status == 'guessing':
    if status == 'ready':
        ready = input('Ready to start? [y/n]\nNOTE: No will exit the game ')

    if ready.lower() == 'y' or status == 'guessing':
        #this entire status system could probably be removed but oh well
        status = 'guessing'
        #checks if there are any blanks left, if not, that means P2 wins!
        complete = "_" in blanks
        clear()

        if complete == False:
            status = 'win'
            break
        else:
            print(f'Guessed Letters: {guessed_letters}')
            print(f'Word: {blanks}')
            print(f'Mistakes: {mistakes}/7')
            current_guess = input('Guess a letter: ')
            check_letter(current_guess)

        if mistakes == 3:
            status = 'lose'
            break

    elif ready.lower() == 'n':
        #if answer no, exit
        system('exit')
        print('Exiting')
        break
    else:
        #if anything else, reset
        print("ERROR: please enter either 'y' or 'n' ")


##KEEP THIS AT THE BOTTOM.
#checks if the game is a win or a loss
if status == 'win':
    clear()
    print('You Win!')
    print(f'Guesses: {guessed_letters}')
    print(f'The Word: {"".join(word_list)}')
    exit()
elif status == 'lose':
    clear()
    print('Game Over')
    print(f'Guesses: {guessed_letters}')
    print(f'The Word: {"".join(word_list)}')
    exit()