import random
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """)
l=["sayali","sahil","banana","axioms","sorry","pooja","vaishali","rutuja","shravan"]
stages = ['''
---------------------------------
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

randomword=random.choice(l)
display=[]

n=len(randomword)
for i in range(n):
    display.append("_")
    end_game=False
    lives=len(stages)-1
while not end_game:
    choosen_word=input("Guess letter:").lower()
    for i in range(len(randomword)):
        if randomword[i]==choosen_word:
            display[i]=randomword[i]

    if choosen_word not in randomword:
      lives=lives-1
      print("You entered wrong word,you loss live")
      if lives==0:
        end_game=True
        print("Sorry!!!! You loss game")

    print(stages[lives])
   
       
    print(''.join(display))
    if "_" not in display:
        end_game=True
        print("You win")
    
