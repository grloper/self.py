# Hangman Game

This is a classic Hangman game written in Python. You guess letters to reveal a secret word chosen based on difficulty.

Features:

    Difficulty Levels: Choose from Easy, Medium, or Hard difficulties with words tailored to each level. (Words are stored in a separate file words.txt)
    Visual Hangman: See a visual representation of the hangman as you make incorrect guesses.
    Clear Gameplay: The game guides you through each step, displaying the hidden word with revealed letters and unguessed letters replaced by underscores.

How to Play:

    Run the Game:

        Save the files (source.py and words.txt) in the same directory.

        Open a terminal or command prompt and navigate to the directory containing the files.

Run the game using the following command:
         
         
        Bash >> python source.py


Choose Difficulty:

        The game will prompt you to enter the file path for words.txt. Ensure the path is correct.
        Select a difficulty level (1: Easy, 2: Medium, 3: Hard).

    Guessing Letters:
        The game will display the hidden word with underscores and the hangman image.
        Take turns guessing letters. Enter a single lowercase letter at a time.
        If you guess a correct letter, it will be revealed in the hidden word.
        If you guess an incorrect letter, the number of tries remaining will decrease, and the hangman image will update.

    Winning or Losing:
        The game continues until you either:
            Guess all the letters in the word correctly (You Win!).
            Run out of tries (MAX_TRIES) (You Lose!).

Customizing Words:

    You can customize the words used in the game by editing the words.txt file.
    The file format uses the pipe symbol ("|") to separate difficulty levels and commas (",") to separate words within each level.
    For example:

hat,sun,dog,cat,car|flower,rainbow,butterfly,mountain,river|knowledge,philosophy,beautiful,comfortable,technology,communication

This file defines three difficulty levels: Easy, Medium, and Hard, with corresponding word lists.

Have Fun!

This Hangman game is a fun and challenging way to test your vocabulary and word guessing skills. Enjoy playing!


![image](https://github.com/grloper/self.py/assets/72247422/93a9e7b1-dca4-4ba4-a996-f06f8a0024f1)

