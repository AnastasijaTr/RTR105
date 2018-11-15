import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 11)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, color="#CC1111")

y1 = x
y2 = y1 - x**3/(3*2*1)
y3 = y2 + (x**5)/(5*4*3*2*1)
y4 = y3 -(x**7)/(7*6*5*4*3*2*1)

plt.plot(x, y1, color="#AAAAAA")
plt.plot(x, y2, color="#089500")
plt.plot(x, y3, color="#0895ac")
plt.plot(x, y4, color="#A246FC")

while x < 0.01

plt.show()

