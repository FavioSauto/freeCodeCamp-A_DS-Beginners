import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# It takes overall O(n log n) time to sort a list using quick sort. -> Best Case Scenario
# It takes overall O(n^2) time to sort a list using quick sort. -> Worst Case Scenario
def quicksort(list):
  # if (len(list) <= 1):
  #   return list
  
  # less_than_pivot = []
  # greater_than_pivot = []
  # pivot = list[0] 

  # for value in list[1:]:
  #   if value <= pivot:
  #     less_than_pivot.append(value)
  #   else:
  #     greater_than_pivot.append(value)

  # return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

  if (len(list) <= 1):
    return list
  
  pivot = list[len(list) // 2]
  left = [x for x in list if x < pivot]
  middle = [x for x in list if x == pivot]
  right = [x for x in list if x > pivot]

  return quicksort(left) + middle + quicksort(right)


sorted_numbers = quicksort(numbers)
print(sorted_numbers)