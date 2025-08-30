# ### 🔹 **Hollow Patterns**
# 17. Print a hollow square of stars.
# 18. Print a hollow right-angled triangle.
# 19. Print a hollow pyramid.
# 20. Print a hollow diamond.

"""
Hollow Patterns  - 30th Aug 2024
Hollow square (n=4)
****
*  *
*  *
****
"""
print("Hollow Patterns: ")
rows = 6

for i in range(1, rows +1):
    if i == 1 or i == rows:
        print("*" * rows)
    else:
        print("*" + (" " * (rows - 2)) + "*")

"""
Hollow right triangle (n=4)
*
**
* *
****
"""
print("\nHollow right triangle: ")



"""
Hollow pyramid (n=4)
   *
  * *
 *   *
*******

"""

"""
Hollow diamond (n=3)
  *
 * *
*   *
 * *
  *
"""