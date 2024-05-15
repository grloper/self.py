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

def show_hidden_word(secret_word, old_letters_guessed):  # One-liner using list comprehension
    """
    Returns a string representing the hidden word, with letters revealed if they have been guessed correctly.

    Parameters:
        secret_word (str): The word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed.

    Returns:
        str: The hidden word with correctly guessed letters revealed and other letters replaced with underscores.
    """
    return " ".join([letter if letter in old_letters_guessed or letter == " " else "_" for letter in secret_word]).strip()

def check_win(secret_word, old_letters_guessed):
    """
    Check if all the letters in the secret_word have been guessed correctly.

    Args:
        secret_word (str): The word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed.

    Returns:
        bool: True if all the letters in the secret_word have been guessed correctly, False otherwise.
    """
    return all(letter.lower() in old_letters_guessed for letter in secret_word if letter != " ")  


    
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
def validate_file_path(prompt="Enter file path: "):
  """
  Prompts the user for a valid file path and returns it.

  Args:
      prompt (str, optional): The message to display when prompting the user.
          Defaults to "Enter file path: ".

  Returns:
      str: The valid file path entered by the user.
  """

  while True:
    path = input(prompt)
    if os.path.isfile(path):
      return path
    else:
      print("Invalid file path. Please enter a valid file path:")

def validate_difficulty(prompt="Choose difficulty level (1: Easy, 2: Medium, 3: Hard): "):
  """
  Prompts the user for a valid difficulty level and returns it.

  Args:
      prompt (str, optional): The message to display when prompting the user.
          Defaults to "Choose difficulty level (1: Easy, 2: Medium, 3: Hard): ".

  Returns:
      str: The valid difficulty level (1, 2, or 3) entered by the user.
  """

  valid_options = ["1", "2", "3"]
  while True:
    difficulty = str(input(prompt))
    if difficulty in valid_options:
      return difficulty
    else:
      print("Invalid difficulty level. Please choose 1, 2, or 3:")

def check_lose(num_of_tries, saved_word):
  """
  Checks if the player has lost in a Hangman game.

  This function takes the current number of tries and the hidden word as input,
  performs a loss check, and displays messages if the player has lost.

  Args:
      num_of_tries (int): The current number of tries the player has used.
      saved_word (str): The hidden word the player is trying to guess.

  Prints:
      Loss messages ("You lost!", "Hidden word:") and reveals the hidden word
      if the player has lost. Calls the `print_hangman` function to display the hangman state.

  Returns:
      None
  """

  if num_of_tries == MAX_TRIES: # if the player reached MAX_TRIES, we then know he has lost
    print_hangman(num_of_tries)  # print the current state
    print("You lost!") # L
    print("Hidden word:", saved_word)

    
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
    
    # Getting valid input from user
    path = validate_file_path()
    difficulty = validate_difficulty()
        
    SAVED_WORD = choose_word(path, int(difficulty)) # Call choose_word to roll a random word from the difficulty level
    print_welcome_screen() # Clear the screen 
    
    # Main game loop
    while num_of_tries < MAX_TRIES:
        print_hangman(num_of_tries) # Print current game state using the hashmap
        print(show_hidden_word(SAVED_WORD, old_letters_guessed)) # Call show_hidden_word to print the player progress
        
        letter_guessed = input("\nGuess a letter: ").lower() # Take input from user
        if not try_update_letter_guessed(letter_guessed, old_letters_guessed): # Call try_update_letter_guessed to check for valid input and handle edge cases
            continue # Go to the next loop and re-input
        
        if letter_guessed not in SAVED_WORD: # If letter_guessed is wrong increase the num_of_tries
            num_of_tries += 1
            
        if check_win(SAVED_WORD, old_letters_guessed): # Call check_win to see if the player has won
            print("\n",show_hidden_word(SAVED_WORD, old_letters_guessed)) # Call show_hidden_word to print the player progress
            print("You won!") # W
            break
    # End of main game loop
    check_lose(num_of_tries, SAVED_WORD)


if __name__ == "__main__":
    print_welcome_screen()
    main()
