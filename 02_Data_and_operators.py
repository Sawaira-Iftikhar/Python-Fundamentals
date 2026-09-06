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

# Q3. Create two variables that contain the same
#     numerical value, but use different data types.
#
#     Compare:
#     - Their values
#     - Their data types
#
#     Print the results.
#
#     What difference do you observe?


