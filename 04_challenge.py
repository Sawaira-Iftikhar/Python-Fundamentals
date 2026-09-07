"""
============================================
  LECTURE 1 - FILE 4: BOSS CHALLENGE 
  Topics: ALL 6 Topics Combined
  Total Challenges: 
============================================
  These problems test EVERYTHING you learned
  in Lecture 1.
============================================
"""

# ==========================================
#  CHALLENGE 1: The Smart Calculator (Easy-Medium)
#  Topics Used: Variables, Data Types, Operators, Type Conversion
# ==========================================

"""
Write a program that:
1. Creates two variables: num1 = "15" and num2 = "4" (as STRINGS)
2. Converts both to integers
3. Performs ALL 7 arithmetic operations (+, -, *, /, //, %, **)
4. Stores each result in a separate variable with a valid identifier name
5. Prints each result in this exact format:
   "15 + 4 = 19 (type: <class 'int'>)"
6. At the end, convert the sum to a boolean and print it. 
"""

num1 = "15"
num2 = "4"

#covnert both string to interger
num1 =int("15")
num2 =int("4")

add = num1 + num2
sub = num1 - num2
multip = num1 * num2
divide = num1 / num2
floor_divide = num1 // num2
reminder = num1 % num2
power = num1 ** num2