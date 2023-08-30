#Elaborado por: Daniel Campos y Alejadro Madrigal
#Creación: 28/08/2023 9:48 am
#Ult mod: 28/08/2023 
#Versión 3.10.6
from Funciones import *
#funciones de entrada y salida, con validaciones
#1
def compararDigitosAux(n1,n2):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n1 y n2
    S: Función seleccionada
    """
    if isinstance(n1 and n2,int)==True:
        compararDigitos(n1,n2)
        if n1<=0 and n2<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""
    
def opcioncompararDigitos(n1,n2):
    """
    F: Entrada y salida de datos de la funcion comparar dígitos
    E: Número n1 y n2
    S: Dígitos del número n que son pares
    """
    while True:
        try:
            print("Comparar dígitos y números.")
            n1=int(input('Digite un numero entero positivo: '))
            n2=int(input('Digite otro numero entero positivo: '))
            return  print(compararDigitosAux(n1,n2))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 

#2
def opcioncontarRepetidosAux(n, buscar):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n1 y n2
    S: Función seleccionada
    """
    if isinstance(n and buscar,int)==True:
        contarRepetidos(n, buscar)
        if n<=0 and buscar<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""

def opcioncontarRepetidos(n, buscar):
    """
    F: Entrada y salida de datos de la funcion 
    E: Número n1 y n2
    S: Dígitos del número n que son pares
    """
    while True:
        try:
            print("¿Cuántas veces aparece un dígito en una cifra entera?")
            n=int(input('Digite un número entero positivo: '))
            buscar=int(input('Número a buscar: '))
            return  print(opcioncontarRepetidosAux(n, buscar))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 

#3
def opcionindicarSumaAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        indicarSuma(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""

def opcionindicarSuma(n):
    """
    F: Entrada y salida de datos de la función 
    E: Número n
    S: Cifra del número n más grande
    """
    while True:
        try:
            print("Suma de los dígitos.")
            n=int(input('Digite un numero entero positivo: '))
            return print(opcionindicarSumaAux(n))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 
        
#4
def opcionrevisarBinarioAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        revisarBinario(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""

def  opcionrevisarBinario(n):
    """
    F: Entrada y salida de datos de la función 
    E: Número n
    S: Cifra del número n más grande
    """
    while True:
        try:
            print("Saber si un número es binario.")
            n=int(input('Digite un numero entero positivo: '))
            return print(opcionrevisarBinarioAux(n))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 

#5
def opcionverificarParidadAux(n, posicion):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n1 y n2
    S: Función seleccionada
    """
    if isinstance(n and posicion,int)==True:
        verificarParidad(n, posicion)
        if n<=0 or posicion<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""

def opcionverificarParidad(n, posicion):
    """
    F: Entrada y salida de datos de la funcion 
    E: Número n1 y n2
    S: Dígitos del número n que son pares
    """
    while True:
        try:
            print("Verificar la paridad de un dígito en una posición dada.")
            n=int(input('Número entero: '))
            posicion=int(input('Posición a buscar: '))
            return  print(opcionverificarParidadAux(n, posicion))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n")    

#6
def opcionreconocerPalindromoAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        reconocerPalindromo(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""

def  opcionreconocerPalindromo(n):
    """
    F: Entrada y salida de datos de la función 
    E: Número n
    S: Cifra del número n más grande
    """
    while True:
        try:
            print("Saber si un número es palíndromo.")
            n=int(input('Digite un numero entero positivo: '))
            return print(opcionreconocerPalindromoAux(n))
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 

#menu
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    n=posicion=n1=n2=buscar=0
    print ("1. Comparar dígitos y números.")
    print ("2. ¿Cuántas veces aparece un dígito en una cifra entera?")
    print ("3. Suma de los dígitos.")
    print ("4. Saber si un número es binario.")
    print ("5. Verificar la paridad de un dígito en una posición dada.")
    print ("6. Saber si un número es palíndromo.")
    print ("0. Terminar")
    while True:
        try:
            opcion=int(input ("Escoja una opción: "))
            if opcion>=0 and opcion<=12:
                if opcion==1:
                    opcioncompararDigitos(n1,n2)
                elif opcion==2:
                    opcioncontarRepetidos(n, buscar)
                elif opcion==3:
                    opcionindicarSuma(n)
                elif opcion==4:
                    opcionrevisarBinario(n)
                elif opcion==5:
                    opcionverificarParidad(n, posicion)
                elif opcion==6:
                    opcionreconocerPalindromo(n)
                else:
                    return
            else:
                return print ("Opción inválida")
        except:
            return print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n") 
    
def menuAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Opción del menú seleccionada
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        menu(n)
    else: 
        return "Debe ingresar sólo números."
    return ""

#programa principal
menu()