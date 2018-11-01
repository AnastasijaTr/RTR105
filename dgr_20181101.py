Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fhand = open('tekst')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fhand = open('tekst')
IOError: [Errno 2] No such file or directory: 'tekst'
>>> print(fhand)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(fhand)
NameError: name 'fhand' is not defined
>>> stuff = 'Heloo\nWorld!'
>>> stuff
'Heloo\nWorld!'
>>> print(stuff)
Heloo
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> open()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    open()
TypeError: Required argument 'name' (pos 1) not found
>>> fhand = open('text.txt')

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fhand = open('text.txt')
IOError: [Errno 2] No such file or directory: 'text.txt'
>>> 
================== RESTART: /home/user/RTR105/test_01_11.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/test_01_11.py", line 1, in <module>
    xfile = open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> 
================== RESTART: /home/user/RTR105/test_01_11.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/test_01_11.py", line 1, in <module>
    xfile = open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> 
