import math

def area(base, height):
    '''(number, number) -> float

    Return the Area of Triangle by calculating
    using base and height of triangle.

    >>> area(20,12)
    120.0
    '''
    return base * height / 2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the Perimeter of a triangle by
    taking the length of three sides.

    >>> perimeter(3,4,5)
    12.0
    '''
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the semiperimeter of triangle by
    taking in the output of perimeter function.
    
    >>> semiperimeter(3,4,5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1, side2, side3) / 2

def area_hero(side1, side2, side3):
    '''(number, number, number) -> float

    Return the area of triangle using Heron's Formula.
    
    >>> area_hero(3, 4, 5)
    6.0
    >>> area_hero(10.5, 6, 9.3)
    27.73168584850189
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1)*(semi - side2)*(semi - side3))
    return area
