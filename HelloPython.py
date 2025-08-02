print('Hello Python')

a = 10
print(a)

for i in range(10):
    print(i,sep="," ,end=" ")

print()

count = 0
while count < 5:
    print(count, end=" ")
    count = count + 1
    count += 1

print("\n------")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end = ' ')

print('\n Nested loops')
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

if '111' == '111':
    print("\n111 is equals")


for i in range(2, 20, 4):
    print(i)