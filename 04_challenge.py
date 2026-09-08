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

print("15 + 4 = ",add,"type:",type(add))
print("15 - 4 = ",sub,"type:",type(sub))
print("15 * 4 = ",multip,"type:",type(multip))
print("15 / 4 = ",divide,"type:",type(divide))
print("15 // 4 = ",floor_divide,"type:",type(floor_divide))
print("15 % 4 = ",reminder,"type:",type(reminder))
print("15 ** 4 = ",power,"type:",type(power))

sum = bool(add)
print("sum as Boolean: ",sum)

#--------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 2: The Ultimate Expression (Hard) 
#  Topics Used: ALL 6 Topics
#  program:  Print a formatted bill
# ==========================================

# ===========================================
#    This program is little bit long and
#  difficult so here's the full explanation.
# ============================================
"""
Solve this step by step. This ONE expression uses:
- Character set (Unicode variable names are allowed!)
- Variables & Identifiers
- Data Types (int, float, bool)
- Operators (arithmetic, comparison, logical)
- Type Conversion (implicit + explicit)

Step 1: Create these variables (use valid identifiers):
   price_per_item = 299.5
   quantity = "3"          # Notice: it's a string!
   discount_percent = 10
   is_member = True        # Members get extra 5% off

Step 2: Calculate the total bill:
   a) Convert quantity to int
   b) Calculate subtotal = price * quantity
   c) Calculate discount = subtotal * (discount_percent / 100)
   d) If is_member is True, apply extra 5% discount on the
      already discounted price
   e) Calculate final_total = subtotal - all discounts

Step 3: Print a formatted bill:
   ================================
        🧾 SHOPPING BILL
   ================================
   Price per item:  ₹299.5
   Quantity:        3
   Subtotal:        ₹898.5
   Discount (10%):  ₹89.85
   Member Discount: ₹40.4325
   --------------------------------
   FINAL TOTAL:     ₹768.2175
   Type of total:   <class 'float'>
   Is bill > 500?   True
   ================================
   
Step 4: Convert the final total to int (floor it) and print.
        Convert it to bool and print.
        Convert it to string and print with a message.

"""
