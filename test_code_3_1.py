import unittest
from code_3_1 import Rectangle, Triangle, Circle


class TestShape(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(15, 20)
        self.triangle = Triangle(30, 21)
        self.circle = Circle(45)
        self.rectangle_1 = Rectangle(15, 20)
        self.triangle_1 = Triangle(30, 21)
        self.circle_1 = Circle(45)
        self.rectangle_2 = Rectangle(4, 6, 'Red')

    def test_add(self):
        rectangle = self.rectangle.__add__(self.triangle)
        self.assertEqual(rectangle, 615)
        rectangle = self.rectangle.__add__(self.circle)
        self.assertEqual(rectangle, 6661.725123519331)
        triangle = self.triangle.__add__(self.rectangle)
        self.assertEqual(triangle, 615)
        triangle = self.triangle.__add__(self.circle)
        self.assertEqual(triangle, 6676.725123519331)
        circle = self.circle.__add__(self.rectangle)
        self.assertEqual(circle, 6661.725123519331)
        circle = self.circle.__add__(self.triangle)
        self.assertEqual(circle, 6676.725123519331)

    def test_sub(self):
        rectangle = self.rectangle.__sub__(self.triangle)
        self.assertEqual(rectangle, -15)
        rectangle = self.rectangle.__sub__(self.circle)
        self.assertEqual(rectangle, -6061.725123519331)
        triangle = self.triangle.__sub__(self.rectangle)
        self.assertEqual(triangle, 15)
        triangle = self.triangle.__sub__(self.circle)
        self.assertEqual(triangle, -6046.725123519331)
        circle = self.circle.__sub__(self.rectangle)
        self.assertEqual(circle, 6061.725123519331)
        circle = self.circle.__sub__(self.triangle)
        self.assertEqual(circle, 6046.725123519331)

    def test_eq(self):
        rectangle = self.rectangle.__eq__(self.triangle)
        self.assertEqual(rectangle, False)
        rectangle = self.rectangle.__eq__(self.circle)
        self.assertEqual(rectangle, False)
        triangle = self.triangle.__eq__(self.rectangle)
        self.assertEqual(triangle, False)
        triangle = self.triangle.__eq__(self.circle)
        self.assertEqual(triangle, False)
        circle = self.circle.__eq__(self.rectangle)
        self.assertEqual(circle, False)
        circle = self.circle.__eq__(self.triangle)
        self.assertEqual(circle, False)
        rectangle = self.rectangle.__eq__(self.rectangle_1)
        self.assertEqual(rectangle, True)
        triangle = self.triangle.__eq__(self.triangle_1)
        self.assertEqual(triangle, True)
        circle = self.circle.__eq__(self.circle_1)
        self.assertEqual(circle, True)

    def test_color(self):
        rectangle = self.rectangle.color()
        self.assertEqual(rectangle, 'Black')
        triangle = self.triangle.color()
        self.assertEqual(triangle, 'Black')
        circle = self.circle.color()
        self.assertEqual(circle, 'Black')
        rectangle_2 = self.rectangle_2.color()
        self.assertEqual(rectangle_2, 'Red')

unittest.main()
