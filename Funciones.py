#Elaborado por: Daniel Campos y Alejadro Madrigal
#Creación: 28/08/2023 Hora: 8:37 am
#Ult mod: 
#Versión 3.10.6

#def funciones
#contar dígitos 0
def contarDigitos(n):
    """
    Función: Cuenta los dígitos de un número entero
    Entrada: Número entero
    Salida: Cantidad de dígitos
    """
    contador=0
    while n!=0:
        if n%10 !=0:
            contador+=1
        n//=10
    return contador
    
#funcion: comparar dígitos y números 1
def compararDigitos(n1,n2):
    """
    Función: Compara si los números enteros colocados son igual en tamaño y en valor
    Entrada: Dos números enteros
    Salida: Comparador
    """
    contador1=0
    contador2=0
    num1=n1
    num2=n2
    while num1!=0:
        if num1%10!=0: 
            contador1+=1
        num1//=10
    while num2!=0:
        if num2%10!=0:
            contador2+=1
        num2//=10
    if contador1==contador2:
        if n1!=n2:
            return print("Los números no son iguales.")
        else:
            return print("Los números son iguales.")
    else:
        return print("Los dígitos de los números no son iguales.")

#funcion: cuántas veces aparece un dígito en una cifra entera 2
def contarRepetidos (n, buscar):
    """
    Función: Busca un dígito de un número que se coloca
    Entrada: Número entero y número a buscar
    Salida: Contador o respuesta.
    """
    contador=0
    while n!=0:
        if n%10==buscar:
            contador+=1
        n//=10
    if contador !=0:
        return print(contador)
    else:
        return "El número a buscar no se encuentra en la cifra numérica."

#funcion: indicar la suma de los dígitos 3
def indicarSuma (n):
    """
    Función: Suma los dígitos de un número entero
    Entrada: Número
    Salida: Suma
    """
    suma=0
    while n>0:
        x=n%10
        if x!=0:
            suma+=x
        n=n//10
    return print(suma)

#funcion:  Reciba un valor, indique si es binario o no 4
def revisarBinario(n):
    """
    Función: Verifica que los números digitados sean binarios 5
    Entrada: Número binario
    Salida: True o False
    """
    while n > 0:
        num = n % 10
        if num != 0 and num != 1:
            return print(False)
        n = n // 10
    return print(True)

#funcion: verificar la paridad de un dígito en una posición dada 5
def verificarParidad (n, posicion):
    """
    Función: Verifica si en X posición, existe un dígito par
    Entrada: Número
    Salida: True o False
    """
    contador=0
    while n!=0:
        x=n%10
        if x!=0:
            contador+=1
            digito=x
        n//=10
        if posicion==contador:
            if digito%2==0:
                print(True)
            else:
                print(False)          
    return ""

#funcion: Número palíndromo 6
def reconocerPalindromo(n):
    """
    Función: Verifica si el número es palíndromo
    Entrada: Número
    Salida: Palíndromo o no
    """
    numeroOriginal=n
    palindromo=0
    while n>0:
        num = n % 10
        palindromo=(palindromo*10)+num
        n=n//10
    if numeroOriginal!=palindromo:
        return print("Su número no es palindromo")
    else:
        return print("Su número es palindromo")


#funcion: Invertir número 7
def invertirNumero(n):
    """
    Función: Invierte cualquier número entero que se digíte
    Entrada: Número
    Salida: Número invertido
    """
    invertir=0
    while n>0:
        num = n % 10
        invertir=(invertir*10)+num
        n=n//10
    return print(invertir)

#función: número binario 8
def convertirBinario(n):
    """
    Función: Convierte cualquier número decimal que se digíte en binario
    Entrada: Número decimal
    Salida: Binario
    """
    binario=0
    contador=1
    while n>0:
        num = n % 2
        binario+=(num*contador)
        n=n//2
        contador*=10
    return print(binario)

#funcion: crear digito solo con impares 9
def crearDigitoImpar(n):
    """
    Función: Crea un número con solo impares a partir de un número entero
    Entrada: Núméro entero
    Salida: Número impar
    """
    i=0
    numImpar=0
    while n!=0:
        num=n%10
        if (num%2)==0:
            numImpar+=0
            i+=0
        elif num%2!=0:
            numImpar=numImpar+(num*(10**i))
            i+=1
        n=n//10
    if numImpar==0:
        print("No existen números impares en su número")


    return print(numImpar)

#funcion:  eliminar en el primero los valores repetidos 10
def eliminarRepetidos(n1,n2):
    """
    Función: Elimina del número 1 los números repetidos que están en el número 2
    Entrada: n1 y n2, números enteros
    Salida: Número sin repetidos
    """
    i=0
    numImp=0
    aux1=n1
    while aux1!=0:
        num1=aux1%10
        aux2=n2
        repetido=False
        while aux2!=0:
            num2=aux2%10
            if num1==num2:
                repetido=True
                break
            aux2//=10
        if repetido==False:
            numImp+=num1*(10 ** i)
            i+=1
        aux1//=10
    if numImp==0:
        print("Todos los valores fueron eliminados")
    return print(numImp)

#funcion: Convertir de decimal a octal 11
def convertirOctal(n):
    """
    Función: Convierte de decimal a octal
    Entrada: Número entero en decimal
    Salida: Número entero en octal
    """
    numOct=0
    i=0
    while n>0:
        num=n%8
        numOct+=num*(10**i)
        i+=1
        n=n//8
    return print(numOct)

#funcion: factorial de un número: 12
def factorialNum(n):
    """
    Función: Calcula el factorial de un número
    Entrada: Número entero
    Salida: Factorial del número ya calculado
    """
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    return print(fact)