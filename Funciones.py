#Elaborado por: Daniel Campos y Alejadro Madrigal
#Creación: 28/08/2023 Hora: 8:37 am
#Ult mod: 28/08/2023 Hora: 9:37 pm
#Versión 3.10.6

#val funciones

#def funciones
#contar dígitos
def contarDigitos(n):
    """
    """
    contador=0
    while n!=0:
        if n%10 !=0:
            contador+=1
        n//=10
    return contador
    
#funcion: comparar dígitos y números
def compararDigitos(n1,n2):
    """
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

#funcion: cuántas veces aparece un dígito en una cifra entera
def contarRepetidos (n, buscar):
    """
    """
    contador=0
    while n!=0:
        if n%10==buscar:
            contador+=1
        n//=10
    if contador !=0:
        return contador
    else:
        return "El número a buscar no se encuentra en la cifra numérica."

#funcion: indicar la suma de los dígitos
def indicarSuma (n):
    """
    """
    suma=0
    while n>0:
        x=n%10
        if x!=0:
            suma+=x
        n=n//10
    return suma

#funcion:  Reciba un valor, indique si es binario o no
def revisarBinario(n):
    if n%10!=0 and n%10!=1:
        print(False)
    else:
        print(True)
    return ""

#funcion: verificar la paridad de un dígito en una posición dada
def verificarParidad (n, posicion):
    """
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

#funcion: Número palíndromo
def reconocerPalindromo(n):
    """
    """
    numeroOriginal=n
    palindromo=0
    while n>0:
        num = n % 10
        palindromo=(palindromo*10)+num
        n=n//10
    if numeroOriginal!=palindromo:
        return "Su número no es palindromo"
    else:
        return "Su número es palindromo"


#funcion: Invertir número
def invertirNumero(n):
    """
    """
    invertir=0
    while n>0:
        num = n % 10
        invertir=(invertir*10)+num
        n=n//10
    return invertir

#función: número binario
def convertirBinario(n):
    """
    """
    binario=0
    contador=1
    while n>0:
        num = n % 2
        binario+=(num*contador)
        n=n//2
        contador*=10
    return binario

#funcion: crear digito solo con impares
def crearDigitoImpar(n):
    """
    """
    i=0
    numImpar=0
    while n!=0:
        num=n%10
        if (num%2)==0:
            numImpar+=0
            i+=0
        else:
            numImpar=numImpar+(num*(10**i))
            i+=1
        n=n//10
    return numImpar

#funcion:  eliminar en el primero los valores repetidos
def eliminarRepetidos(n1,n2):
    """
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
    return numImp

#funcion: Convertir de decimal a octal
def convertirOctal(n):
    """
    """
    numOct=0
    i=0
    while n>0:
        num=n%8
        numOct+=num*(10**i)
        i+=1
        n=n//8
    return numOct

#funcion: factorial de un número:
def factorialNum(n):
    """
    """
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    return fact

#prueba
n1=int(input("n1: "))
n2=int(input("n2: "))
print(eliminarRepetidos(n1,n2))


