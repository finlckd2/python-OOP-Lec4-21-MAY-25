import math
from typing import override


class Circle:

    pie=3.14#static property

    def __init__(self, _radius):
        self.__radius = _radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    @override
    def __str__(self):
        return f"Circle radius is:{self.__radius}"
