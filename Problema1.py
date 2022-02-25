""" Juego simulado del Gran 8
La Reglas del juego. Debes lanzar un par de dados. Si la suma de las caras es un 8, ganas. Si sale 7, pierdes. Si no ha
salido, ni 8, ni 7, puedes seguir lanzando. Si sale 8 ganas, pero si en algún otro lanzamiento sale 7, pierdes """
#Javier Andrés Barrios del Aguila
#201801376
import random

import psycopg2

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "javier",
        password = "javier",
        dbname = "Parcial1"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Error en la conexión \nverificar parametros \n")


def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero


while True:
    menu=int(input_numero("El Gran 8 \n 1- Lanza los dados \n 2- Historial \n 0- Salir \n"))
    if menu == 1:
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        suma= num1+num2
        print("Tu primer numero es: ", num1)
        print("Tu primer numero es: ", num2)
        print("La suma es: ", suma)

        if num1+num2 == 8:
            x=("¡¡GANASTE!!")
            print(x)

            cursor = conexion.cursor()
            SQL = "INSERT INTO Problema1(Dado_1,  Dado_2, Suma, Resultado) VALUES( %s, %s,%s, %s)" 
            cursor.execute(SQL,(num1, num2, suma, x))
            conexion.commit()
            cursor.close()

        elif num1+num2 == 7:
            x=("Perdiste :(")
            print(x)

            cursor = conexion.cursor()
            SQL = "INSERT INTO Problema1(Dado_1,  Dado_2, Suma, Resultado) VALUES( %s, %s,%s, %s)" 
            cursor.execute(SQL,(num1, num2, suma, x))
            conexion.commit()
            cursor.close()

            break

        elif num1+num2 != 8 and num1+num2 !=7 :
            x=("Sigue Participando")
            print(x)

            cursor = conexion.cursor()
            SQL = "INSERT INTO Problema1(Dado_1,  Dado_2, Suma, Resultado) VALUES( %s, %s,%s, %s)" 
            cursor.execute(SQL,(num1, num2, suma, x))
            conexion.commit()
            cursor.close()

        else:
            break

    elif menu == 2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM Problema1" 
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
    elif menu == 0:
        break
    else:
        print("Ingrese un valor correcto")


