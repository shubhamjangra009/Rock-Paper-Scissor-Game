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

#Write your code below this line 👇
list=[rock,paper,scissors]
import random
rndnum=random.randint(0,2)
print('Welcome to rock, papers, scissors game!')
print('type R for rock, P for papers, S for scissors to choose from')
i=input()
if i=='R':
    print(list[0])
elif i=='P':
    print(list[1])
else:
    print(list[2])

print('Computer choose')
print(list[rndnum])

if i=='R' and rndnum==1:
    print('You lost with computer')
elif i=='P' and rndnum==2:
    print('You lost with computer')
elif i=='S' and rndnum==0:
    print('You lost with computer')
elif i=='P' and rndnum==0:
    print('You won the game')
elif i=='S' and rndnum==1:
    print('You won the game')
elif i=='R' and rndnum==2:
    print('You won the game')
else:
    print('Game tied')
