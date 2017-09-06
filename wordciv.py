#! /usr/bin/python3

class Game:
  state = 0
  done = False
  name = False
game = Game();


#Game Screens
def welcomeScreen():
  global game
  print('Welcome To Word Civ')
  print('-------------------')
  print('')
  print('n| new game')
  print('l| load game')
  print('h| how to')
  print('q| quit')
  print('')

  command = input('\nwhat would you like to do? ')
  if command == 'a':
    game.state = 1
  elif command == 'b':
    game.state = 2
  elif command == 'c':
    game.state = 3
  elif command == 'd':
    game.done = True
    print('quiting...')

def newScreen():
  global game
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
  global game
  print('Load Game')
  print('---------')
  print('')
  print('type \'delete <game name>\' to delte game')
  print('type \'exit\' to go back')

  command = input('what would you like to do? ')
  if command == 'exit':
    game.state = 0

def HowToScreen():
  global game
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
  global game
  print(game.name)
  for ch in game.name:
    print('-', end = '')
  print('')

  command = input('command: ')
  if command == 'exit':
    game.state = 0

while not game.done:
  if game.state == 0:
    welcomeScreen()
  elif game.state == 1:
    newScreen()
  elif game.state == 2:
    loadScreen()
  elif game.state == 3:
    howToScreen()
  elif game.state == 4:
    gameStartScreen()
