def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  
  return total

print(sum([1, 2, 3, 4, 5]))

def sum_recursive(numbers):
  # if len(numbers) == 1:
  #   return numbers[0]
  
  # return numbers[0] + sum_recursive(numbers[1:])

  if not numbers:
    return 0
  
  print("Calling sum(%s)" % numbers[1:])
  remaining_sum = sum_recursive(numbers[1:])

  print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
  return numbers[0] + remaining_sum

print(sum_recursive([1, 2, 3, 4, 5]))
