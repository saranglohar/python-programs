# 🔹 Pyramid Patterns
# Print a centered pyramid of stars.
# Print an inverted centered pyramid.
# Print a half pyramid using stars (left aligned).
# Print a half pyramid using stars (right aligned).
# Print a pyramid with numbers instead of stars.
# Print a pyramid with alphabets instead of stars.


"""
Centered pyramid (n=4)
   *
  ***
 *****
*******
"""
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (i + (i-1))
    print(spaces + stars)

print()
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))

"""
Inverted centered pyramid (n=4)
*******
 ***** 
  ***  
   *   
"""

print()

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))


"""
Half pyramid left-aligned (n=4)
*
**
***
****
"""

print()
for i in range(rows):
    print("*" * (i + 1))


print()

"""
Half pyramid right-aligned (n=4)
   *
  **
 ***
****
"""
print()

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (i + 1))


"""
Number pyramid (n=4)
   1
  121
 12321
1234321

"""

for i in range(1, rows + 1):
    print()
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")

"""
Alphabet pyramid (n=3)
  A
 ABA
ABCCBA
"""
print()
for i in range(1, rows + 1):
    print()
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for k in range(i - 1, 0, -1):
        print(chr(64 + k), end="")