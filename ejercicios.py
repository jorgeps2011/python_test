"""

1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******

"""



print("========================== Ejercicio 1 ========================== ")

#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(a,b):
    if a > b: 
        return a
    else:
        return b

print(max(20,3))


print("========================== Ejercicio 2 ========================== ")

#2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a,b,c):
    if a > b:
        if a > c:
            return a
        elif a < c:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c

print(max_de_tres(1,2,3))
print(max_de_tres(1,3,2))
print(max_de_tres(3,2,1))

print("========================== Ejercicio 3 ========================== ")

print("========================== Ejercicio 4 ========================== ")

print("========================== Ejercicio 5 ========================== ")

print("========================== Ejercicio 6 ========================== ")

print("========================== Ejercicio 7 ========================== ")

print("========================== Ejercicio 8 ========================== ")

print("========================== Ejercicio 9 ========================== ")

print("========================== Ejercicio 10 ========================= ")

