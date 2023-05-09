import random

print("Welcome to hangman")
print("----------------------------------------------")

wordDictionary = ["rose","love","friends","water","ruby","green","sunset","sweet","cupcakes"]

# choosing a random word

randomWord = random.choice(wordDictionary)

for x in randomWord:
    print("_", end="")

# Defining a funtcion that will hold all the hangman designs
# The design shows when the guess is wwrong
def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("     |")
        print("     |")
        print("     |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O    |")
        print("     |")
        print("     |")
        print("    ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O    |")
        print("|    |")
        print("     |")
        print("    ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \ |")
        print("    ===")

# Defining a function that will print oou the word on each iteration of the loop

def printWord(guessedLetters):
   counter=0     #This is an iterater
   rightLetters=0   #The amount of letters they have gotten right
   for char in randomWord:
       if (char in guessedLetters):
           print(randomWord[counter], end=" ")
           rightLetters+=1
       else: #*
           print(" ", end=" ")
       counter+=1
   return rightLetters
       
def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
# Intiliazing the number of times the user has guessed wrong
amount_of_times_wrong = 0
# Intializing guess index which will keep trck where the player is in the whole array i.e _ _ d _ _
current_guess_index = 0
# Array of the letters alreaady guessed
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
      print(letter, end=" ")
    # Prompt user for input
    letterGuessed = input("\nGuess a letter: ")
    # To determine if the user is right

    if letterGuessed in randomWord:
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    # When user was wrong
    else:
        print_hangman(amount_of_times_wrong)
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
   

print("Game is over! Thank you for playing.")

print("The word was:", randomWord)
    
    
    
  