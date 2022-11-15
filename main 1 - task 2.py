print("Main 1, Task 2")
print("  Створіть клас Rectangle. Для ініціалізації атрибутів-даних класу – довжини і ширини прямокутника – використовуйте метод __init __ () з аргументами за замовчуванням. Передбачити можливість визначення периметра і площі прямокутника. Доступ до атрибутів-даних повинен бути контрольований (довжину і ширину прямокутника обмежити 100 см). Для демонстрації функціоналу класу Rectangle створіть консольний додаток.")
print()
class Rectangle:
    def __init__(self, width=80, height=60):
        if width <= 0 or height <= 0:
            raise ValueError("Side cannot be equal to or less than 0")
        self.width = Rectangle.limit_side(width)
        self.height = Rectangle.limit_side(height)

    MAX_SIZE = 100

    @classmethod
    def limit_side(cls, side):
        if side > cls.MAX_SIZE:
            return cls.MAX_SIZE
        return side


    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return f"{perimeter} cm"


    def get_square(self):
        square = self.width * self.height
        return f"{square} cm²"


    def __str__(self):
        return f"Perimeter: {self.get_perimeter()};" \
               f"square: {self.get_square()}"
    
print("Введіть(enter)")
