### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secretWord = actual
   
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secretWord):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secretWord[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        printColorfulLetter(letter, True, False)

        # ...so we'll print it out with a yellow background

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user
def getSixLetterInput():
  # Create input for user
  userGuess = ""
  
  while len(userGuess) != 6:
    userGuess = input("Enter a six letter word: ")
  print()
  return userGuess.lower()
    
# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# TO-DO: Write the logic of the game here!
print(r"""

WW      WW                    dd    PPPPPP  lll                 
WW      WW  oooo  rr rr       dd    PP   PP lll   aa aa yy   yy 
WW   W  WW oo  oo rrr  r  dddddd    PPPPPP  lll  aa aaa yy   yy 
 WW WWW WW oo  oo rr     dd   dd    PP      lll aa  aaa  yyyyyy 
  WW   WW   oooo  rr      dddddd    PP      lll  aaa aa      yy 
                                                         yyyyy 
""")
print()

# Print instructions 
print("Welcome to Word Play!! ")
print("=============")
print("You have five tries to get the word correct ")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length ")
print("If a letter is in the correct place, it will be green ")
print("If a lettter is in the word but NOT in the correct place, it will be yellow ")
print("If the letter is NOT in the word, it will be red ")
print()

# Create secret word
secretWord = "secret"

# create variable to hold user guess 
guess = ""

# Keep Track of Attempts 
countAttempts = 0

# Create a loop to keep track of attempts
while countAttempts <6 and guess != secretWord:
  
  guess = getSixLetterInput()
  print()
  printGuessAccuracy(guess , secretWord)
  countAttempts += 1

# Congratulate or tell user they lost or won
if guess == secretWord:
  print("You won!!")
else:
  print("You Lost!")

  