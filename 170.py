# Autors:
# Apliecibas numurs : 
# Datums : 2018.11.26
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

#-*- coding : utf -8 -*-

from math import sin, fabs
from time import sleep

def f(x) :
    return sin(x)

# Definejam argumenta x robežam:
a = 1.1
b = 3.2

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Parbaudam, vai dotajaa intervalaa ir saknes:
if ( funa* funb > 0.0):
    print "Dotajaa intervala [%s, %s] saknu nav"%(a, b)
    sleep(1); exit() # Zinjo uz ekrana, gaida 1 sec. un darbu pabeidz
else:
    print "Dotajaa intervalaa sakne ir!"

# Defineejam precizitaati , ar kaadu mekleesim sakni :
deltax = 0.01

# Sashaurinam saknes mekleeshanas robezhas :
while (fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0. ):
        b = x
    else:
        a = x


print "Sakne ir :", x


