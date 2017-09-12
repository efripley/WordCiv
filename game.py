import random
import screens

state = 0
done = False
name = False
numTroops = 0

def newTroop():
  global numTroops
  if hangman(1, 2):
    numTroops += 1

def hangman(completions, attempts):
  #keep track of successful completions and attempts
  success = 0
  total = 0
  #while not enough completions or not enough attempts
  while total < attempts:
    #run hangman loop
    if hangmanloop():
      success += 1
    total += 1
  return success >= completions

def hangmanloop():
  file = open("words.txt", "r")
  lines = file.readlines()
  file.close();
  #choose a random word from file
  index = random.randint(0, 10)
  word = lines[index].rstrip()
  guess = list()
  print(word)
  for ch in word:
    guess.append(' ')
  print(len(guess))
  letters = ''
  attempt = 1
  while attempt <= 5:
    #allow user to input character
    letter = screens.hangmanScreen(''.join(guess), letters)
    letters += letter
    temp = ''
    correct = False
    #test if charachter exists in word
    for a, ch in enumerate(word):
      if letter == ch:
        guess[a] = letter
        correct = True
    if not correct:
      attempt += 1
    #test if spaces remain in word and break if not
    if ''.join(guess) == word:
      break
  #return true if word is guessed
  return attempt <= 5

