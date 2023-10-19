def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

# This has constant space complexity O(1)
# Because we don't create any new variables, 
# we just use the existing ones
def binary_search(list, target):
    firstIndex = 0
    lastIndex = len(list) - 1

    while firstIndex <= lastIndex:
        midpoint = (firstIndex + lastIndex) // 2 # double slash is for floor division
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            firstIndex = midpoint + 1
        elif list[midpoint] > target:
            lastIndex = midpoint - 1
    return None
    

# This has O(log n) time complexity
# Because we are dividing the input in half every recursive call
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False

    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(index): 
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

linear_result = linear_search(numbers, 10)
verify(linear_result)

binary_result = binary_search(numbers, 10)
verify(binary_result)

recursive_binary_result = recursive_binary_search(numbers, 10)
verify(recursive_binary_result)


# Depending on the language there are different ways to run the code
# There is the tail optimization that can be used to optimize the recursive function
# But this is not available in Python, and it is available in Swift.
# So to know the space complexity of different implementations of the same algorithm and choose the best one
# You need to know the language and the compiler that is being used.