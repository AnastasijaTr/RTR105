Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> original = "To be or not to be"
>>> type(original)
<type 'str'>
>>> len(original)
18
>>> original[0]
'T'
>>> key = 10
>>> original[0] ^ key

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    original[0] ^ key
TypeError: unsupported operand type(s) for ^: 'str' and 'int'
>>> ord(original[0]_)
SyntaxError: invalid syntax
>>> ord(original[0])
84
>>> bin(ord(original[0]))
'0b1010100'
>>> ord(original[0]) ^key
94
>>> chr(ord(original[0]) ^key)
'^'
>>> 
>>> (ord(original[0]) ^key) ^ key
84
>>> chr(ord(original[0]) ^key) ^ key)
SyntaxError: invalid syntax
>>> chr((ord(original[0]) ^key) ^ key)
'T'
>>> original
'To be or not to be'
>>> key
10
>>> N = len(original)
>>> N
18
>>> message = []
>>> for i in range(N):
	message.append(ord(original[1]) ^key))
	
SyntaxError: invalid syntax
>>> for i in range(N):
	message.append(ord(original[1]) ^key)

	
>>> 
>>> 
>>> original
'To be or not to be'
>>> message
[101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101]
>>> message = ''
>>> for i in range(N)
SyntaxError: invalid syntax
>>> message = ''
>>> for i in range(N):
	message = message + (chr(ord(original[i]) ^key))

	
>>> message
'^e*ho*ex*de~*~e*ho'
>>> 
>>> 
>>> result = ''
>>> key1 = 45
>>> for i in range(N):
	message = message + (chr(ord(original[i]) ^key1))

>>> result
''
>>> result = ''
for i in range(N):
	result = result + (chr(ord(original[i]) ^key1))
	
>>> result
''
>>> result = ''
>>> for i in range(N):
	result = result + (chr(ord(original[i]) ^key1))

>>> result
'yB\rOH\rB_\rCBY\rYB\rOH'
>>> key1 = key
>>> result = ''
>>> for i in range(N):
	result = result + (chr(ord(message[i]) ^key1))

	
>>> result
'To be or not to be'
>>> original
'To be or not to be'
>>> key
10
>>> key1 = 45
>>> message = ''
for i in range(N):
	message = message + (chr(ord(original[i]) ^key))
	
>>> message
''
>>> for i in range(N):
	message = message + (chr(ord(original[i]) ^key))

	
>>> message
'^e*ho*ex*de~*~e*ho'
>>> result = ''
>>> for i in range(N):
	result = result + (chr(ord(message[i]) ^key1))

	
>>> result
'sH\x07EB\x07HU\x07IHS\x07SH\x07EB'
>>> key1 = key
>>> result = ''
>>> for i in range(N):
	result = result + (chr(ord(message[i]) ^key1))

	
>>> result
'To be or not to be'
>>> 
