def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)

#from conditions import print_even_numbers
#print_even_numbers(100)

def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        
        else:
            print(f"{number} is odd")

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 == 0:
            print(f"{number} is divisible by 3")

        elif number % 5 == 0:
            print(f"{number} is divisible by 5")

        elif number % 7 == 0:
            print(f"{number} is divisble by 7")

        else:
            print(f"{number} is not divisible by 3, 5, or 7")


def count_down(n):
    x = 0
    while n > x:
        print(n)
        n -= 1

def count_down_to_five(n):
    x = 0
    while n > x:
        print(n)

        if n == 5:
            break

        # print(n)
        n -= 1

# def count_down_to_five(n):
#     x = 0
#     while True


# Continue Statement

def divisible_by_seven(n):
    x = 1
    while x <= n:
        x += 1
        if x % 7 != 0:
            continue

        print(f"{x} is divisible by 7")

# QUESTIONS
# Using while, continue and if statements, write a function that prints all the odd numbers between 0 and 100.

# Create a function named fizzbuzz that does the following:

# for numbers divisible by 3 it prints "fizz"
# for numbers divisible by 5 it prints "buzz"
# for all the other numbers it prints "fizzbuzz"
# Use if, elif, else


# Question1
def odd_numbers(n):
    x = 0

    while x < n:
        x += 1

        if x % 2 == 0:
            continue

        print(f"{x} is an odd number")


def fizzbuzz(n):
    numbers = range(n)

    for number in numbers:
        if number % 3 == 0:
            print("fizz")

        elif number % 5 == 0:
            print("buzz")

        else:
            print("fizzbuzz")

