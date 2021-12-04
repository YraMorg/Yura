print("Task 1")
a = input()
print(len(a))
print("Task 2")
b = ""
if len(a) < 2:
    print()
else:
    for i in range(0, 2):
        b += a[i]
    for i in range(len(a)-2, len(a)):
        b += a[i]
    print(b)
print()
print("Task 3")
b = a[1:]
c = a[0]
print(b.find(c))
while b.find(c) > -1:
    b = b.replace(c, "$")
print(c+b)
print()
print("task 4")
if len(s) % 4 == 0:
    t = ""
    for i in range(len(s)-1, -1, -1):
        t += s[i]
    print(t)
else:
    print("length is not a multiple of 4")
print()
print("Task 5")
a = input("Введіть слова за допомогою цих знаків ', ': ")
words = a.split(", ")
words = set(words)
words = list(words)
words.sort()
print(words)