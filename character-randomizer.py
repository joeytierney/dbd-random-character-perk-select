import random
import sys

def mainMenu():
  menuOption = True
  while menuOption is True:
    print('\n*** WELCOME, TO DEAD BY DAYLIGHT CHARACTER/PERK ROULETTE! ***')
    userChoice = input('\n1. Survivor\n2. Killer\n3. Exit\n> ')

    if userChoice == '1':
      survivorMenu()
      menuOption = False
    elif userChoice == '2':
      killerMenu()
      menuOption = False
    elif userChoice == '3':
      print('\nEnding program....')
      print('**********')
      sys.exit()
    else:
      print('\nInvalid input! Please enter a number between 1 - 3\n')

def survivorMenu():
  survMenuOption = True

  while survMenuOption is True:
    print('\n*** SURVIVOR MENU ***')
    survMenuChoice = input('\n1. Survivor\n2. Perks\n3. Survivor List\n4. Perk List\n5. Back\n> ')

    if survMenuChoice == '1':
      randomSurvivor()
      survMenuOption = False
    elif survMenuChoice == '2':
      randomPerkSurv()
      survMenuOption = False
    elif survMenuChoice == '3':
      print('')
      print(survivorNames)
    elif survMenuChoice == '4':
      print('')
      print(survPerks)
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

    if killerMenuChoice == '1':
      randomKiller()
      killerMenuOption = False
    elif killerMenuChoice == '2':
      randomPerkKiller()
      killerMenuOption = False
    elif killerMenuChoice == '3':
      print('')
      print(killerNames)
    elif killerMenuChoice == '4':
      print('')
      print(killerPerks)
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
      killerMenu()

    else:
      print('\nInvalid input! Please enter Y/N')

def randomPerkSurv():
  randomSurvPerk = True

  random.shuffle(survPerks)
  result = survPerks[:4]

  # Print the random choice
  print('\n***** RANDOM SURVIVOR PERKS *****')
  print('')
  print(result)

  while randomSurvPerk is True:
    goAgain = input('\nWould you like to go again? (Y/N)\n> ')
    goAgain = goAgain.upper()

    if goAgain == 'Y':
      random.shuffle(survPerks)
      result = survPerks[:4]

      # Print the random choice
      print('\n***** RANDOM SURVIVOR PERKS *****')
      print('')
      print(result)

    elif goAgain == 'N':
      survivorMenu()

    else:
      print('\nInvalid input! Please enter Y/N')

def randomPerkKiller():
  randomKillerPerk = True

  random.shuffle(killerPerks)
  result = killerPerks[:4]

  # Print the random choice
  print('\n***** RANDOM KILLER PERKS *****')
  print('')
  print(result)

  while randomKillerPerk is True:
    goAgain = input('\nWould you like to go again? (Y/N)\n> ')
    goAgain = goAgain.upper()

    if goAgain == 'Y':
      random.shuffle(killerPerks)
      result = killerPerks[:4]

      # Print the random choice
      print('\n***** RANDOM KILLER PERKS *****')
      print('')
      print(result)

    elif goAgain == 'N':
      killerMenu()

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
  '??lodie Rakoto',
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

survPerks = ['Ace in the Hole',
 'Adrenaline',
 'Aftercare',
 'Alert',
 'Any Means Necessary',
 'Appraisal',
 'Autodidact',
 'Balanced Landing',
 'Bite the Bullet',
 'Blast Mine',
 'Blood Pact',
 'Boil Over',
 'Bond',
 'Boon: Circle of Healing',
 'Boon: Shadow Step',
 'Borrowed Time',
 'Botany Knowledge',
 'Breakdown',
 'Breakout',
 'Buckle Up',
 'Built to Last',
 'Calm Spirit',
 'Clairvoyance',
 'Counterforce',
 'Dance With Me',
 'Dark Sense',
 'Dead Hard',
 'Deception',
 'Decisive Strike',
 'Deliverance',
 'Desperate Measures',
 'Detective\'s Hunch',
 'Distortion',
 'Diversion',
 'D??j?? Vu',
 'Empathy',
 'Fast Track',
 'Flashbang',
 'Flip-Flop',
 'For the People',
 'Guardian',
 'Head On',
 'Hope',
 'Inner Healing',
 'Iron Will',
 'Kindred',
 'Kinship',
 'Leader',
 'Left Behind',
 'Lightweight',
 'Lithe',
 'Lucky Break',
 'Mettle of Man',
 'No Mither',
 'No One Left Behind',
 'Object of Obsession',
 'Off the Record',
 'Open-Handed',
 'Pharmacy',
 'Plunderer\'s Instinct',
 'Poised',
 'Power Struggle',
 'Premonition',
 'Prove Thyself',
 'Quick & Quiet',
 'Red Herring',
 'Renewal',
 'Repressed Alliance',
 'Resilience',
 'Resurgence',
 'Rookie Spirit',
 'Saboteur',
 'Self-Aware',
 'Self-Care',
 'Self-Preservation',
 'Situational Awareness',
 'Slippery Meat',
 'Small Game',
 'Smash Hit',
 'Sole Survivor',
 'Solidarity',
 'Soul Guard',
 'Spine Chill',
 'Sprint Burst',
 'Stake Out',
 'Streetwise',
 'Technician',
 'Tenacity',
 'This Is Not Happening',
 'Unbreakable',
 'Up the Ante',
 'Urban Evasion',
 'Vigil',
 'Visionary',
 'Wake Up!',
 'We\'ll Make It',
 'We\'re Gonna Live Forever',
 'Windows of Opportunity'
]

killerPerks = ['A Nurse\'s Calling',
 'Agitation',
 'Bamboozle',
 'Barbecue & Chilli',
 'Beast of Prey',
 'Bitter Murmur',
 'Blood Echo',
 'Blood Warden',
 'Bloodhound',
 'Brutal Strength',
 'Claustrophobia',
 'Corrupt Intervention',
 'Coulrophobia',
 'Coup de Gr??ce',
 'Dark Devotion',
 'Dead Man\'s Switch',
 'Deadlock',
 'Deathbound',
 'Deerstalker',
 'Discordance',
 'Distressing',
 'Dragon\'s Grip',
 'Dying Light',
 'Enduring',
 'Eruption',
 'Fearmonger',
 'Fire Up',
 'Forced Penance',
 'Franklin\'s Demise',
 'Furtive Chase',
 'Gearhead',
 'Hangman\'s Trick',
 'Hex: Blood Favour',
 'Hex: Crowd Control',
 'Hex: Devour Hope',
 'Hex: Haunted Ground',
 'Hex: Huntress Lullaby',
 'Hex: No One Escapes Death',
 'Hex: Plaything',
 'Hex: Retribution',
 'Hex: Ruin',
 'Hex: The Third Seal',
 'Hex: Thrill of the Hunt',
 'Hex: Undying',
 'Hoarder',
 'Hysteria',
 'I\'m All Ears',
 'Infectious Fright',
 'Insidious',
 'Iron Grasp',
 'Iron Maiden',
 'Jolt',
 'Knock Out',
 'Leathal Pursuer',
 'Lightborn',
 'Mad Grit',
 'Make Your Choice',
 'Monitor & Abuse',
 'Monstrous Shrine',
 'Nemesis',
 'No Way Out',
 'Oppression',
 'Overcharge',
 'Overwhelming Presence',
 'Play with Your Food',
 'Pop Goes the Weasel',
 'Predator',
 'Rancor',
 'Remember Me',
 'Save the Best for Last',
 'Scourge Hook: Gift of Pain',
 'Shadowborn',
 'Sloppy Butcher',
 'Spies from the Shadows',
 'Spirit Fury',
 'Starstruck',
 'Stridor',
 'Surveillance',
 'Territorial Imperative',
 'Thanatophobia',
 'Thrilling Tremors',
 'Tinkerer',
 'Trail of Torment',
 'Unnerving Presence',
 'Unrelenting',
 'Whispers',
 'Zanshin Tactics'
]

mainMenu()
killerMenu()
survivorMenu()
randomSurvivor()
randomPerkSurv()
randomKiller()
randomPerkKiller()

randomSurv = False
randomKilr = False
randomSurvPerk = False
randomKillerPerk = False