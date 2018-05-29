#Hangman
#This is a word guessing game based on Hangman.
#The player guesses letters till they come up with the word.
#The word list consists of flower names.
#The player gets ten guesses.

print('Hangman')
print('The objective of the game is to guess the name of a flower.')
print('You get ten guesses. Each guess can be one letter, a full flower name \
or if you want to stop playing, the word "end".')

#flower is the word list. Can be changed or extended
flower = ['dahlia',
          'lilac',
          'marigold',
          'rose',
          'daisy',
          'lily',
          'daffodil']           

import random

def main():
    
    play = 'yes'
    while play == 'yes':
                
        letter=[] #define variable letter
        git_list=[] #List for testing git and GitHub
        badlist=[] # List of wrong guesses
        goodlist=[] # List of good guesses
        lchoice=[] # Chosed word in list format
        finish='no'
        picture=[] # This is the graphic shown to the player, it is a list

        #choice is a word selected randomly from the flower list.
        #This is the word to be guessed.
        choice = flower[random.randint(0,(len(flower))-1)] #This is a string
        # The maximum number for the random range is calculated from the number
        # of flowers in the list flower.
        
        lchoice += choice #This converts the string to a list
               
        for l in range(len(lchoice)+1): # Provide an underscore for every letter
            if l:
                picture += '_'
        
        attempt=0
        while attempt < 10:

            # Display of game status
            print('\nThe flower name is', (len(choice)), 'letters long.')

            if attempt == 1:
                print('You made 1 guess')
            else:
                print('You made', attempt, 'guesses.')

            if attempt != 0:
                
                if badlist == []:
                    print('You have no wrong letter guesses.')
                else:
                    print('These are your wrong guesses: ', badlist)

                if goodlist == []:
                    print('You have no correct guesses.\n')
                else:
                    print('These are the correct guesses in the correct location.\n')
                
            print(picture, '\n\n')

            # Guess and guess analysis section
            guess=input('What is your guess? Letter, flower name or "end"?  ')

            attempt = attempt + 1

            if len(guess)==1: # Determines whether guess is one letter long
                letter=guess  # If so then letter is the current guess

                for r in range(len(lchoice)):             
                    #Check every letter in the word to see if it matches the guess
                    if lchoice[r]==letter.lower():
                        print('\nThe letter', letter.lower(), 'is a correct guess\n')
                        picture[r]= letter.lower()

                if not letter.lower() in lchoice: # Handles incorrect letter guesses
                    badlist.append(letter.lower())
                    print('\nThe letter', letter.lower(),
                          'is not in the name of the flower\n')

                else:
                    goodlist.append(letter.lower())

                if not '_' in picture: # Ends game if all the flower letters entered
                    print('You guessed all the letters correctly!\n')
                    print('The name of the flower is', choice, '.')
                    print('Congratulation! You won!')
                    finish='yes'  ##Do I need this line?
                    break

            # This section handles the "end" response
            elif guess == 'end':
                break
                
            # This section handles a guess of whole flower name
            elif len(guess)==len(choice):
                if guess.lower()==choice:
                    print('Congratulation! You won!')
                    break
                else:
                    print(guess, 'is not the flower I am thinking of.')

            #This handles the situation of a guess that's not a single letter,
            # the word "end" or is a different length than the chosen flower
            else:
                print(guess, 'is the wrong length. Try again')

        # End of game when max number of guesses was reached
        if attempt > 9:
            print('The name of the flower was', choice,'.',\
                  'You did not guess it in ten tries.')
            
        # End of game for all other reasons
        else:
            print('\nThank you for playing.')
            
        # Option to play another game
        play = input('\nWould you like to play again? Yes or no?: ')
        play=play.lower()
                
main()

