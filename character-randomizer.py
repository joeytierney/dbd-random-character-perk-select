import random
import sys

def mainMenu():
  menuOption = True
  while menuOption is True:
    print('*** WELCOME, TO DEAD BY DAYLIGHT CHARACTER/PERK ROULETTE! ***')
    userChoice = input('\n- (S)urvivor\n- (K)iller\n- (E)xit\n>')
    userChoice = userChoice.upper()

    if userChoice == 'S':
      survivorMenu()
      menuOption = False
    elif userChoice == 'K':
      killerMenu()
      menuOption = False
    elif userChoice == 'E':
      print('Ending program....')
      print('**********')
      sys.exit()
    else:
      print('\nInvalid input! Use S or K\n')

def survivorMenu():
  survMenuOption = True

  while survMenuOption is True:
    print('\n*** SURVIVOR MENU ***')
    survMenuChoice = input('\n- (C)haracter\n- (P)erks\n- (B)ack\n> ')
    survMenuChoice = survMenuChoice.upper()

    if survMenuChoice == 'C':
      randomSurvivor()
      survMenuOption = False
    elif survMenuChoice == 'P':
      print('Random Perks')
      survMenuOption = False
    elif survMenuChoice == 'B':
      print()
      mainMenu()
      survMenuOption = False
    else:
      print('\nInvalid input! Use C or P\n')

def killerMenu():
  print('\n*** KILLER MENU ***')
  killerMenuChoice = input('\n(C)haracter or (P)erks?\n> ')
  killerMenuChoice = killerMenuChoice.upper()

  if killerMenuChoice == 'C':
    randomKiller()
  elif killerMenuChoice == 'P':
    print('Random Perks')

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
      print('Ending program....')
      print('**********')
      sys.exit()

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