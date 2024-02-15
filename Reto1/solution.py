def problem_1(limit): 
  total_sum = 0
  
  for num in range(limit):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num
  return total_sum      

def problem_2(limit):
 
  a, b = 1, 2
  even_sum = 0

  while b <= limit:
      if b % 2 == 0:
          even_sum += b
        
      a, b = b, a + b
  return even_sum


def problem_3(num):
  largest_prime = 1

  while num % 2 == 0:
      largest_prime = 2
      num //= 2

  
  for i in range(3, int(num**0.5) + 1, 2):
      while num % i == 0:
          largest_prime = i
          num //= i
  if num > 1:
      largest_prime = num

  return largest_prime

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def problem_4():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

def problem_5(n):
    def MCD(a, b):
          while b:
              a, b = b, a % b
          return a

    def MCM(a, b):
          return a * b // MCD(a, b)

    multiple = 1
    for i in range(2, n + 1):
          multiple = MCM(multiple, i)
    return multiple

