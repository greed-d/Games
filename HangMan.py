import random
HANGMAN = ['''

  +---+
  |   |
      |
      |
      |
      |
  ========''', '''


  +---+
  |   |
  O   |
      |
      |
      |
   =======''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
   =======''', '''

  +----+
  |    |
  O    |
  |\   |
       |
       |
   =======''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
   =======''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
   =======''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
   =======''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_random_words(word_list):
    # Function to get random word, we need randint
    word_index = random.randint(0, len(word_list)-1)
    return word_list[word_index]


def dispaly_board(HANGMAN, missed_letters, correct_letters, secret_word):

    # To display the hangman with each missed letters
    print(HANGMAN[len(missed_letters)])
    print()

    # To display missed letters on screen and connect missed letters
    print('Missed Letters : ', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    # To display blanks for the game:
    blank = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blank = blank[:i] + secret_word[i] + blank[i+1:]

    for letter in blank:
        print(letter, end=' ')
    print()


# To make sure user will enter 'a' LETTER not a string or any other data types
def get_guess(already_guessed):
    while True:
        guess = input("Enter a letter : ")
        guess = guess.lower()

        if len(guess) != 1:
            print("Enter a single letter")

        elif guess in already_guessed:
            print("You have already guessed that letter")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER")
        else:
            return guess

# To ask user if they want to play again or not


def play_again():
    print("Do you want to play again? : ")
    return input().lower().startswith('y')


# The real fun begins here: :)
print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_words(words)
game_is_done = False


while True:
    dispaly_board(HANGMAN, missed_letters, correct_letters, secret_word)

    # To get a letter user enters
    guess = get_guess(missed_letters + correct_letters)

    # This loop is for wheather the user entered correct letter or not
    if guess in secret_word:

        # Loop for correct letter
        correct_letters = correct_letters + guess

        found_all_letters = True

        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print("Good job! You found the secret word", secret_word)
            game_is_done = True

    else:
        # Loop for missed letter
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN)-1:
            dispaly_board(HANGMAN, missed_letters,
                          secret_word, correct_letters)
            print("You lost! \nYou are out of chances after " + str(len(missed_letters)) + " guesses and made " +
                  str(len(correct_letters)) + " correct guess. The secret word is ", secret_word)
            game_is_done = True

    # This is to prompt user if they want to play again or not:
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_words(words)

        else:
            break
