from abc import ABC, abstractmethod
import math

pi = math.pi


class Shape(ABC):
    def __init__(self, color='Black'):
        self.__color = color
        self.area = 0

    def __add__(self, other):
        if self.area != 0 and other.area != 0:
            return self.area + other.area
        else:
            self.calculate_area()
            other.calculate_area()
            return self.area + other.area

    def __sub__(self, other):
        if self.area != 0 and other.area != 0:
            return self.area - other.area
        else:
            self.calculate_area()
            other.calculate_area()
            return self.area - other.area

    def __eq__(self, other):
        if self.area == 0 or other.area == 0:
            self.calculate_area()
            other.calculate_area()
            return self.area == other.area
        else:
            return self.area == other.area

    def color(self):
        return self.__color

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, height, color='Black'):
        super().__init__(color=color)
        self.length = length
        self.height = height
        self.__color = color

    def calculate_area(self):
        self.area = self.length * self.height


class Triangle(Shape):
    def __init__(self, length, height, color='Black'):
        super().__init__(color=color)
        self.length = length
        self.height = height
        self.__color = color

    def calculate_area(self):
        self.area = self.length * self.height / 2


class Circle(Shape):
    def __init__(self, radius, color='Black'):
        super().__init__(color=color)
        self.radius = radius
        self.__color = color

    def calculate_area(self):
        self.area = pi * self.radius ** 2

rectangle_1 = Rectangle(15, 20, 'Green')
triangle_1 = Triangle(30, 21)
circle_1 = Circle(45, 'Orange')
