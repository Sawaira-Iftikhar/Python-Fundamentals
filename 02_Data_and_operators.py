"""
============================================
  LECTURE 1 - FILE 2: DATA & OPERATORS
  Topics: Data Types, Types of Operators
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: DATA TYPES (Q1 - Q5)
# ==========================================

# Q1. Create one variable for EACH of these data types:
#     int, float, str, bool, complex
#     Print each variable along with its type using type().

name = "Green International Uni"
semester = 2
cgpa = 3.64
com =  3 + 4j

print(name,type(name))
print(semester,type(semester))
print(cgpa,type(cgpa))
print(com,type(com))

# ------------------------------------------------------------------------------------------

# Q2. PREDICT THE OUTPUT (guess first, then run):
#   Two situations
#     print(type(a) == type(b))
#     print(a == b)

a = 90
b = 90.0
print(type(a) == type(b))
print(a == b) 

#   My guess for line 1:  The answer is going to be in bool type (False) bcz data-type of "a" is "int" and data-type of "b" is "float" so it's not equal
#   My guess for line 2:  The answer is going to be in bool type (true) bcz both sides have same values

# ------------------------------------------------------------------------------------------

# Q3. Create a variable called data.
#
#     Store a string in it and print its type.
#     Then store an integer in it and print its type.
#     Then store a float in it and print its type.
#
#     Write a comment explaining what you notice.

data = "Hello World"
print(type(data))

data = 10
print(type(data))

data = 10.67
print(type(data))

# So what we learn form here is that a same variable can store and run different data types in Python.

"The variable 'data' store three types of value 1. string , 2. integer , 3. float "
"Python Allows a variable to assigned a value of a different data type later. "
"This is one reason Python is called a dynamically typed language."

# ------------------------------------------------------------------------------------------

# Q4. Find the data type of each expression by using
#     type().
#
#     expression1 = 15 / 3
#     expression2 = 15 // 3
#     expression3 = "Python" * 2
#     expression4 = 5 == 5
#     expression5 = 4 + 6.0
#
#     Print each result and its type.

expression1 = 15 / 3
expression2 = 15 // 3
expression3 = "Python" * 2
expression4 = 5 == 5
expression5 = 4 + 6.0

print("expression1 = 15 / 3",type(expression1))
print("expression2 = 15 // 3", type(expression2))
print("expression3 = 'Python' * 2", type(expression3))
print("expression4 = 5 == 5", type(expression4))
print("expression5 = 4 + 6.0", type(expression5))

# ------------------------------------------------------------------------------------------

# Q5. What is the output of this tricky code? Explain WHY in a comment.
#
#     print(type(type(42)))

print(type(type(42)))

"    My guess:  <class 'type'> "
"    Explanation: type(42) gives the <class 'int' and the type of <class 'int'> is itself 'type'. "
"      Therefore, the final result is <class 'type'>. "

# ------------------------------------------------------------------------------------------

# ==========================================
#  PART B: TYPES OF OPERATORS (Q6 - Q10)
# ==========================================

# Q6. ARITHMETIC OPERATORS:
#     Given a = 17 and b = 5, calculate and print:
#     - Addition, Subtraction, Multiplication
#     - True Division (/), Floor Division (//)
#     - Modulus (%), Exponentiation (**)

a = 17
b = 5

print(a,"+",b ," = ",a+b)
print(a,"-",b ," = ",a-b)
print(a,"*",b ," = ",a*b)
print(a,"/",b ," = ",a/b)
print(a,"//",b ," = ",a//b)
print(a,"%",b ," = ",a%b)
print(a,"**",b ," = ",a**b)

# ------------------------------------------------------------------------------------------

# Q7. COMPARISON & LOGICAL OPERATORS:
#     What will each print? Guess first, then verify.
#
print(5 == 5.0)       # 
print(5 is 5.0)       # 
print(True and False) # 
print(True or False)  # 
print(not True)       # 
print(0 and 5)        # 
print("" or "Hello")  # 
#
#     BONUS: Explain WHY "5 == 5.0" and "5 is 5.0" give different results.
