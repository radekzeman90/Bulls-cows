"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Radek Zeman
email: ze.ra@seznam.com
discord: Radek Zeman
"""

import random
import time

def random_4digit_number():
  '''
  Funkce při spuštění z číslic 0-9 generuje 4ciferné číslo,
  ve kterém se žádná číslice neopakuje.
  '''
  n = list()
  l = list(range(1,10))
  while len(n) < 4:
    random.shuffle(l)
    n.append(str(l[0]))
    l.remove(l[0])
  random_number = ''.join(n)
  return(random_number)

#Spuštění funkce která, vygeneruje 4ciferné číslo z unikátních číslic
random_number = random_4digit_number()

# začíná měření času, za který uživatel uhádne číslo.
start = time.time()

# úvodní uvítání
separator = 50 * "-"
print("Hi there!")
print(separator)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(separator)
print(random_number)
count = 1
guess = input("Enter a number:")

while guess != random_number:
  #Tyto podcykly ověřují, zda je vstup 4ciferné číslo
  while guess.isnumeric() == False:
    print("Tento vstup není číselný")
    guess = input("Enter a number:")
  while len(guess) != 4:
    print("Number is not 4digit")
    guess = input("Enter a number:")
  bull = 0
  cow = 0
  guess_letter = list()
  random_number_letter = list()
  enumerate_guess = list(enumerate(guess))
  enumerate_guess_copy = enumerate_guess.copy()
  enumerated_random_number = list(enumerate(random_number))
  enumerated_random_number_copy = enumerated_random_number.copy()

  # Tento for cyklus určuje počet uhodnutých písmen na správných pozicích
  for position, number in enumerate_guess:
    if (position, number) in enumerated_random_number:
      bull = bull + 1
      enumerated_random_number_copy.remove((position, number))
      enumerate_guess_copy.remove((position, number))

  # Tento for cyklus určuje počet uhodnutých písmen na špatných pozicích
  for tupl in enumerate_guess_copy:
    for tupl2 in enumerated_random_number_copy:
      if tupl[1] == tupl2[1]:
        cow = cow + 1
        enumerated_random_number_copy.remove(tupl2)
        break
  count += 1

  # tato část kódu uživateli sdělí
  # kolik číslic na správných/špatný pozicích uhodl.
  if cow == 1:
    cow_output = "cow"
  else:
    cow_output = "cows"
  if bull == 1:
    bull_output = "bull"
  else:
    bull_output = "bulls"
  print(f"{bull} {bull_output}, {cow} {cow_output} ")
  print(separator)
  guess = input(">>> ")

# Uhodutím správného čísla se ukončí měření času.
end = time.time()

# Zde se vyprintují metriky odhadu uživatele.
if count == 1:
  print(f"Correct, you've guessed the right number in {count} guess!")
else:
  print(f"Correct, you've guessed the right number in {count} guesses!")
print(separator)
if count < 4:
  print('That is completely awesome.')
elif (count >= 4) and (count <= 8):
  print('That is very good.')
elif (count > 8) and (count <= 12):
  print('This attempt was average.')
else:
  print('You should practice more.')
print(separator)
print(f"You managed to guess the number in {(end - start):.1f} seconds")