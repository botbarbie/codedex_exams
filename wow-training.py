# Hi there, here's my first attempt at coding on my own
##There are some easter eggs for those of you that play wow

print('Welcome adventurer!')
print('    ')

# QUESTION NUMBER ONE
print('Today is the first day of your training, first pick a class:')
print('    ')
print('1. Mage')
print('2. Druid')
print('3. Paladin')
print('4. Warlock')
print('    ')

Q1 = int(input('Enter your answer(1-4):'))
print('    ')

if Q1 == 1:
  print(" _________________________")
  print("|                         |")
  print("|          NICE           |")
  print("|_________________________|")
  print("    ")
elif Q1 == 2:
  print(" _________________________")
  print("|                         |")
  print("|        GOOD CHOICE      |")
  print("|_________________________|")
  print("    ")
elif Q1 == 3:
  print(" _________________________")
  print("|                         |")
  print("|           MEH.          |")
  print("|_________________________|")
  print("    ")
elif Q1 == 4:
  print(" _________________________")
  print("|                         |")
  print("|        GOOD ENOUGH      |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|         NICE TRY        |")
  print("|_________________________|")
  print("    ")

# QUESTION NUMBER TWO
print('Now pick your weapon:')
print('    ')
print('1. Bow')
print('2. Staff')
print('3. Hammer')
print('4. Sword')
print('    ')
Q2 = int(input('Enter your answer(1-4):'))
print('    ')

if Q1 == 2 and Q2 == 2:
  print(" _________________________")
  print("|                         |")
  print("|          NICE           |")
  print("|_________________________|")
  print("    ")
elif Q1 == 1 and Q2 == 2:
  print(" _________________________")
  print("|                         |")
  print("|          GOOD           |")
  print("|_________________________|")
  print("    ")
elif Q1 == 3 and Q2 == 3:
  print(" _________________________")
  print("|                         |")
  print("|        OK THOR          |")
  print("|_________________________|")
  print("    ")
elif Q1 == 4 and Q2 == 2:
  print(" _________________________")
  print("|                         |")
  print("|        GOOD CHOICE      |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|   WHAT THE HELL JOHNNY  |")
  print("|_________________________|")
  print("    ")

# QUESTION NUMBER 3
print('Where should we start our journey ?')
print('    ')
print('1. I want to stay home')
print('2. I want to go to the Elwynn Forest')
print('3. I want to pursue Arthas in the Icecrown Citadel')
print('    ')
Q3 = int(input('Enter your Asnwer(1-3):'))
print('    ')

if Q3 == 1:
  print(" _____________________________")
  print("|                             |")
  print("|  COME ON, YOU GO TO ELWYNN  |")
  print("|_____________________________|")
  print("    ")
elif Q3 == 2:
  print(" _________________________")
  print("|                         |")
  print("|         LETS GO         |")
  print("|_________________________|")
  print("    ")
elif Q3 == 3:
  print(" _________________________")
  print("|                         |")
  print("| CALM DOWN, GO TO ELWYNN |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("| YOU HAVE A PROBLEM MATE |")
  print("|_________________________|")
  print("    ")

# QUESTION NUMBER 4
import random

print('    ')
print('Oh no you encountered a terrified Kobold ! ')
Q4 = (input('Press ENTER for your next a action:'))
print('    ')

random_number = random.randint(1, 10)
if random_number == 1:
  print(" _________________________")
  print("|                         |")
  print("|      YOU RUN AWAY       |")
  print("|_________________________|")
  print("    ")
elif random_number == 2:
  print(" _________________________")
  print("|                         |")
  print("|        YOU ATTACK       |")
  print("|_________________________|")
  print("    ")
elif random_number == 3:
  print(" _________________________")
  print("|                         |")
  print("|   YOU LEAVE THEM ALONE  |")
  print("|_________________________|")
  print("    ")
elif random_number == 4:
  print(" _______________________________")
  print("|                               |")
  print("| TOO MUCH AURA TO GET ATTACKED |")
  print("|_______________________________|")
  print("    ")
elif random_number == 5:
  print(" _________________________")
  print("|                         |")
  print("|     YOU GET INJURED     |")
  print("|_________________________|")
  print("    ")
elif random_number == 6:
  print(" _________________________")
  print("|                         |")
  print("|    YOU DANCE WITH THEM  |")
  print("|_________________________|")
  print("    ")
elif random_number == 7:
  print(" _________________________")
  print("|                         |")
  print("|    YOU FLIRT WITH THEM  |")
  print("|_________________________|")
  print("    ")
  print("ps : you freak")
  print("    ")
elif random_number == 8:
  print(" _________________________")
  print("|                         |")
  print("|  YOU CALL YOUR FRIENDS  |")
  print("|_________________________|")
  print("    ")
elif random_number == 9:
  print(" _________________________")
  print("|                         |")
  print("|       YOU STUN THEM     |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|   YOU SHROUD YOURSELF   |")
  print("|_________________________|")
  print("    ")

# QUESTION NUMBER 5
print('Oof, now that we had our first glimpse of what is an adventure, what should we do ?')
print('    ')
print('1. Head to Stormwind')
print('2. I still want to pursue Arthas in the Icecrown Citadel')
print('3. Head to the tavern')
print('    ')
Q5 = int(input('Enter your answer 1-3):'))
print('    ')

if Q5 == 1:
  print(" _________________________")
  print("|                         |")
  print("|        HERE WE GO       |")
  print("|_________________________|")
  print("    ")
elif Q5 == 2:
  print(" _________________________")
  print("|                         |")
  print("|    NO! GO TO STORMWIND  |")
  print("|_________________________|")
  print("    ")
elif Q5 == 3:
  print(" _________________________")
  print("|                         |")
  print("|   AFTER TRAINING MAYBE  |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|  STOP DEFYING AUHTORITY |")
  print("|_________________________|")
  print("    ")

#QUESTION NUMBER 6
import random
print('What should we do next ?')
Q6 = input('Press ENTER to decide')
print('    ')
random_number = random.randint(1, 5)
if random_number == 1:
  print('    ')
  print('You go to the tavern, have a nice one mate')
  print('I think this journey touches to an end, see you tomorrow')
  print('    ')
elif random_number == 2:
  print('    ')
  print('You escape behind your trainers back to pursue Arthas')
  print('You cannot stop a hero I guess')
  print('    ')
elif random_number == 3:
  print('    ')
  print('You go home, enough action for today')
  print('I think this journey touches to an end, see you tomorrow')
  print('    ')
elif random_number == 4:
  print('    ')
  print('You head to Goldshire to have some fun time, and if you know what it means you are a freak')
  print('    ')
elif random_number == 5:
  print('    ')
  print('You thank your trainer and go train some more on the dummies')
  print('You cannot stop a hero I guess')
  print('    ')
else:
  print('    ')

print('    ')
print('    ')
print('////////////')
# QUESTION NUMBER 7
print('THE NEXT DAY')
print('After a good night full of fun and rest you go back to the training camp')
print('Your trainer is waiting for you as you are running late')
print('What is your excuse ?')
print('    ')
print('1. I had too much fun in Goldshire :3')
print('2. I was training on the dummies')
print('3. I went to pursue Arthas but fell into a cliff')
print('4. I did not wanna come')
print('    ')
Q7 = int(input('Enter your answer (1-4):'))

if Q7 == 1:
  print(" _________________________")
  print("|                         |")
  print("|           EW            |")
  print("|_________________________|")
  print("    ")
elif Q7 == 2:
  print(" _________________________")
  print("|                         |")
  print("|        GOOD GIRL        |")
  print("|_________________________|")
  print("    ")
elif Q7 == 3:
  print(" _________________________")
  print("|                         |")
  print("|           SAD           |")
  print("|_________________________|")
  print("    ")
elif Q7 == 4:
  print(" _________________________")
  print("|                         |")
  print("|          LEGIT          |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|        FFS STOP         |")
  print("|_________________________|")
  print("    ")

#QUESTION NUMBER 8

print('   ')
print('Since you have been training so hard you are granted with a new ability!')
print('yay')
if Q1 == 1:
  print(" _________________________")
  print("|                         |")
  print("|        PYROBLAST        |")
  print("|_________________________|")
  print("    ")
elif Q1 == 2:
  print(" _________________________")
  print("|                         |")
  print("|      FURY OF ELUNE      |")
  print("|_________________________|")
  print("    ")
elif Q1 == 3:
  print(" _________________________")
  print("|                         |")
  print("|     BLADE OF JUSTICE    |")
  print("|_________________________|")
  print("    ")
else:
  print(" _________________________")
  print("|                         |")
  print("|   UNSTABLE AFFLICTION   |")
  print("|_________________________|")
  print("    ")

#FINAL ROLL FOR QUESTION 9
print('   ')
import random
print('You are so impatient to try your new ability that you accidentally attack a random group of wild tigers')
Q9 = (input('Press ENTER to know your fate: '))
print('    ')
random_number = random.randint(1, 5)
if random_number == 1:
  print(" _________________________")
  print("|                         |")
  print("|         YOU DIED        |")
  print("|_________________________|")
  print("    ")
  print('Ouch')
elif random_number == 2:
  print(" _________________________")
  print("|                         |")
  print("|      YOU SURVIVED       |")
  print("|_________________________|")
  print("    ")
  print('yay')
elif random_number == 3:
  print(" _________________________")
  print("|                         |")
  print("|      YOU RAN AWAY       |")
  print("|_________________________|")
  print("    ")
elif random_number == 4:
  print(" _________________________________")
  print("|                                 |")
  print("|  YOU TRIPPED AND BECAME A FOOL  |")
  print("|_________________________________|")
  print("    ")
elif random_number == 5:
  print(" ________________________")
  print("|                        |")
  print("|    YOU SLAYED GURL     |")
  print("|________________________|")
  print("    ")
else:
  print('   ')
