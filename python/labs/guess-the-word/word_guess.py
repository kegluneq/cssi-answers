from random import randint

# A function to determine if the letter guessed is a single legal character.
def is_valid_input(letter, letters_guessed):
    if len(letter) != 1:
        print('You must guess a single letter, not multiple.')
        return False
    if not letter.isalpha():
        print('You entered a character that\'s not in the alphabet')
        return False
    if letter in letters_guessed:
        print('You\'ve already guessed "%s"' % letter)
        return False
    return True

def compute_guessed_word(word, letters_guessed):
    # Go through every letter that has been guessed and use it to generate
    # the current_output visible to the user with _ where the letters
    # haven't been guessed.
    guess_progress = ''
    for letter in word:
        # Allow spaces and all guesses the users have made to show in the
        # progress. not letter.isalpha() means that all punctuation in the
        # phrase is shown by default.
        if not letter.isalpha() or letter in letters_guessed:
            guess_progress += letter
        else:
            guess_progress += '_'
    return guess_progress

def play_hangman(word, max_guesses):
    # Sets are like lists, but without repeats. If you add 2 of the same thing
    # to a set, only 1 copy will remain in the set.
    letters_guessed = set()
    # guessed_word will always hold the most recent version of the word the user
    # knows about based on what letters they've guessed with unguessed letters
    # represented with _.
    guessed_word = ''
    # Keep track of incorrect_guesses so that when they guess too many bad
    # letters they lose.
    incorrect_guesses = 0
    # Print out the instructions!
    print("")
    print("Welcome to the game of Hangman!")
    print("Enter a single letter at a time to guess. You get only %s "
          "wrong guesses so choose wisely." % max_guesses)
    while guessed_word != word and incorrect_guesses < max_guesses:
        guessed_word = compute_guessed_word(word, letters_guessed)
        print('Current Progress: %s' % guessed_word)
        print('Guesses: %s' % ' '.join(letters_guessed))
        if guessed_word != word:
            # Ask the user to enter a letter and validate it.
            valid_input = False
            while not valid_input:
                last_letter_guessed = raw_input('Guess a letter: ').lower()
                valid_input = is_valid_input(last_letter_guessed,
                                             letters_guessed)
            # If they guess a letter not in the word, penalize them.
            if last_letter_guessed not in word:
                incorrect_guesses += 1
                print('You\'ve guessed the letter "%s" that\'s not in the word.'
                      ' You have %s guesses remaining' %
                      (last_letter_guessed, max_guesses-incorrect_guesses))

            # Once the user guesses a valid letter, keep track of it.
            letters_guessed.add(last_letter_guessed)
    if guessed_word == word:
        print('Congratulations!')
    else:
        print('Game over! You guessed too many (%s) times' % incorrect_guesses)

    print('The word was "%s".\n' % word)


hangman_phrases = [
    'aardvark',
    'vaccuum cleaner',
    'longitude and latitude',
    'android',
    'pembroke welsh corgi',
    'cavalier king charles spaniel',
    'the princess bride',
    'inside out',
    'upside down',
    'python',
    'javascript',
    'google chrome',
    'apple iphone',
    'how to train a dragon',
    'object oriented programming',
    'oklahoma',
    'monacle',
    'hangman',
    'boggle',
    'chocolate chip cookie',
    'chai tea',
    'vanilla ice cream',
    'alpaca',
]
# Play the game!
while raw_input('Would you like to play hangman? (y/n) ').lower()[:1] == 'y':
    # Get a random word from the list and then force the hidden word to be
    # lower cased.
    hidden_word = hangman_phrases[randint(0, len(hangman_phrases)-1)].lower()
    play_hangman(hidden_word, 5)
