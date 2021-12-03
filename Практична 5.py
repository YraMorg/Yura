print("Task 1")
a = []
for i in range(1, 31):
    a.append(i**2)
print(a)
print("Task 2")
exam_st_date = (11, 12, 2014)
print(f"Розклад занять: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}!")
print("Task 3")
b = input("Введіть декулька чисел: ")
while "," in c:
    c = c.replace(",", " ")

c = c.split()
d = tuple(c)
print(c, st)
print("Task 4")
x = [1, 2, 3, 4]
y = [1, 5]

flag = False
for i in x:
    if flag is False:
        for z in y:
            if i == z:
                flag = True
                break
    else:
        break
if flag is True:
    print("Тут э збіжності")
else:
    print("Тут немає збіжностів")
print("Task 5")
a = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
passengers = 0
for i in a:
    passengers += i[0]
    passengers -= i[1]
print(f"Ці пасажири сонні")