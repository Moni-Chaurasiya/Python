# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x= lambda a: a+10

print(x(20))

x= lambda a,b:a*b
print(x(5,6))

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def mult(n):
    return lambda a:a*n

mydouble=mult(2)

print(mydouble(10))

# Recursion is when a function calls itself.

def countdown(n):
    if(n==1):
        return n
    else:
        return n* countdown(n-1)
    
c=countdown(5)
print(c)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

