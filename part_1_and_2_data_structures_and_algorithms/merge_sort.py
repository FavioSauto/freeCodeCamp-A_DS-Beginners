def split(list):
  """
  Divide the unsorted list at midpoint into sublists
  Returns two sublists - left and right
  
  Takes overall O(k log n) time
  """
  mid = len(list) // 2
  
  left = list[:mid]
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Merges two lists, sorting them in the process
  Returns a new merged list

  Takes overall O(n) time
  """
  new_list = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      new_list.append(left[left_index])
      
      left_index += 1
    else:
      new_list.append(right[right_index])
      
      right_index += 1

  while left_index < len(left):
    new_list.append(left[left_index])
    left_index += 1

  while right_index < len(right):
    new_list.append(right[right_index])
    right_index += 1

  return new_list


def merge_sort(list):
  """
  Sort a list in ascending order
  Returns a new sorted list

  Steps:
  1. Divide: Find the midpoint of the list and divide into sublists
  2. Conquer: recursively sort the sublists created in previous step
  3. Combine: Merge the sorted sublists created in previous step

  Takes overall O(kn log n) time
  """
  if (len(list) <= 1):
    return list
  
  left_half, right_half = split(list)

  left = merge_sort(left_half)
  right = merge_sort(right_half)
  
  return merge(left, right)

def verify_sorted(list):
  n = len(list)

  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])

