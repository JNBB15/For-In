def suma(a, b):
    """Funcion que sirve para sumar dos numeros"""
    print(a+b)
print(suma. __doc__)#Recordatorio que para que imprima la documentacion primero debe ir la documentacion antes que el resto del codigo

website="apple.com"#Asigne una variable
website="programiz.com"#Acabo de reasignar la misma variable

a, b, c="Hola", 1, 2.4#Otra forma de asignar variables
print(a)
print(b)
print(c)

x=y=z="Lo mismo"#Forma de asignar el mismo valor a una variable
print(x)
print(y)
print(z)

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
#Float Literal
float_1 = 10.5
float_2 = 1.5e2
#Complex Literal
x = 3.14j
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is Python"#Las strings no se pueden alterar. No se puede utilizar el [] con ellos
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = (1 == True)#Esto vale 1. O sea que True es igual a 1
y = (1 == False)#Esto vale a 0
a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

Drink="Disponible si es alcohol"
Food=None#Esto es solo para mostrar este caracter que evidencia que algo no se ha creado aun
def Menu(x):
    if x==Drink:
        print(Drink)
    else:
        print(Food)

Fruta=["Manzana", "Pera", "Durazno"]#Lista. Los elementos de una lista pueden ser alterados.
Verdura=(1, 2, 3)#Tupla. Estas no pueden ser alteradas.
Diccionario={'Jesus':'Brasil', 'Edad':22, 'Nacionalidad':'Mexicano'}#Diccionario: Se puede preguntar por la "Llave" no por el "Valor" de esa llave
Vocales={'a', 'e', 'i', 'o', 'u'}#Set. No se pueden repetir valores dentro de los set. Se eliminan los duplicados. No se pueden utilizar el simbolo []

#CONVERSION IMPLICITA
num_int=2
num_float=1.23
nuevo_num=num_int+num_float
print(nuevo_num)#Conversion de un valor de tipo entero a tipo decimales

#CONVERSION EXPLICITA
num_int=3
num_str="23"
num_new=int(num_str)
print(num_new)

print(1, 2, 3, 4, sep="*")
print(1, 2, 3, 4, sep="*", end="&")

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print("My name is {name} , my age is {age}".format(name="Jesus", age=22))
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)

X=input("Enter a number, please: ")#Ejemplo de como pedir algo al usuario mediante el teclado
y=input("Enter another number, please: ")
def suma(x, y):
    print(x+y)

from math import * #Ejemplo de como importar un modulo a el presente archivo
print(pi)

from sys import * #Se supone que con esto puedo importar el directorio de los diferentes modulos y paquetes de Python

#DETALLE: ES IMPORTANTE SABER QUE LAS LISTAS NO SON IGUALES PORQUE EL INTERPRETE DE PYTHON LOS COLOCA EN LUGARES DIFERENTES DE LA MEMORIA

a=2
print(id(a), id(a))#Forma de buscar la ruta en la RAM del objeto 2 con el nombre a, mediante la funcion id
print(id(2), id(2))

#IMPORTANCIA DE USAR EL GLOBAL SI QUEREMOS USAR UNA FUNCION DENTRO DE OTRA FUNCION. O MAS BIEN UNA VARIABLE DENTRO DE ESAS FUNCIONES

#SUPUESTO FUNCIONAMIENTO DE LOS CONDICIONALES IF, ELIF Y ELSE
z=input("Enter a number my dearest bitch: ")

if z==1:
    print("Oh, darling, this is so bad for you")
elif z==2:
    print("Well, this start to looking nice for us")
else:
    print("Babe, theres no I in threesome")

#FUNCIONAMIENTO DE LOS FOR I IN RANGE
lista=[1,2,3,4,5,6,7,8,9]
for i in range(lista):
    i=i+lista

genre=["pop", "rock", "post punk"]
for i in range(len(genre)):
    print("My favourite music genres is ", genre(i))

digits=1, 2, 3, 4
for i in range(digits):
    print(i)
else:
    print("There no more digits")

student_name="Jesus"
students=["Arturo", "Jason", "Omar", "Max"]
for i in range(students):
    if i == student_name:
        print(i(students))
        break
    else:
        print("No entry with that name")

#FUNCIONAMIENTO DE UN BUCLE WHILE
counter=0
while counter<=5:
    print("Estoy dentro de un bucle")
    counter=counter+1
else:
    print("Soy el amo del tiempo")

#FUNCIONAMIENTO DEL BREAK Y DEL CONTINUE
for val in "string":
    if val=="i":
        break
    print(val)
print("This is the end, my only friend")

for letter in "word":
    if letter=="r":
        continue
    print(letter)
print("Now is the end")

#FUNCIONAMIENTO DEL PASS
def nada():
    pass

#FUNCIONES QUE YA SE HAN VISTO
def gracias(nombre):
    """Recuerda que antes de llamar la funcion, debes crear dicha funcion
        Y esto sirve como documentacion"""
    print("Hola" + nombre + "muchas gracias")
print(gracias("Fernando"))
print(gracias.__doc__)

def valores(num):
    """Funcion que trata de mencionarte que numero 
    absoluto elegiste"""
    if num>=0:
        return num
    else:
        return -num
print(valores(2))
print(valores(-4))

def gracias2point0(nombre, mensaje):
    """Funcion con dos argumentos"""
    print("Hello"+nombre+mensaje)
gracias2point0("Jebus", "Chifla o canta o baila")

def gracias3(nm, msg="Buenas tardes"):
    """Funcion que tiene por default, un valor para msg
    , en caso de que no se le de un valor cuando se llama
    la funcion"""
    print("Hola"+nm+msg)
print("Barry")
print("Imani", "Mira detras de ti")

def gracias4(*names):
    """Funcion que engloba los valores dentro
    de una tupla"""
    for name in names:
        print("Hallo", name)
gracias4("Monica", "Richard", "Bertram", "Jared")

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))

#Funcion anonima que se usa para trabajos cortos
funcionlambda=lambda x: x+5
print(funcionlambda(5))

#Ejemplo 2 de una funcion anonima lambda
listilla=[1,3,4,6,8,12,16,20]
nuevalistilla=list(filter(lambda x:(x%2==0), listilla))
print(nuevalistilla)

# Program to double each item in a list using map. Ejemplo 3
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

#EJEMPLO DE UNA VARIABLE GLOBAL CON ACCESO DESDE FUERA Y DENTRO DE UNA VARIABLE
x="global"
def foo():
    print("x inside: ", x)
foo()
print("x outside: ", x)

"""Recordar que cuando se hace una funcion y se define
una variable dentro de la funcion, esta debe ser local.
O sea, no puede llamada desde fuera sin la funcion."""

y="GLOBAL"
def dosvar():
    #ESTA FUNCION COMBINA VARIABLES LOCALES Y GLOBALES. PERO PARA MODIFICAR DICHA VARIABLE DENTRO DE LA FUNCION SE OCUPA PONER GLOBAL
    global y
    z="local"
    y=y*2
    print(y)
    print(z)
dosvar()

def outer():
    """Basicamente, estas son variables locales que
    se pueden modificar en funciones anidadas"""
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

"""HAY UNA PEQUE;A PRACTICA QUE TRATA DE CREAR UN ARCHIVO CONFIG.PY Y GUARDAR
DOS VARIABLES CON DETERMINADO VALOR. LUEGO CREAR UNA CARPETA LLAMADA UPDATE.PY
E IMPORTAR CONFIG.PY PARA REESCRIBIR LOS VALORES DE DICHAS VARIABLES DENTRO DEL
ARCHIVO UPDATE. POR ULTIMO, CREAR UN ARCHIVO LLAMADO MAIN.PY PARA TESTEAR LOS CAMBIOS
DE VALORES. AL CORRER ESTE ARCHIVO, SE MUESTRAN LOS CAMBIOS MAS RECIENTES. DESDE
AHORA, TECNICAMENTE, PUEDES UTILIZAR ESAS VARIABLES EN CUALQUIER ARCHIVO DE TRABAJO
A LO LARGO DE LA CARPETA"""

#IMPORTACION DE MODULOS A OTROS ARCHIVOS
def adicion(a, b):
    """Funcion que suma dos numeros. Esto se puede importar para poder usarse desde otro archivo mediante
    el comando import nombredelarchivo. Se puede usar en otro archivo mediante la escritura nombredelarchivo.adicion(3, 4)"""
    result=a+b
    return result

"""Tambien se pueden importar modulos predefinidos de python como import math. Si quieres importar solo alguna funcion de
dicho modulo, lo haces mediante esto: from math import pi, por ejemplo. O si quieres todas las funciones dentro del modulo,
escribe from math import *"""

import sys
sys.path
dir()#Con esta funcion se puede ver la lista de funciones que estan dentro de un modulo. Con el sys.path se ve la lista de modulos registrados en el path

#DETALLES ACERCA DE LOS STRINGS
"PrOgRaMiZ".lower()
'programiz'
"PrOgRaMiZ".upper()
'PROGRAMIZ'
"This will split all words into a list".split()
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'This will join all words into a string'
'Happy New Year'.find('ew')
7
'Happy New Year'.replace('Happy','Brilliant')
'Brilliant New Year'

#MAS EXPLICACION ACERCA DE LOS SET EN PYTHON
"""Los set son listas sin orden especifico y sin que se puedan cambiar los elementos en ella. Ademas, no permite los duplicados"""

#AHORA VENDRA UNA EXPLICACION ACERCA DE LOS ARCHIVOS Y COMO MANIPULARLOS MEDIANTE COMANDOS EN PYTHON

