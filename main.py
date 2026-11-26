import random
from ai import call_gpt
from words import get_random_word
from random import randint
from animal import get_random_animal

GAMES = {"1": "Guess my Number", "2": "Wordle", "3": "Guess my Animal"}
NUMBER_ATTEMPTS = 6
POINTS = {"1": 12, "2": 10, "3": 8, "4": 6, "5": 4, "6": 2}


def instruction(select):
    if select == "1":
        print(f"INSTRUCTIONS:\n(1) You have {NUMBER_ATTEMPTS} attempts to guess the right number.")
        print(f"(2) Your total score will be based on the total number of attempts as follows:")
        for key in POINTS:
            print(f"{key} {POINTS[key]}")
        print("Are you ready? Let's start!")
    if select == "2":
        print(f"INSTRUCTIONS:\n(1) You have {NUMBER_ATTEMPTS} attempts to guess the right word.")
        print("(2) Enter only a five-letter word.")
        print("(3) The letter in the [] indicates that the letter is in the right position. The () indicates that the letter is in a wrong position. Else, the letter does not appear in the word.")
        print(f"(4) Your total score will be based on the total number of attempts as follows:")
        for key in POINTS:
            print(f"{key} {POINTS[key]}")
        print("Are you ready? Let's start")
    if select == "3":
        print(f"INSTRUCTIONS:\n(1) You have {NUMBER_ATTEMPTS} attempts to guess the right animal.")
        print(f"(2) Your total score will be based on the total number of attempts as follows:")
        for key in POINTS:
            print(f"{key} {POINTS[key]}")
        print("Are you ready? Let's start!")

def main():
    print("Welcome to World of Games!")
    for game in GAMES:
        print(f"{game} {GAMES[game]}")
    
    select = input("Enter the game number you want to play: ")
    while select not in GAMES:
        print("Enter only 1, 2 or 3")
        select = input("Enter the game number you want to play: ")

    # "Guess my number"
    if select == "1":
        print(f"Welcome to {GAMES[select]}!")
        instruction("1")
        secret_number = random.randint(1,100)
        
        for attempt in range(NUMBER_ATTEMPTS):
            guess = int(input("I am thinking of a number from 1 to 100. Make a guess: "))
            while guess not in range(1,101):
                print("Enter only a number between 1 and 100.")      
                guess = int(input("I am thinking of a number from 1 to 100. Make a guess: "))
            
            if guess == secret_number:
                print(f"Correct! You guessed it in {attempt + 1} tries!")
                print(f"Your score is {POINTS[str(attempt + 1)]}")
                break     # or return to exit the for loop
            elif guess > secret_number:
                print("Nope, the guess is too high. Try again!")
            else:
                print("Nope, the guess is too low. Try again!")
        else:
            print(f"Better luck next time! The correct number was '{secret_number}'.")

    # "Wordle"
    elif select == "2":
        print(f"Welcome to {GAMES[select]}!")
        instruction("2")
        SECRET = get_random_word()

        for attempt in range(NUMBER_ATTEMPTS):
            guess = input("Enter your guess: ")
            guess = guess.lower()
            while len(guess) != 5:
                print("Please enter a 5-letter word.")
                guess = input("Enter your guess: ")
                guess = guess.lower()

            result = []
            remaining_letters = list(SECRET)

            for i in range(len(SECRET)):
                if SECRET[i] == guess[i]:
                    result.append("G")    # Adds an element to the list
                    remaining_letters.remove(guess[i])
                else:
                    result.append("B")
    
            for j in range(len(result)):
                if result[j] == "B":
                    if guess[j] in remaining_letters:
                        result[j] = f"({guess[j]})"
                        remaining_letters.remove(guess[j])
                    else: result[j] = guess[j]
                else: 
                    result[j] = f"[{guess[j]}]"

            print("Result:", " ".join(result))     # Combine list elements into a string with space in between
            attempt + 1
        
            if guess == SECRET:
                print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
                print(f"Your score is {POINTS[str(attempt + 1)]}.")
                return

        print(f"Better luck next time! The correct word was '{SECRET}'.")

    else:
        print("Welcome to Guess my Animal!")
        instruction("3")
        animal = get_random_animal ()
        mode = input("Easy mode? Type yes or no: ").strip().lower()     #.strip() remove the space user accidentally adds
        while mode not in ["yes", 'no']:
            print("Type only yes or no.")
            mode = input("Easy mode? Type yes or no: ").strip().lower()
        print("I am thinking of an animal. \nCan you guess what it is?")

        for attempt in range (NUMBER_ATTEMPTS):
            user_input = input ("Ask me a yes or no question: ")
            if mode == "yes":
                prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {user_input}. Please respond with exactly Yes, No, with a small clue, or Correct if they guess the animal exactly. Do not say anything else. Do not reveal the answer"
                gpt_response = call_gpt(prompt)
                if gpt_response != "Correct":
                    print(gpt_response)
                else:
                    print(f"Correct! You guess in {attempt + 1} tries.")
                    print(f"Your score is {POINTS[str(attempt + 1)]}.")
                    break
            else:
                prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {user_input}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else. Do not reveal the answer"
                gpt_response = call_gpt(prompt)
                if gpt_response != "Correct":
                    print(gpt_response)
                else:
                    print(f"Correct! You guess in {attempt + 1} tries.")
                    print(f"Your score is {POINTS[str(attempt + 1)]}.")
                    break
        else:
            print(f"Better luck next time! The correct animal is {animal}.")
    
if __name__ == "__main__":
    main()