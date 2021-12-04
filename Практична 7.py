print("Task 1")
a = input("")
b = ""
for i in range(0, len(a)):
    if a[i] == "'":
        b += '"'
    elif a[i] == '"':
        b += "'"
    else:
        b += a[i]
a = b
print(b)
print()
print("Task 2")
a = input("Введіть паліндром: ")
i, c = 0, len(a) - 1
flag = True
b = a.lower()
while i < c and flag:
    if b[i] != b[c]:
        flag = False
        break
    i += 1
    c -= 1
print(flag)
print()
print("Task 3")
x = input("")
splitter = input("Введіть символ для розділення за допомогою: ")
res = []
while x.find(splitter) > -1:
    splitter_index = x.find(splitter)
    res.append(x[0:splitter_index])
    x = x[splitter_index+len(splitter):]
res.append(x)
print(res)
print("")
print("Task 4")
y = input("Введіть послідовність слів: ")
first_index = 0
last_index = y.find(" ")
longest_word = y[first_index:last_index]
while last_index != -1:
    first_index += last_index + 1
    last_index = y[first_index:].find(" ")
    if len(y[first_index:first_index+last_index]) > len(longest_word):
        longest_word = y[first_index:first_index+last_index]
if len(y) - first_index > len(longest_word):
    longest_word = y[first_index:]
print(longest_word)
print()
print("Task 5")
z = input("Введіть ціле число: ")
res = 0
for i in z:
    if int(i) % 2 != 0:
        res += int(i)
print(res)
print()
print("Task 6")
b = str(bin(int(a)))[2:]
res = 0
for i in b:
    res += int(i)
print(res)
print()
print("Task 7")
directions = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
n = 0
s = 0
w = 0
e = 0
for i in directions:
    if i == "NORTH":
        n += 1
    elif i == "SOUTH":
        s += 1
    elif i == "WEST":
        w += 1
    else:
        e += 1

x = abs(e-w)
y = abs(n-s)
if n > s:
    for i in range(0, s):
        directions.remove("NORTH")
        directions.remove("SOUTH")
else:
    for i in range(0, n):
        directions.remove("NORTH")
        directions.remove("SOUTH")

if e > w:
    for i in range(0, w):
        directions.remove("WEST")
        directions.remove("EAST")
else:
    for i in range(0, e):
        directions.remove("WEST")
        directions.remove("EAST")
print(directions)
print()
print("Task 8")
words = ["","bc","","cd"]
d = len(words)
res = []
for i in range(0, d):
    if words[i] == "":
        print("Пусте слово")
        break
    res.append(words[i])
    if i < d-1 and words[i+1] != "":
        if words[i][len(words[i])-1] != words[i+1][0]:
            break
print(res)