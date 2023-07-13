import random
from word import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    Complet_word = "_" *len(word)
    guessed =False
    guessed_letter =[]
    gussed_word =[]
    TRIES =6
    print("Let's play hangman")
    print(display_hangman(TRIES))
    print(Complet_word)
    print("\n")
    while not guessed and TRIES > 0:
        guess =input("Please guess a letter or word : ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("you already guessed the letter", guess)
            elif guess not in word:
                print(guess,"is not in the word :")
                TRIES -= 1
                guessed_letter.append(guess)
            else:
                print("you guessed right")
                guessed_letter.append(guess)
                word_as_list =list(Complet_word)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                Complet_word = "".join(word_as_list)
                if "_" not in Complet_word:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in gussed_word:
                print("you already guessed the word")
            elif guess != word:
                TRIES -= 1
                gussed_word.append(guess)
            else:
                guessed=True
                Complet_word = Complet_word

        else:
            print("Not a valid guess")
        print(display_hangman(TRIES))
        print(Complet_word)
        print("\n")

    if guessed:
        print("congrats that's the right word")
    else:
        print("Sorry you ran out of tries the word was " + word + " maybe next time")

def display_hangman(TRIES):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[TRIES]

def main():
    word = get_word()
    play(word)
    while input('Play again? (Y/N)').upper() == "Y":
        word=get_word()
        play(word)

if __name__ == "__main__":
    main()