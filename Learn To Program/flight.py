Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/Gaurav Gunjan/Documents/Python Scripts/triangle.py ====
>>> area(20, 12)
120.0
>>> perimeter(10+23+17)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    perimeter(10+23+17)
TypeError: perimeter() missing 2 required positional arguments: 'side2' and 'side3'
>>> perimeter(10,23,17)
50
>>> 'hello'
'hello'
>>> 'hello' + 'brother'
'hellobrother'
>>> 'hello ' + 'brother'
'hello brother'
>>> "Hello buddy, How are you?"
'Hello buddy, How are you?'
>>> puzzle_start = 'I want to be your'
>>> punctuation = '!'
>>> noun = 'earthworm'
>>> puzzle_start + noun + punctuation
'I want to be yourearthworm!'
>>> puzzle_start = 'I want to be your '
>>> puzzle_start + noun + punctuation
'I want to be your earthworm!'
>>> ('Bwa' + 'ha')* 9
'BwahaBwahaBwahaBwahaBwahaBwahaBwahaBwahaBwaha'
>>> 
== RESTART: C:/Users/Gaurav Gunjan/Documents/Python Scripts/temperature.py ==
>>> convert_to_celsius(32)
0.0
>>> convert_to_celsius(212)
100.0
>>> 
==== RESTART: C:\Users\Gaurav Gunjan\Documents\Python Scripts\triangle.py ====
>>> semiperimeter(3,4,5)
6.0
>>> help(semiperimeter)
Help on function semiperimeter in module __main__:

semiperimeter(side1, side2, side3)
    (number, number, number) -> float
    
    Return the semiperimeter of triangle by
    taking in the output of perimeter function.
    
    >>> semiperimeter(3,4,5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9

>>> max(area(3.8,7),area(3.5,6.8))
13.299999999999999
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(math.log)
Help on built-in function log in module math:

log(...)
    log(x[, base])
    
    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.

>>> 
==== RESTART: C:\Users\Gaurav Gunjan\Documents\Python Scripts\triangle.py ====
>>> area_hero(3,4,5)
6.0
>>> import math
>>> area_hero(3,4,5)
6.0
>>> area_hero(10.5, 6, 9.3)
27.73168584850189
>>> 
