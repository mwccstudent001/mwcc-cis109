import random

wordlist = [
    "hangman",
    "llama",
    "python"
]

# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

word = wordlist[random.randint(0, len(wordlist) - 1)]

bad_guess = []

board = []
for word_len in word:
    board.append('_')

# word_coords = enumerate(word:[], start:0)

max_wrong = 6

# Ascii art
ascii1 = '''+---+
|
|
|
|    
======='''

ascii2 = '''+---+
|   |
|
|
|   
======='''

ascii3 = '''+---+
|   |
|   0
|
|    
======='''

ascii4 = '''+---+
|   |
|   0
|   |
|   
======='''

ascii5 = '''+---+
|   |
|   0
|  /|\ 
|
======='''

ascii6 = '''+---+
|   |
|   0
|  /|\ 
|  / \ 
======='''

ascii_art = [ascii1, ascii2, ascii3, ascii4, ascii5, ascii6]


print('Welcome to Hangman!')
while board != list(word) and len(bad_guess) < max_wrong:
    print(f'Board: {board}')
    if len(bad_guess) > 0:
        print(ascii_art[len(bad_guess) - 1])
    print(f'Wrong guesses: {bad_guess}\n')
    guess = input('Guess a letter:')
    if len(guess) > 1:
        print('Please enter only one letter')
        input('Press [Enter] to continue\n')
        continue
    elif guess in bad_guess or guess in board:
        print('You already guessed that')
        input('Press [Enter] to continue\n')
        continue
    elif guess in word:
        for idx,letter in enumerate(word, start=0):
            if letter == guess:
                board[idx] = word[idx]
        print('You got it')
        input('Press [Enter] to continue\n')
    else:
        bad_guess.append(guess)
        print('Wrong')
        input('Press [Enter] to continue\n')
if len(bad_guess) >= max_wrong:
    print(f'Board: {board}')
    print(ascii6)
    print(f'Wrong guesses: {bad_guess}\n')
    print(f'You lost! The word was "{word}".')
if board == list(word):
    print(f'You win! The word was "{word}".')
    