x = float(input("4 цілих числа = "))
print("{:3d}".format(int(x)))
print()
b = float(input("Numbers = "))
print("{:10f}".format(float(b)))
print()
с = float(input("Numbers = "))
print(f"{с:5.2f}")
print()
d = str(input("Введіть 4 символи:"))
(len(d))
if len(d) > 4:
    print("False")
elif len(d) < 4:
    print("False")
elif len(d) == 4:
    print("True")