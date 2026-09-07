"""
============================================
  LECTURE 1 - FILE 3: TYPE CONVERSION
  Topics: Type Conversion & Casting
  Total Questions: 
============================================
"""

# ============================================
#  PART A: EXPLICIT CONVERSION / Type Casting
# ============================================

# Q1. Convert the following and print each result WITH its type:
#     a) float 9.99  → int
#     b) string "42" → int
#     c) int 100     → float
#     d) int 1       → bool
#     e) int 0       → bool
#     f) int 7       → string

a = 9.99 
a =int(9.99)
print("9.99 -",a,type(a))

b = "43"
b = int("42")
print('"42" -',b,type(b))

c = 100
c =float(100)
print("100 -",c,type(c))

d = 1
d =bool(1)
print("1 -",d,type(d))

e = 0
e =bool(0)
print("0 -",e,type(e))

f = 7
f =str(7)
print("7 -",f,type(f))

#------------------------------------------------------------------------------------

# Q2. Convert the string "3.14" to a float, then to an int.
#     Print the result at each step.
#     Can you convert "3.14" directly to int? Try it and explain the error.

num = "3.89"
print("String: ",num, type(num))
num = float("3.89")
print("Float: ",num, type(num))
num = int(3.89)
print("int: ",num,type(num))

"Direct str→int: ERROR because in string the vlaue is in decimal so it if we try to convert string in int in this situation it will show error we have to go with sequence."

#------------------------------------------------------------------------------------

# ==========================================
#  PART B: IMPLICIT CONVERSION (Q5 - Q7)
# ==========================================

# Q4. What is IMPLICIT type conversion? Give an example where Python
#     automatically converts one type to another WITHOUT you asking.
#     Print the result and its type.

result = 30 + 45.7
print("the result is: ",result,type(result))

