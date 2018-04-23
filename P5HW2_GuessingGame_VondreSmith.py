#User plays a game with input that randomizes an integer for the user to find.
#4.22.18
#CTI-110 P5HW2 - Random Number Guessing Game
#Vondre Smith
#

def main():
    print("This is a game...")
    play_game()

def play_game():
    import random
    n = random.randint(1,99)
    guess = int(input("Enter an interger from 1 to 99: "))
    while n!= guess:
        if guess<n:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess>n:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
            

main()
