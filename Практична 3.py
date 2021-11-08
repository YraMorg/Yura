print("Завдання 1")
print("")
for number in range(1, 10):
    if number % 1 == 0:
        print(number)
print("")
print("Завдання 2")
for number in range(9, 0, -1):
    if number % 1 == 0:
        print(number)
print("")
print("Завдання 3")
start, end = 5, 13
for number in range(start, end + 1):
    if number % 2 != 0:
        print(number, end=" ")
print("")
print("Завдання 4")
num_str = input("Впишіть будь-яке число окрім нуля 0: ")
num_int=int(num_str)
even_count=0
odd_count=0
even_sum=0
odd_sum=0

while num_int !=0:
   num_str = input("Впишіть будь-яке число,окрім нуля 0: ")
   num_int=int(num_str)
for num_int in num_str:
        if num_int == 0:
            print("Помилка")

print("")
print("Завдання 5")
n1 = input("Впишіть число: ")
n_list = list(n1)
n_list.reverse()
n2 = "".join(n_list)
print(n2)
print("")
print("Завдання 6")
n = int(input("Впишіть число:"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)