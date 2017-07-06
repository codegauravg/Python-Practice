def convert_to_celsius(fahrenheit):
    '''
    (number) -> float

    Return Celsius equivalent to fahrenheit.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5/9
