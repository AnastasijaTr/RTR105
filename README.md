# RTR105
Datormācibas kursa elektroniskā klade  
**Ctrl+Shit+T** - atvert jauno user  
**Tab** - visas komandas( jāatkarto 2 reizes)  
_Piemeram_   
burts _-u-_ Tab  visas komandas, kuri sākas uz -u- burtu  
**Ctrl+L** - ekrans tīrs viss no jauna  
**q** - iziet  
**Ctrl+Alt+F1(F2,F3...)** - teletypwriter vai TTY  
**F7** - parasta versija  
**pwd** - adrese lokala stacija  
**ls** - saraksts
**chmod** - izmainīt  
**mkdir** - jauna mape  
**rmdir** - dzest mapi  
**man rm** - dzeš failus
**cp** - copy  
**mv** - parvietot
**=** pieškiršanas objekts  
**cd** jāiet mapē  
**cat** - lasīt  

**Skript**  
_Piemeram_  
mkdir Mape  
cd Mape  
mkdir MapeMape  
**echo $PATH** - lai varētu stradāt Tab  

**python**  
vars() - kas ir piejams  
__builtins__ - iebuvēti objekti  
__doc__ - objekta apraksts  
_Piemers_  
a = 10 - integer( jo bez zīmem)  
b = 2,45 - float( ar komatiem)  
c = 'R' - str  
Skripts - fails  
Ctrl+k - copy  
Ctrl+u - paste  
  
PY4E  
**idle**  
'''  
Piemers nozime lai saglabāt  
'''  
x = 42  
if x > 1:  
   print('More that one')  
   if x < 100:  
      print('Less than 100')
print('All done')  


  
x = 4  
if x > 2:  
   print('Bigger')  
else:  
    print('Smaller')  
print('All done')  


**Nosacijuma oporats**  
if (nosacijums):  

elif pieder if  
elif (nosacijums):  
    vismaz viena darbība  

if (...):  
    ....  
elif (...):  
    ....  
else:
    vismaz viena darbība  

**Funkcijas**  
def funkcijas vards(vieta argumentam):
    vismaz viena darbība  
    return mainigais  
**return**- ja kautko planojat atgriezt 


**Loops and iterations**(Cikli)  
1)While(tikmēr, kamēr)  
while nosacijums:  
    vismaz viena darbība  
cikla partraukuma vards -**break**(vispar)  
**continue**- partrauk darbību un atgriežas pie nosacijuma    
2)for cikla mainigais in skaitlis:  
    vismaz viena darbība  
continue> nakamais elements saraksta  
break> no cikla for arā  

n = 5  
while n > 0:
      print(n)
      n = n - 1  
print('Blastoff!') 
print(n)  
>>>>>>>  
5  
4  
3  
2  
1  
Blastoff!  
0  
>>>>>>>>  
n = 5   
while n > 0
      print('A')  
      print('B')  
print('Dry off')  
>>>>>>>>>>>>>>
A  
B  
A  
B  
un tā bus bezgalīgi, jo n nemainas un visu laiku ir vairāk neka nulle  
>>>>>>>>>>>>>>>>>>>>>>>>>>  

**Strings**
len - cik ir burtu vardā  
_Piemērs_  
>friut = 'banana'  
>print(len(fruit))  
6  

Monty Pyth o n    
01234567891011  
>s = 'Monty Python'  
>print(s[0:4])  
Mont  
>print(s[6:7])  
P  
>print(s[6:20])  
Python  
>print(s[:2])  
Mo  
>print(s[8:])  
thon  
>print(s[:])  
Monty Python  


.lower() - visi burti ar maziem burtiem  
.upper() - visi burti ar LIELAM burtiem  
.lstrip() - kreisā puses    
.rstrip() - labā puse  
.strip() - pa vidu

_Piemērs, lai butu atstarpe_  
> a = 'hello'  
> b = a + 'there'  
> print(b)  
hellothere  
> c = a + ' ' + 'there'  
> print(c)  
hello there 

**Files**  

