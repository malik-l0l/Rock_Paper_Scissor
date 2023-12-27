"""
rock crushes scissors.
paper wraps rock.
scissors cut the paper.
"""
import random


def main():
    while True:
        choices = ["rock", "paper", "scissors"]

        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input('Rock, paper or scissors? :').lower()

        print('Computer : ', computer)
        print('Player   : ', player)

        if player == computer:
            print('Its a Tie')

        elif player == "rock":
            if computer == "paper":
                print("You lose")
            elif computer == "scissors":
                print('You win')

        elif player == "paper":
            if computer == "scissors":
                print("You lose")
            elif computer == "rock":
                print('you win')

        elif player == "scissors":
            if computer == "paper":
                print("You lose")
            elif computer == "rock":
                print('you win')

        play_again = input('wanna play again? (y/n):').lower()

        if play_again != 'y':
            break

    print('wow, it was a good game!')


if __name__ == '__main__':
    main()
