"""
============================================
  LECTURE 1 - FILE 1: BASICS
  Topics: Character Set, Variables, Identifiers
  Total Questions: 
============================================

"""

# ==========================================
#  PART A: PYTHON CHARACTER SET 
# ==========================================

#  Q1. Print your name in English using the print() function.
#      Then print your name in any other language (Hindi, Urdu, Arabic, etc.)

print("My name is Sawaira")
print("السلام علیکم")  #it means python is unicode
 
# ----------------------------------------------------------------------------------------------------

# Q2. Python's character set includes letters, digits, special symbols,
#     and white spaces. Create a single string variable that contains
#     at least ONE of each: a letter, a digit, a special symbol, and a space.
#     Print it.

print("My Python 3.12 version is running smoothly !")

# ----------------------------------------------------------------------------------------------------

# ==========================================
#  PART B: Variables
# ==========================================

# Q3. Create three variables to store your:
#     - name (string)
#     - age (integer)
#     - height in feet (float)
#     Print all three with labels.

name  = "Sawaira"
age = 23
cgpa = 3.64

print("Name: ",name )
print("Age: ",age )
print("CGPA: ",cgpa )

# ----------------------------------------------------------------------------------------------------

# Q4. Assign values 10, 20, 30 to variables a, b, c in a SINGLE line.
#     Then print all three separated by a dash "-".

a, b, c = 10, 20, 30
print(a, b, c, sep="-")

# ----------------------------------------------------------------------------------------------------

# Q5. Swap two variables WITHOUT using a third variable.
#     Start with: x = 5, y = 10
#     After swap: x should be 10, y should be 5
#     Print both after swapping.

x = 20
y = 40

x, y = y, x

print("After Swapping: x =", x,"y =", y)

# ----------------------------------------------------------------------------------------------------

# ==========================================
#  PART C: IDENTIFIERS 
# ==========================================

# Q6. List 5 Python keywords (reserved words) that CANNOT be used
#     as variable names. Store them in 5 separate variables as strings
#     and print them.

keyword_1 = "if"
keyword_2 = "else"
keyword_3 = "not"
keyword_4 = "and"
keyword_5 = "assert"

print("Keyword 1: ", keyword_1)
print("Keyword 2: ", keyword_2)
print("Keyword 3: ", keyword_3)
print("Keyword 4: ", keyword_4)
print("Keyword 5: ", keyword_5)

# ----------------------------------------------------------------------------------------------------

