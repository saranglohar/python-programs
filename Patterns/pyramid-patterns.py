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
Half pyramid left-aligned (n=4)
*
**
***
****
Half pyramid right-aligned (n=4)
   *
  **
 ***
****
Number pyramid (n=4)
   1
  121
 12321
1234321
Alphabet pyramid (n=3)
  A
 ABA
ABC  BA
"""