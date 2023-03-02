# Operator and User Input

"""
Arithmetic Operators

+ Addition
- Subtraction
* Multiplication
/ Division
% Mod
** Exponentiation
// Floor division
"""

x = 15
y = 2

print("Addition", x + y)
print("Subtraction", x - y)
print("Multiplication", x * y)
print("Division", x / y)
print("Mod", x % y)
print("Exponentiation", x ** y)
print("Floor division", x // y)

"""
Assignment Operators

= Assign value of right side of expression to left side operand
+= Add and Assign: Add right side operand with left side operand and then assign to left operand
-= Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal
*= Multiply AND: Multiply right operand with left operand and then assign to left operand
/= Divide AND: Divide left operand with right operand and then assign to left operand
%= Modulus AND: Takes modulus using left and right operands and assign result to left operand
//= Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand
**= Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand
"""

"""
number = 5
number += 1
number -= 1
number *= 2
number /= 2
number %= 2
number **= 2
number //= 2
"""

"""
Comparison Operators

== Equal
!= Not equal
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
"""

x = 10
y = 5 

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Logical Operators

and   Returns True if both statements are true
or    Returns True if one of the statements is true
not   Reverse the result, returns False if the result is true
"""

print(x == y and x != y)
print(x == y or x != y)
print(not(x == y and x != y))