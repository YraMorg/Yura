print("Task 1")
a = input("Введіть 4 числа:")
print(max(a))
print()
print("Task 2")
y = int(input())
if y % 4 == 0 and y % 100 != 0:
    print("YES")
elif y % 400 == 0:
    print("YES")
else:
    print("NO")
print()
print("Task 3")
a = int(input("Введіть будь яке число"))
b = int(input("Введіть будь яке число"))
c = int(input("Введіть будь яке число"))
a, b, c = sorted([a, b, c])
if a + b <= c:
    print("не існує")
elif c**2 == (a**2) + (b**2):
    print("прямокутний")
elif ((a**2) + (b**2) - (c**2)) / (2 * a * b) > 0:
    print("гострий")
else:
    print("тупий")
print()
print("Task 4")
for x in range(0, 100):
    if x % 7 == 0:
        print(x)
print()
print("Task 5")
n = int(input("Ведіть будь яке число"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
print()
print("Task 7")
for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print (num)