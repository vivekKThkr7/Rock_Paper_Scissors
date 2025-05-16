# Rock Paper Scissors Game

import random

def rps():
    options = ['rock', paper' 'Scissors']
    user_score = comp_score = 0
    round = int(input("How many rounds? "))

    for i in range(rounds):
        user = input('rock, paper, or scissors? ').lower()
        comp = random.choice(options)
        print(f"Computer chose {comp}")
        if user == comp:
            print("TIEEE")

        elif(user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round.")
            comp_score += 1

    print(f"Final Score — You: {user_score}, Computer: {comp_score}")

if __name__ == '__main__':
    rps()

    