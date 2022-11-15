print("Завдання 1")
print()
class Rational:
    def __init__(self, numberator=4, denominator=10):
        numberator, denominator = self.reduce_fraction(numberator, denominator)
        self.numberator = numberator
        self.denominator = denominator

    @staticmethod
    def reduce_fraction(numberator, denomunator):
        from math import gcd

        gcd = gcd(numberator, denomunator)
        numberator //= gcd
        denomunator //= gcd
        return numberator, denomunator

    def get_float(self):
        return self.numberator / self.denominator

    def __str__(self):
        return f"{self.numberator}/{self.denominator};" \
               f"float {self.get_float()}"

print("Введіть приклад:")
