Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
hello
fun
zip

Traceback (most recent call last):
  File "/home/user/RTR105/test_18_10.py", line 6, in <module>
    things()
NameError: name 'things' is not defined
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
hello
fun
zip
hello
fun
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
>>> big = max('hello world')
>>> print(big)
w
>>> tiny = min('hello world')
>>> print(tiny)
 
>>> 
>>> print(float(99)/100)
0.99
>>> i = 42
>>> type(i)
<type 'int'>
>>> f - float(i)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    f - float(i)
NameError: name 'f' is not defined
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1 + 2 * float(3)/4 - 5)
-2.5
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
hello
yo
7
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
('Hello', 'sally')
>>> def greet(lang)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def greet(lang):
	if lang == 'es'
	
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == 'es':
		return 'hola'
	elif lang == 'fr'
	
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == 'es':
		return 'hola'
	elif lang == 'fr':
		return 'bonjour'
	else:
		return 'hello'

	
>>> print(greet('en'),'glenn')
('hello', 'glenn')
>>> print(greet('es'),'sally')
('hola', 'sally')
>>> print(greet('fr'),'michael')
('bonjour', 'michael')
>>> 
================== RESTART: /home/user/RTR105/test_18_10.py ==================
8
>>> big = max('hello world')
>>> print(big)
w
>>> 
