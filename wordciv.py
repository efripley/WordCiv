#! /usr/bin/python3
import screens
import game

while not game.done:
  if game.state == 0:
    screens.welcomeScreen()
  elif game.state == 1:
    screens.newScreen()
  elif game.state == 2:
    screens.loadScreen()
  elif game.state == 3:
    screens.howToScreen()
  elif game.state == 4:
    screens.gameStartScreen()
