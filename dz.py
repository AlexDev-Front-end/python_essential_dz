""" 
Завдання 1

Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
"""

class Car:
    def __init__(self, brand:str, model:str, year:int, power:int, color:str, max_speed:int):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__power = power
        self.__color = color
        self.__max_speed = max_speed
        
        
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_power(self):
        return self.__power
    
    def get_color(self):
        return self.__color

    def get_max_speed(self):
        return self.__max_speed
    
    def set_power(self, power):
        if power > self.__power:
            self.__power = power

    def set_color(self, color):
        if color != self.__color:
            self.__color = color

    def car_info(self):
        return f"Марка: {self.__brand}, Модель: {self.__model}, Рік: {self.__year}, Потужність двигуна: {self.__power} к/с, Колір: {self.__color}, Максимальна швидкість: {self.__max_speed} км/год"


car1 = Car('BMW', 'X3', 2013, 306, 'Сірий', 280)
print(car1.car_info())

""" 
Завдання 2

Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).
"""

class English:
    def greeting(self):
        return "Hello, friend!"


class Ukrainian:
    def greeting(self):
        return "Привіт друже!"

    
english_greeting = English()
ukrainian_greeting = Ukrainian()


def hello_friend(English, Ukrainian):
    print(f'{English.greeting()}\n{Ukrainian.greeting()}')

hello_friend(english_greeting, ukrainian_greeting)


""" 
Завдання 3

Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.
"""

class Temperature:
    def __init__(self, cel=0) -> float:
        self._cel = cel  # Внутрішнє збереження температури в Цельсії

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, value:float):
        self._cel = value

    @property
    def far(self):
        return self._cel * 9 / 5 + 32

    @far.setter
    def far(self, value:float):
        self._cel = (value - 32) * 5 / 9
        
temp = Temperature()

temp.cel = 25
print("Цельсії:", temp.cel)
print("Фаренгейти:", temp.far)

temp.far = 98.6
print("Цельсії:", temp.cel)

        
        
""" 
Завдання 4

Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.
"""

class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")

class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")

Base.method()
Child.method()


""" 
Завдання 5

Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами. В результаті повинно з’явитися зображення. Перегляньте їх.
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

