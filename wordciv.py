#! /usr/bin/python3

state = 0
done = False

def showWelcomeScreen():
  print('Welcome To Word Civ')
  print('-------------------')
  print('')
  print('a| new game')
  print('b| load game')
  print('c| how to')
  print('d| quit')

def welcomeScreenInput():
  global done
  command = input('\nwhat would you like to do? ')
  if command == 'd':
    done = True
    print('quiting...')

while not done:
  if state == 0:
    showWelcomeScreen()
    welcomeScreenInput()
