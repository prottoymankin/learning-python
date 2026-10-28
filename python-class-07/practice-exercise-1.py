# Mini Project - Guess Game

import random

def generate_lucky_number ():
  return random.randint(1, 50)

def play_game ():
  lucky_number = generate_lucky_number()

  while True:
    user_guess = int(input("Guess your lucky number between 1 to 50: "))

    if user_guess == lucky_number:
      print("Hurrah! you win the game")
      break

    if (user_guess > lucky_number):
      print("Too high.")
    else:
      print("Too low.")

def main ():
  while True:
    play_game()

    user_choice = input("Want to play again (y/n): ").lower()

    while user_choice not in ('y', 'n'):
      user_choice = input("Invalid choice. Please enter y or n: ").lower()

    if user_choice == 'n':
      print("Thank you for playing the game.")
      break

main()