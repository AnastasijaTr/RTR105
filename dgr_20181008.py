Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> x =12.2
>>> y = 14
>>> x
12.2
>>> y
14
>>> x = 100
>>> x
100
>>> x + y
114
>>> x * y
1400
>>> x1q3z9ocd = 35.00
>>> a

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 	a = 35.0
	
  File "<pyshell#11>", line 1
    a = 35.0
    ^
IndentationError: unexpected indent
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * (1 -x)
>>> x = 0.6
>>> x = 3.9 * x * (1 - x)
>>> x = 0.6
>>> x(0,6)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x(0,6)
TypeError: 'float' object is not callable
>>> x = 3.9 * x * ( 1 - x )
>>> x = 0.6
>>> x(0,6)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x(0,6)
TypeError: 'float' object is not callable
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> jj = 23
>>> kk % 5

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    kk % 5
NameError: name 'kk' is not defined
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> x = 1 + 2 * 3 -4 / 5 ** 6
>>> x
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> x
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello'+ 'there'
>>> print(eee)
hellothere
>>> eee = 'hello' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10 / 2)
5
>>> print(9 / 2)
4
>>> print(99 /100)
0
>>> print(99 / 100)
0
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> type(ival + 1)
<type 'int'>
>>> print(ival +1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you?')
Who are you?print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1
    print('Welcome', nam)
        ^
SyntaxError: invalid syntax
>>> Who are you?
SyntaxError: invalid syntax
>>> Who are you? Chuck
SyntaxError: invalid syntax
>>> inp = input('Europe floor?')
Europe floor?

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    inp = input('Europe floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    usf = int(inp) + 1
NameError: name 'inp' is not defined
>>> print('US floor', usf)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print('US floor', usf)
NameError: name 'usf' is not defined
>>> Europe floor? 0
SyntaxError: invalid syntax
>>> inp = input('Europe floor?')
Europe floor? 0
>>> usf = int(inp) + 1
>>> print('Us floor', usf)
('Us floor', 1)
>>> 
