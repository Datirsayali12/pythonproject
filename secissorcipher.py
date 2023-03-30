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

p = int(input("what do you want to choose 0.rock 1.paper 2.scissors!"))
print("you choose")

if p == 0:
    print(rock)
if p == 1:
    print(paper)
if p == 2:
    print(scissors)

print("computer choose")
r = random.randint(0, 2)
if r == 0:
    print(rock)
if r == 1:
    print(paper)
if r == 2:
    print(scissors)

if p == 0 and r == 2:
    print("you win!!!!")
elif r == 0 and p == 2:
    print("you loss")
if p == 1 and r == 0:
    print("you win!!!!")
elif p == 0 and r == 1:
    print("you loss")
if p == 2 and r == 1:
    print("you win!!!!!")
elif p == 1 and r == 2:
    print("you loss")
if r == p:
    print("oops Its draw")
