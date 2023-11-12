# Hangman Game

![Hangman](https://i.ibb.co/wWgR64Z/ss.png)

**Hangman Game** is a simple Python console-based game where players try to guess a hidden word, letter by letter. Players have a limited number of lives, and they must guess the word before running out of lives. It's a fun and interactive way to test your vocabulary and word-guessing skills.

## Getting Started

### Prerequisites

Before you can play the Hangman Game, you'll need to have Python installed on your computer. If you don't have Python, you can download it from the official [Python website](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/dev-diegov/hangman.git
    ```
2. Change to the project directory:
    ```bash
   cd The_hangman
    ```
3. Start the game by running:
    ```bash
   python hangman.py
    ```

### How to Play
1. The game will randomly select a word from its word list, and you'll see a series of underscores representing the letters in the word. For example: _ _ _ _ _ _.

2. Guess a letter by typing it and pressing Enter. For example:
    ```bash
    Enter a letter: a
    ```
If the letter is in the word, it will be revealed in the word display. If it's not, you'll lose a life.

3. Keep guessing letters until you either correctly guess the entire word or run out of lives (you have 6 lives in total).

4. If you guess the word before running out of lives, you win the game! If you run out of lives, you lose.

### Customization
You can customize the Hangman Game by modifying the words.txt file, which contains the list of words that the game will choose from.  You can add, remove, or modify words in this file to change the words used in the game.

### Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. We welcome any improvements or bug fixes to make the game even better.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Special thanks to Dev-DiegoV for creating this Hangman Game.

Happy playing!