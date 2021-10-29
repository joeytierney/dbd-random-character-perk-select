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
      randomPerkSurv()
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
      killerMenu()

    else:
      print('\nInvalid input! Please enter Y/N')

def randomPerkSurv():
  randomSurvPerk = True
  # Declare a variable as a random choice
  random_array_item = random.choice(survPerks)
  random_array_item1 = random.choice(survPerks)
  random_array_item2 = random.choice(survPerks)
  random_array_item3 = random.choice(survPerks)

  # Print the random choice
  print('\n***** RANDOM SURVIVOR *****')
  print('')
  print('      ' + random_array_item)
  print('      ' + random_array_item1)
  print('      ' + random_array_item2)
  print('      ' + random_array_item3)

  while randomSurvPerk is True:
    goAgain = input('\nWould you like to go again? (Y/N)\n> ')
    goAgain = goAgain.upper()

    if goAgain == 'Y':
      # Declare a variable as a random choice
      random_array_item = random.choice(survPerks)
      random_array_item1 = random.choice(survPerks)
      random_array_item2 = random.choice(survPerks)
      random_array_item3 = random.choice(survPerks)

      # Print the random choice
      print('\n***** RANDOM SURVIVOR *****')
      print('')
      print('      ' + random_array_item)
      print('      ' + random_array_item1)
      print('      ' + random_array_item2)
      print('      ' + random_array_item3)

    elif goAgain == 'N':
      survivorMenu()

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
 'Déjà Vu',
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
 'Coup de Grâce',
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

randomSurv = False
randomKilr = False
randomSurvPerk = False