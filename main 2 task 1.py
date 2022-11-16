print("Ссновні Задачі 2, Завдання 1")
print("RPG-гра надає можливість гравцю обрати расу героя: аргоніанін, бретонець, альтмер, норд, данмер, каджит. Окрім вибору раси, користувач має можливість налаштувати зовнішність вибраного героя: стать, колір шкіри, маса тіла, татуювання, колір волосся (якщо у раси воно існує). Написати програму для відображення всіх характеристик створеного героя.:")
print()

#let's go!

from datetime import datetime, date
from random import randint
from json import dump, load, loads

#Appearance (Зовнішній вигляд)

class BaseAppearance:
    def __init__(self, sex, weight, skin_color, tattoo, hair_color=None):
        if sex.lower() != "man" and sex.lower() != "woman":
            raise ValueError("Incorrect sex!")

        if weight <= 0:
            raise "Incorrect weight!"
        self.sex = sex
        self.weight = weight
        self.skin_color = skin_color
        self.tattoo = tattoo

        try:
            super().__init__(hair_color)
        except:
            self.hair_color = None


    def add_appearance(self):
        base_appearance = f"Race: {self.__class__.__name__}, " \
                          f"sex: {self.sex}, weight: {self.weight}, " \
                          f"skin color: {self.skin_color}, " \
                          f"tattoo: {self.tattoo}"

        if self.hair_color != None:
            base_appearance += f"; hair color: {self.hair_color}"
        return base_appearance


class HairColor:
    def __init__(self, hair_color):
        self.hair_color = hair_color


    def add_hair_color(self):
        return self.hair_color


# Race of the Hero (Раса Героя)

class Argonianine(BaseAppearance):
    def __str__(self):
        return f"{self.add_appearance()}"


class Breton(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Altmer(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class North(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Dunmer(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Kajit(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"

print("Вітаємо Вас у RPG-грі! Виберіть расу Героя із вибраних (english) ")
print()
print("Argonianine, Breton, Altmer, North, Dunmer, Kajit")
print()
print("Введіть расу героя: ")
