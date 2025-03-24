# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!") 
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}!")
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre=input("Escribe tu nombre: ")
apellido=input("Escribe tu apellido: ")
edad=input("Escribe tu edad: ")
pais=input("Ingresa tu pais de nacimiento: ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y soy de {pais} ")
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro
import math
radio=float(input("Introduce el radio del circulo: "))
area=math.pi*radio*2
perimetro=2*math.pi*radio
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos= int(input("Escribe segundos: "))
horas=segundos/3600
print(f"Esa cantidad de segundos equivalen a {horas:.2f} Hs.")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero=int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar de {numero}")
for i in range (1,10):
    print(f"{numero}*{i}={numero*i}")
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
a=0
b=0
while a==0:
    a=int(input("Introduce el primer num distinto de 0: "))
    if a==0:
        print("El numero debe ser distinto de 0.")
while b==0:
    b=int(input("Introduce el primer num distinto de 0: "))
    if b==0:
        print("El numero debe ser distinto de 0.")
suma=a+b
resta=a-b
multiplicacion=a*b
division=a/b
print(f"La suma de {a} y {b} es {suma}")
print(f"La resta de {a} y {b} es {resta}")
print(f"La multiplicacion de {a} y {b} es {multiplicacion}")
print(f"La division de {a} y {b} es {division}")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2
altura=float(input("Escriba su altura en m: "))
peso=int(input("Escriba su peso entero en kg: "))
imc=peso/altura**2
print(f"Su IMC es de {imc:.2f}")
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =(9/5) * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
temp=float(input("Escriba la temperatura: "))
far=(9/5)*temp+32
print(f"Su temperatura en Farenheit es {far:.2f}")
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números
a=float(input("Escriba un num: "))
b=float(input("Escriba un num: "))
c=float(input("Escriba un num: "))
prom=(a+b+c)/3
print(f"Su promedio es de {prom}")