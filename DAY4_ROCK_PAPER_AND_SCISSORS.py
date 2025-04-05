rock ='''
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
choice = int(input("enter your choice,0 for rock, 1 for scissors and 2 for paper."))
list1 = [rock,paper,scissors]
import random
comchoice = random.choice(list1)
if choice == 0:
    print("your choice:",rock)
    print("computers choice:",comchoice)
    if choice == 0 and comchoice == rock:
        print("its a draw")
    elif choice == 0 and comchoice == paper:
        print("you lost")
    else:
        print("you win")
elif choice == 1:
    print("your choice:",paper)
    print("computers choice:",comchoice)
    if choice == 1 and comchoice == paper:
        print("its a draw")
    elif choice == 1 and comchoice == scissors:
        print("you lost")
    else:
        print("you win")
elif choice == 2:
    print("yours choice:",scissors)
    print("computers choice:",comchoice)
    if choice == 2 and comchoice == scissors:
        print("its a draw")
    elif choice == 2 and comchoice == rock:
        print("you lost")
    else:
        print("you win")
else:
    print("wrong choice")
