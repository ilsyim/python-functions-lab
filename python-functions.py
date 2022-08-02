# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum


# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.
def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
# print(largest([2, 40, 7, 9]))

    
# 3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(string1, string2):
  count_string = string1.replace(string2, '')

  return (len(string1) - len(count_string)) // len(string2)
# print(occurrences('free', 'e'))
    
# 4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on `args`.
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
  
