
#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"


import random
dice_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
      
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●  ●  ● │",
       "│         │",
       "│ ●  ●  ● │",
       "└─────────┘"),
   
      
  }

dice=[]
total=0
number_input=int(input("Enter the value of dice: "))
for die in range(number_input):
    dice.append(random.randint(1,6))
    

for die in range(number_input):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total+=die

print(f"The total of dice is: {total}")    