def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def divide(a, b):
    """Divide a by b."""
    return a / b

def square(a):
    """Square a number."""
    return a ** 2

def cube(a):
    """Cube a number."""
    return a ** 3

def square_n_times(number, n):
    """Square the number n times and return the sum of all intermediate values."""
    result = number
    total = number
    for i in range(n):
        result = result ** 2
        total += result
    return total

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)
