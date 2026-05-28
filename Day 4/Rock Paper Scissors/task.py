import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = input("Type 0 for ROCK, 1 for PAPER, 2 FOR SCISSORS:")
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice == 0: and computer_choice == 2:
if computer_choice>user_choice:
    print(f)
#if user_choice == 0:
    #print(rock)


