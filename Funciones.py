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

#funcion 3: indicar la suma de los dígitos
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
#prueba
n=int(input("n: "))
print(convertirBinario(n))


