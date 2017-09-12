#Game Screens
import game

def clear():
  print("\033[H\033[J")

def welcomeScreen():
  clear()
  print('Welcome To Word Civ')
  print('-------------------')
  print('')
  print('n| new game')
  print('l| load game')
  print('h| how to')
  print('q| quit')
  print('')

  command = input('\nwhat would you like to do? ')
  if command == 'n':
    game.state = 1
  elif command == 'l':
    game.state = 2
  elif command == 'h':
    game.state = 3
  elif command == 'q':
    game.done = True
    print('quiting...')

def newScreen():
  clear()
  print('New Game')
  print('--------')
  print('')
  print('type \'exit\' to go back')

  command = input('what would you like to name your game? ')
  if command == 'exit':
    game.state = 0
  else:
    game.name = command
    game.state = 4

def loadScreen():
  clear()
  print('Load Game')
  print('---------')
  print('')
  print('type \'delete <game name>\' to delte game')
  print('type \'exit\' to go back')

  command = input('what would you like to do? ')
  if command == 'exit':
    game.state = 0

def HowToScreen():
  clear()
  print('How To')
  print('------')
  print('')
  print('u| scroll up')
  print('d| scroll down')
  print('q| go back')

  command = input('what would you like to do? ')
  if command == 'u':
    print('scrolling up')
  elif command == 'd':
    print('scrolling down')
  elif command == 'q':
    game.state = 0

def gameStartScreen():
  clear()
  print(game.name)
  for ch in game.name:
    print('-', end = '')
  print('')
  print('t| new troop | 1/2 games | troops:', game.numTroops)
  print('q| quit')

  command = input('command: ')
  if command == 't':
    game.newTroop()
  elif command == 'q':
    game.state = 0


def hangmanScreen(guess, letters):
  clear()
  print(game.name)
  for ch in game.name:
    print('-', end = '')
  print('\n')
  print('WORD')
  print(guess)
  for ch in guess:
    print('-', end = '')
  print('\n')
  print('LETTERS')
  print(letters)
  for ch in letters:
    print('-', end = '')

  command = input('best guess: ')
  return command
