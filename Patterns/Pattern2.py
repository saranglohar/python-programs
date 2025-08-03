# Star pattern 2
"""
Enter the number of rows: 5
    *
   * *
  * * *
 * * * *
* * * * * 
"""
print("Start Pattern 2nd Program")

rows = 5  # Number of rows in the pattern
print()
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '* ' * i
    print(spaces + stars)




