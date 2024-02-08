rock = ''' ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("  Welcome to the Rock, Paper, Scissors game!    ")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

print("\n\nComputer chose: \n")
chance = random.randint(0,2)


if chance == 0:
    print(rock)
elif chance == 1:
    print(paper)
else:
    print(scissors)

if((choice == 0 and chance == 1) or (choice == 1 and chance == 2) or (choice == 2 and chance == 0)):
  print("You Lose!")
elif((choice == 0 and chance == 2) or (choice == 1 and chance == 0) or (choice == 2 and chance == 1)):
  print("You Win!")
elif choice == chance :
    print("It's a tie!")
else:
   print("Please enter valid number")
 

# if(choice == 0 and chance == 1):
#     print("You Lose!")
# elif(choice == 1 and chance == 2):
#    print("You Lose!")
# elif(choice == 2 and chance == 0):
#    print("You Lose!")
# elif(choice == 0 and chance == 2):
#    print("You Win!")
# elif(choice == 1 and chance == 0):
#    print("You Win!")
# elif(choice == 2 and chance == 1):
#    print("You win!")
# elif(choice == 0 and chance == 0):
#    print("It's a tie!")
# elif(choice == 1 and chance == 1):
#    print("It's a tie!")
# elif(choice == 1 and chance == 1):
#    print("It's a tie!")   
