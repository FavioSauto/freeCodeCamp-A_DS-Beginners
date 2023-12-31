import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# It takes overall O(n^2) time to sort a list using selection sort.
def selection_sort(list):
  sorted_list = []

  print("%-25s %-25s" % (list, sorted_list))

  for i in range(0, len(list)):
    index_to_move = index_of_min(list)
    sorted_list.append(list.pop(index_to_move))
    print("%-25s %-25s" % (list, sorted_list))
    
  return sorted_list

def index_of_min(list):
  min_index = 0

  for i in range(1, len(list)):
    if list[i] < list[min_index]:
      min_index = i

  return min_index

print(selection_sort(numbers))