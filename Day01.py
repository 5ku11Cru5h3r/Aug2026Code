import math
from operator import le


def leap_year_checker():
    """
        Exercise 1: Leap Year Checker

    Write a program that takes a year as input from the user and checks whether it is a leap year or not.

    . Leap Year Criteria: A year is a leap year if it is divisible by 4, except for century years (ending in
    00), which must also be divisible by 400.
    . Sample Input: 2024
    . Sample Output: 2024 is a Leap Year.
    """
    year_entered = int(input("enter a year: "))
    if year_entered % 400 == 0 or year_entered % 4 == 0 and year_entered % 100 != 0:
        print(f"{year_entered} is a leap year")
    else:
        print(f"{year_entered} is a not leap year")


def fibbonacci():
    """
        Exercise 2: Fibonacci Sequence Generator

    Write a Python script to print the first N terms of the Fibonacci sequence, where N is provided by the
    user.

    . Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    . Sample Input: N = 6
    · Sample Output: 0, 1, 1, 2, 3, 5
    """
    num_1 = 0
    num_2 = 1
    user_input = int(input("Enter the number of terms:"))
    if user_input < 2:
        print("fibbonacci SERIES contains aleast 2 terms")
        return
    else:
        print(num_1, end=", ")
        print(num_2, end=", ")
        if user_input > 3:
            for i in range(user_input - 3):
                num_2, num_1 = num_1, num_2
                num_2 += num_1
                print(num_2, end=", ")
            print(num_2 + num_1)


def prime_check():
    """
    ### Exercise 3: Prime Number Checker
    Write a program that checks whether a positive integer  entered by the user is a prime number.
    * **Logic**: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    * **Sample Input**: `17`
    * **Sample Output**: `17 is a prime number.`
    """

    num_check = int(input("enter a number:"))
    x = math.floor(math.sqrt(num_check))
    for i in range(2, x + 1):
        if num_check % i == 0:
            print(f"{num_check} is not a prime number.")
            break
    else:
        print(f"{num_check} is a prime number.")


def odd_even_check():
    """
        Write a program that prompts the user for an integer and prints whether it is even or odd.
    . Sample Input: 7
    · Sample Output: 7 is an Odd number
    """
    num = int(input("enter a number:"))
    state = "even" if num % 2 == 0 else "odd"
    print(f"{num} is an {state} number")
    ...


def operator_calc():
    """
        Exercise 5: Basic Operator Calculator

    Create a program that takes two numbers and a math operator (+,
    corresponding calculation, and prints the result.

    . Sample Input: num1=15, num2=3, operator='/'
    . Sample Output: Result: 5.0
    """
    while True:
        a = int(input("num1 = "))
        b = int(input("num2 = "))
        operator = input("operator = ")
        if operator not in "+-*/":
            print("Invalid mathematical operation, skipping this operation.")

        else:
            match operator:
                case "+":
                    print(f"{a} + {b} = {(a+b)}")
                case "-":
                    print(f"{a} - {b} = {(a-b)}")
                case "*":
                    print(f"{a} * {b} = {(a*b)}")
                case "/":
                    print(f"{a} / {b} = {(a/b)}")
            break


def sum_n():
    """
        Exercise 6: Sum of N Natural Numbers

    Write a script that accepts a positive integer N from the user and calculates the
    sum of all natural numbers up to N.

    . Formula: sum_{i=1}^{N} i = frac{N(N+1)}{2}
    . Sample Input: N = 10
    . Sample Output: Sum: 55
    """
    n = input("N = ")
    print(f"Sum: {((n+1)/2)*n}")


def mul_gen():
    n = int(input())
    for i in range(1, 11):
        print(f"{n} x {i} = {(n*i)}")


def score_to_grade():
    """
        Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
    """
    score=int(input("Score = "))
    grades = {
        "A": 90, "B": 80, "C": 70, "D": 60, "F": 0
    }
    x=''
    for grade, max_score in grades.items():
        if score >= max_score:
            x= grade
    while True:
        try:
            score = float(input("Enter your test score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Test score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get the letter grade and display it
    print(f"Your letter grade is: {x}")


def main():
    # leap_year_checker()
    # fibbonacci()
    # odd_even_check()
    # prime_check()

    pass


main()

