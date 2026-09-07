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
