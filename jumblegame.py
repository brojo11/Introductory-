# Word Jumble
#
# The computer picks a random word and then "jumbles" it.
# The player has to guess the original word.

def main():

    import random

    # Sequence of words to choose from
    WORDS = ('python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone')

    # Pick one random word from the sequence
    word=random.choice(WORDS)

    # Create a variable to use late to see if the guess is correct
    correct=word

    #Create a jumbled version of the word
    jumble=''

    while word:
        position=random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position +1):]

    # Start the game
    print(
    '''
                    Welcome to Word Jumble!

             Unscramble the letters to make a word.
          (Press the Enter key at the prompt to quit.)
    '''
    )
    print('The jumble is:', jumble)
    guess = input('\nYour guess: ')
    while guess != correct and guess != '':
        print("Sorry that's not it")
        guess = input('Your guess: ')

    if guess==correct:
              print("That's it! You guessed it!\n")

    print('Thanks for playing.')

    input('\n\nPress enter to exit program.')
    

main() 
