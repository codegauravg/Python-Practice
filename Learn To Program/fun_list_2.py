Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> colours = []
>>> prompt = 'Enter another one of your favourite colours(Type return to end)'
>>> colour = input(prompt)
Enter another one of your favourite colours(Type return to end)
>>> colour
''
>>> colour = input(prompt)
Enter another one of your favourite colours(Type return to end)Blue
>>> colours
[]
>>> colour
'Blue'
>>> while colour != '':
	colours.append(colour)
	colour = input(prompt)

	
Enter another one of your favourite colours(Type return to end)yello
Enter another one of your favourite colours(Type return to end)brown
Enter another one of your favourite colours(Type return to end)
>>> colours.extend(['hot pink', 'neon green'])
>>> colours
['Blue', 'yello', 'brown', 'hot pink', 'neon green']
>>> colours.pop()
'neon green'
>>> colours
['Blue', 'yello', 'brown', 'hot pink']
>>> colours.pop(2)
'brown'
>>> colours
['Blue', 'yello', 'hot pink']
>>> colours.remove('black')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    colours.remove('black')
ValueError: list.remove(x): x not in list
>>> if colours.count('yello') > 0:
	colours.remove('yello')

	
>>> colours
['Blue', 'hot pink']
>>> if 'yellow' in colours:
	colours.remove('yellow')

	
>>> colours
['Blue', 'hot pink']
>>> colours.extend('auburn', 'taupe', 'magenta')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    colours.extend('auburn', 'taupe', 'magenta')
TypeError: extend() takes exactly one argument (3 given)
>>> colours.extend(['auburn', 'taupe', 'magenta'])
>>> colours
['Blue', 'hot pink', 'auburn', 'taupe', 'magenta']
>>> colours.sort()
>>> colours
['Blue', 'auburn', 'hot pink', 'magenta', 'taupe']
>>> colours.pop(0)
'Blue'
>>> colours.extend('blue')
>>> colours.sort()
>>> colour
''
>>> colours
['auburn', 'b', 'e', 'hot pink', 'l', 'magenta', 'taupe', 'u']
>>> colours.pop(1,2,4,7)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    colours.pop(1,2,4,7)
TypeError: pop() takes at most 1 argument (4 given)
>>> colours.pop(1)
'b'
>>> colours.pop(2)
'hot pink'
>>> colours.pop(4)
'taupe'
>>> colours.pop(7)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    colours.pop(7)
IndexError: pop index out of range
>>> colours.extend(['blue'])
>>> colours.sort()
>>> colours
['auburn', 'blue', 'e', 'l', 'magenta', 'u']
>>> colours.reverse()
>>> colours
['u', 'magenta', 'l', 'e', 'blue', 'auburn']
>>> colours.insert(-2, 'brown')
>>> colours
['u', 'magenta', 'l', 'e', 'brown', 'blue', 'auburn']
>>> colours.index('neon green')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    colours.index('neon green')
ValueError: 'neon green' is not in list
>>> if 'hot pink' in colours:
	where = colours.index('hot pink')
	colours.pop(where)

	
>>> 
