import random
import sys

def mainMenu():
  menuOption = True
  while menuOption is True:
    print('\n*** WELCOME, TO DEAD BY DAYLIGHT CHARACTER/PERK ROULETTE! ***')
    userChoice = input('\n1. (S)urvivor\n2. (K)iller\n3. (E)xit\n>')
    userChoice = userChoice.upper()

    if userChoice == 'S':
      survivorMenu()
      menuOption = False
    elif userChoice == 'K':
      killerMenu()
      menuOption = False
    elif userChoice == 'E':
      print('\nEnding program....')
      print('**********')
      sys.exit()
    else:
      print('\nInvalid input! Use S, K or E!\n')

def survivorMenu():
  survMenuOption = True

  while survMenuOption is True:
    print('\n*** SURVIVOR MENU ***')
    survMenuChoice = input('\n1. Survivor\n2. Perks\n3. Survivor List\n4. Perk List\n5. Back\n> ')
    survMenuChoice = survMenuChoice.upper()

    if survMenuChoice == '1':
      randomSurvivor()
      survMenuOption = False
    elif survMenuChoice == '2':
      print('Random Perks')
      survMenuOption = False
    elif survMenuChoice == '3':
      print(survivorNames)
    elif survMenuChoice == '4':
      print('Perk List')
    elif survMenuChoice == '5':
      mainMenu()
      survMenuOption = False
    else:
      print('\nInvalid input! Please enter a number between 1 - 5\n')

def killerMenu():
  killerMenuOption = True

  while killerMenuOption is True:
    print('\n*** KILLER MENU ***')
    killerMenuChoice = input('\n1. Killer\n2. Perks\n3. Killer List\n4. Perk List\n5. Back\n> ')
    #killerMenuChoice = killerMenuChoice.upper()

    if killerMenuChoice == '1':
      randomKiller()
      killerMenuOption = False
    elif killerMenuChoice == '2':
      print('Random Perks')
      killerMenuOption = False
    elif killerMenuChoice == '3':
      print(killerNames)
    elif killerMenuChoice == '4':
      print('Perk List')
    elif killerMenuChoice == '5':
      mainMenu()
      killerMenuOption = False
    else:
      print('\nInvalid input! Please enter a number between 1 - 5\n')

def randomSurvivor():
  randomSurv = True
  # Declare a variable as a random choice
  random_array_item = random.choice(survivorNames)

  # Print the random choice
  print('\n***** RANDOM SURVIVOR *****')
  print('')
  print('      ' + random_array_item)

  while randomSurv is True:
    goAgain = input('\nWould you like to go again? (Y/N)\n> ')
    goAgain = goAgain.upper()

    if goAgain == 'Y':
      # Declare a variable as a random choice
      random_array_item = random.choice(survivorNames)

      # Print the random choice
      print('\n***** RANDOM SURVIVOR *****')
      print('')
      print('      ' + random_array_item)

    elif goAgain == 'N':
      survivorMenu()

    else:
      print('\nInvalid input! Please enter Y/N')

def randomKiller():
  randomKilr = True
  # Declare a variable as a random choice
  random_array_item = random.choice(killerNames)

  # Print the random choice
  print('\n***** RANDOM KILLER *****')
  print('')
  print('      ' + random_array_item)

  while randomKilr is True:
    goAgain = input('\nWould you like to go again? (Y/N)\n> ')
    goAgain = goAgain.upper()

    if goAgain == 'Y':
      # Declare a variable as a random choice
      random_array_item = random.choice(killerNames)

      # Print the random choice
      print('\n***** RANDOM KILLER *****')
      print('')
      print('      ' + random_array_item)

    elif goAgain == 'N':
      print('Ending program....')
      print('**********')
      sys.exit()

    else:
      print('\nInvalid input! Please enter Y/N')

survivorNames = ['Dwight Fairfield',
  'Meg Thomas',
  'Claudette Morel',
  'Jake Park',
  'Nea Karlsson',
  'William "Bill" Overbeck',
  'David King',
  'Laurie Strode',
  'Ace Visconti',
  'Feng Min',
  'Quentin Smith',
  'Detective Tapp',
  'Kate Denson',
  'Adam Francis',
  'Jeff Johansen',
  'Jane Romero',
  'Ashley J. Williams',
  'Nancy Wheeler',
  'Steve Harrington',
  'Jonathan Byers',
  'Yui Kimura',
  'Zarina Kassir',
  'Cheryl Mason',
  'Lisa Garland',
  'Cybil Bennett',
  'James Sunderland',
  'Felix Richter',
  'Élodie Rakoto',
  'Yun-Jin Lee',
  'Jill Valentine',
  'Claire Redfield',
  'Leon S. Kennedy',
  'Chris Redfield',
  'Mikaela Reid'
]

killerNames = ['The Trapper',
  'The Wraith',
  'The Hillbilly',
  'The Nurse',
  'The Huntress',
  'The Mordeo',
  'The Shape',
  'The Hag',
  'The Doctor',
  'The Look-See',
  'The Cannibal',
  'The Nightmare',
  'The Pig',
  'The Clown',
  'The Spirit',
  'The Legion',
  'The Plague',
  'The Ghost Face',
  'The Demogorgon',
  'The Oni',
  'The Deathslinger',
  'The Executioner',
  'The Blight',
  'The Twins',
  'The Trickster',
  'The Nemesis',
  'The Cenobite',
  'The Chatterer'
]

mainMenu()
killerMenu()
survivorMenu()
randomSurvivor()
randomKiller()

randomSurv = False
randomKilr = False