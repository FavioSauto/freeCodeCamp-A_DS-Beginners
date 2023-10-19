import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(list):
  for index in range(len(list) - 1):
    if list[index] > list[index + 1]:
      return False

  return True

def bogo_sort(list):
  attempts = 0
  while not is_sorted(list):
    print(attempts)
    random.shuffle(list)
    attempts += 1

  return list

print(bogo_sort(numbers))