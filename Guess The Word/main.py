import random

def guess_word(word, guesses):
    result = ""
    for letter in word:
        if letter in guesses:
            result += letter
        else:
            result += "-"
    return result

def main():
    with open("Guess The Word\word_list.txt", "r") as file:
        word_list = file.read().splitlines()
        
    word = random.choice(word_list)
    guesses = []
    chances = 7
    
    print("Welcome to the Word Puzzle Game!")
    print("Guess the word that consists of {} letters.".format(len(word)))
    print("You have {} chances.".format(chances))
    
    while chances > 0:
        guess = input("Enter your guess letter: ").lower()
        
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        
        if guess in guesses:
            print("You have already guessed this letter before.")
            continue
        
        guesses.append(guess)
        
        guess_result = guess_word(word, guesses)
        print(guess_result)
        
        if guess_result == word:
            print("Congratulations! You have successfully guessed the word.")
            break
        
        if guess not in word:
            chances -= 1
            if chances == 0:
                pass
            else:
                print("Your guess is incorrect. You have {} chances left.".format(chances))
        
        if chances == 0:
            print("Sorry, you have run out of chances. The correct word is", word)
            
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
