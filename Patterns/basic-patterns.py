# Star Pattern
"""
1. Print a square of stars (n x n).
2. Print a right-angled triangle of stars.
3. Print an inverted right-angled triangle.
4. Print a triangle with stars aligned to the right.
5. Print a horizontal line of n stars.
6. Print a vertical line of n stars.
"""

"""
1. Print a square of stars (n x n).
Enter the number of rows: 5
*****
*****
*****
*****
"""

rows = int(input("Enter the number of rows: "))
for i in range(1, rows):
    print("*" * rows)

print()
"""
2. Print a right-angled triangle of stars.
*
**
***
****
"""

for i in range(0, rows):
    print("*" * i)

print()
"""
3. Print a right-angled triangle of stars.
****
***
**
*
"""

for i in range(0, rows):
    print("*" * (rows - i))

print()
"""
4. Print a triangle with stars aligned to the right.
   *
  **
 ***
****
"""

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)


print()
"""
5. Print a horizontal line of n stars.

*****
"""

for i in range(1, rows):
    print("*", end=" ")

print("\n")
"""
6. Print a vertical line of n stars.

*
*
*
*
*
"""

for i in range(1, rows):
    print("*")

print("\nNumber of rows: ", rows, " start from 1")
for i in range(1, rows):
    print(i, end=" ")

print("\nNumber of rows: ", rows, " start from 0")
for i in range(0, rows):
    print(i, end=" ")