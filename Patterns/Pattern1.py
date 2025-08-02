# First pattern in python
"""
Enter number of level to print:
*
**
***
****
*****
"""
noOfRows = int(input("Enter number of level to print: "))

for i in range(1, noOfRows):
    if i != 1:
        print()
    for j in range(i):
        print("*", end="")
