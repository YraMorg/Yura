print("Task 1(1)")
print(0)
print()
print("Task 1(2)")
print(0.0)
print()
print("Task 1(3)")
print(101)
print()
print("Task 1(4)")
print(1000.)
print()
print("Task 1(5)")
print(10**3)
print()
print("Task 1(6)")
number = int(input("Введіть позитивне число "))
if number < 0:
   print("Помилка")
elif number > 0:
   print(number)
elif number == 0:
   print("Помилка");

number = int(input("Введіть негативне число "))
if number < 0:
   print(number)
elif number > 0:
   print("Помилка")
elif number == 0:
   print("Помилка")

number = int(input("Введіть число нуль "))
if number < 0:
   print("Помилка")
elif number > 0:
   print("Помилка")
elif number == 0:
   print(number)
print()
print("Task 1(7)")
print("(A+B)/C")
a = int(input("Number(A)"))
b = int(input("Number(B)"))
c = int(input("Number(C)"))
d = (a + b)/c
print(d)
print()
print("A*B-C")
a = int(input("Number(A)"))
b = int(input("Number(B)"))
c = int(input("Number(C)"))
d = (a*b-c)
print(d)
print()
print("Task 3(1)")
x = int(input("Numbers"))
print(x % 10000)
print()
print("Task 3(2)")
a = input("Введіть трьохзначне число: ")
a = int(a)
b1 = a % 10
a = a // 10
b2 = a % 10
a = a // 10
print("Сума цифр числа:", a + b1 + b2)