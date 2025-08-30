### 🔹 **Diamond and Hourglass**
# 13. Print a full diamond of stars.
# 14. Print a hollow diamond pattern.
# 15. Print an hourglass pattern.
# 16. Print a mirrored diamond (right-aligned).

### 🔹 **Diamond and Hourglass**



"""
13. **Full diamond (n=3)**
  *  
 *** 
*****
 *** 
  *  
"""
print("---- Full Diamond n = 3")

rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))



"""
14. **Hollow diamond (n=3)**
  *  
 * * 
*   *
 * * 
  *  
"""
print("---- Hollow diamond (n=3)")

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * ( 2 * i - 3) + "*" )

for i in range(rows -1 , 0 , -1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * ( 2 * i - 3) + "*" )

"""
15. **Hourglass (n=4)**

********
 ******
  ****
   **
  ****
 ******
********
"""
print(f"---- Hourglass (n={rows})")

for i  in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (i * 2))

for i  in range(2, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (i * 2))
"""
16. **Mirrored diamond (n=4)**

    *
   **
  ***
   **
    *
"""
print(f"---- Mirrored diamond (n={rows})")

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print(f"{'*' * i}")