import os
import random

MAX_TRIES = 6
#Store the images, based on index access
HANGMAN_PHOTOS = {
    0: "\nx-------x",
    1: "\nx-------x\n|\n|\n|\n|\n|",
    2: "\nx-------x\n|       |\n|       0\n|\n|\n|",
    3: "\nx-------x\n|       |\n|       0\n|       |\n|\n|",
    4: "\nx-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    5: "\nx-------x\n|       |\n|       0\n|      /|\\\n|      / \n|",
    6: "\nx-------x\n|       |\n|       0\n|      /|\\\n|      / \\"
}
#r is used to indicate that the string is a raw string
HANGMAN_GAME_LOGO = r"""
     __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.      _______      ___      .___  ___.  _______
    |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |     /  _____|    /   \     |   \/   | |   ____|
    |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__
    |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
    |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____
    |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|     \______| /__/     \__\ |__|  |__| |_______|"""

def print_hangman(num_of_tries): 
    """
    Prints the hangman image corresponding to the given number of tries.

    Parameters:
    num_of_tries (int): The number of tries made by the player.

    Returns:
    None
    """
    print(HANGMAN_PHOTOS[num_of_tries])

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Returns a string representing the hidden word, with letters revealed if they have been guessed correctly.

    Parameters:
    secret_word (str): The word to be guessed.
    old_letters_guessed (list): A list of letters that have been guessed.

    Returns:
    str: The hidden word with correctly guessed letters revealed and other letters replaced with underscores.
    """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed or letter == " ": # If the letter exist, unblur it, if it a space, show it also
            hidden_word += letter + " "
        else:
            hidden_word += "_ " # If the letter is not exist, blur it.
    return hidden_word.strip()   # Return the hidden word with correctly guessed letters revealed and other letters replaced with underscores

def check_win(secret_word, old_letters_guessed):
    """
    Check if all the letters in the secret_word have been guessed correctly.

    Args:
        secret_word (str): The word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed.

    Returns:
        bool: True if all the letters in the secret_word have been guessed correctly, False otherwise.
    """
    for letter in secret_word:
        if letter.lower() not in old_letters_guessed and letter != " ": # also check for spaces
            return False
    return True  # Return True if all the letters in the secret_word (excluding spaces) have been guessed correctly, otherwise return False
    
    
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Check if the input letter is a valid guess.

    Parameters:
    letter_guessed (str): The letter guessed by the player.
    old_letters_guessed (list): A list of letters previously guessed.

    Returns:
    bool: True if the input letter is a valid guess, False otherwise.
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() or letter_guessed == " " or letter_guessed.lower() in old_letters_guessed:
        return False # Return false, if the len is not 1, if it not an ABC letter, or if space has been entered or if the input already been used
    return True 

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the list of guessed letters with a new letter.

    Args:
        letter_guessed (str): The letter to be added to the list of guessed letters.
        old_letters_guessed (list): The list of previously guessed letters.

    Returns:
        bool: True if the letter was successfully added to the list, False otherwise.
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        old_letters_guessed = ' -> '.join(sorted(old_letters_guessed))
        print(old_letters_guessed)
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
    
def choose_word(file_path, difficulty):
  """
  Chooses a word from a file based on difficulty level.

  Args:
      file_path (str): The path to the file containing the words.
      difficulty (int): The difficulty level (1: easy, 2: normal, 3: hard).

  Returns:
      str: The chosen word.
  """
  with open(file_path, "r") as file:
  # Read the entire file content
      content = file.read()
  # Split the content by the pipe symbol to separate difficulty sections
  difficulty_sections = content.split("|")
  # Choose the appropriate difficulty section based on index
  chosen_difficulty_section = difficulty_sections[difficulty - 1]
  # Split the chosen section by comma to get individual words
  words = chosen_difficulty_section.split(",")
  # Choose a random word from the list
  word_index = random.randint(0, len(words) - 1)
  return words[word_index].lower()
     

def clear_screen():
    """
    Clears the terminal screen.
    
    Args:
        None
        
    Returns:
        None
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux and macOS
    else:
        _ = os.system('clear')

def print_welcome_screen():
    """
    Prints the welcome screen for the Hangman game.
    
    Args:
        None
        
    Returns:
        None
    """
    clear_screen()
    print("Welcome to the Hangman game!")
    print(HANGMAN_GAME_LOGO)
     
def main():
    """
    The main function of the Hangman game

    Args:
        None

    Returns:
        None
    """
    # Initialize the list of guessed letters and the number of tries
    old_letters_guessed = []
    num_of_tries = 0
    
    # Handle the input of the secret word and the difficulty level
    path = input("\nEnter file path: ")
    while not os.path.isfile(path):
        path = input("Invalid file path. Please enter a valid file path: ")
        
    difficulty = int(input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): "))
    while difficulty not in [1, 2, 3]:
        difficulty = int(input("Invalid difficulty level. Please choose 1, 2, or 3: "))
        
    SAVED_WORD = choose_word(path, difficulty)
    
    # Main game loop
    while num_of_tries < MAX_TRIES:
        print_hangman(num_of_tries)
        print(show_hidden_word(SAVED_WORD, old_letters_guessed))
        letter_guessed = input("\nGuess a letter: ").lower()
        if not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            continue
        if letter_guessed not in SAVED_WORD:
            num_of_tries += 1
        if check_win(SAVED_WORD, old_letters_guessed):
            print("\n",show_hidden_word(SAVED_WORD, old_letters_guessed))
            print("You won!")
            break
    # Check if the player has lost
    if num_of_tries == MAX_TRIES:
        print_hangman(num_of_tries)
        print("You lost!")
        print("Hidden word:", SAVED_WORD)


if __name__ == "__main__":
    print_welcome_screen()
    main()
