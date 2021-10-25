print("1.1")
num = int(input("Введіть число: "))
if (num % 2) == 0:
   print("{0} Парне".format(num))
else:
   print("{0} Непарне".format(num))
print()
print("1.2")
x = int(input("Введіть число кратне 20:"))
if x % 20 != 0:
    print("Помилка")
elif x % 20 == 0:
   print(x//20)
print()
print("1.3")
a = int(input("Введіть позитивне число(1):"))
b = int(input("Введіть позитивне число(2):"))
if a <= 0:
    print("Помилка")
elif b <= 0:
    print("Помилка")
else: print(a,b)
print()
print("1.4")
a = int(input("Введіть позитивне або негативне число(1):"))
b = int(input("Введіть позитивне або негативне число(2):"))
if a <= 0 and b <= 0:
    print(a,b)
elif a >= 0 and b >= 0:
    print(a,b)
else: print("Помилка")
print()
print("1.5")
a = int(input("Введіть позитивне або негативне число(1):"))
b = int(input("Введіть позитивне або негативне число(2):"))
if a <= 0 and b <= 0:
    print("Помилка")
elif a >= 0 and b >= 0:
    print("Помилка")
else: print(a,b)
print()
print("1.6")
a = int(input("Введіть позитивне або негативне число(1):"))
b = int(input("Введіть позитивне або негативне число(2):"))
c = int(input("Введіть позитивне або негативне число(3):"))
if a != b and a != c:
    print("Помилка")
elif b != a and b != c:
    print("Помилка")
elif c != a and c != b:
    print("Помилка")
else:print(a,b,c)
print()
print("1.7")
a = int(input("Введіть позитивне або негативне число(1):"))
b = int(input("Введіть позитивне або негативне число(2):"))
c = int(input("Введіть позитивне або негативне число(3):"))
if a == b or a == c:
    print("Помилка")
elif b == a or b == c:
    print("Помилка")
elif c == a or c == b:
    print("Помилка")
else:print(a,b,c)
print()
print("1.8")
a = int(input("Введіть позитивне або негативне число(1):"))
b = int(input("Введіть позитивне або негативне число(2):"))
c = int(input("Введіть позитивне або негативне число(3):"))
if a == b and a != c:
    print(a,b,c)
elif a != b and a == c:
    print(a,b,c)
elif b != a and b == c:
    print(a,b,c)
elif b == a and b != c:
    print(a,b,c)
elif c != a and c == b:
    print(a,b,c)
elif c == a and c != b:
    print(a,b,c)
else:print("Помилка")