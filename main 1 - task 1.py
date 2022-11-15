print("Main 1, Task 1")
print("Створіть клас Rational для виконання арифметичних операцій з раціональними числами. Для ініціалізації атрибутів-даних класу - чисельника і знаменника - використовуйте метод __init __ () з аргументами за замовчуванням для випадку, якщо початкові значення чисельника і знаменника не надані.Раціональне число в пам'яті повинно зберігатися в скороченій формі, наприклад, дріб 2/4 повинна зберігатися як 1 в чисельнику і 2 в знаменнику. Передбачити можливість виведення раціональних чисел у форматі a / b, де a - чисельник,b - знаменник і в форматі з плаваючою комою. Для демонстрації функціоналу класу Rational створіть консольний додаток.")
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


print("Введіть приклад(enter example (+,/,*,-)")
