"""Realice un programa que ingrese un número e indique si el número ingresado es primo o es compuesto"""
#Javier Andrés Barrios del Aguila
#201801376

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
    menu=int(input_numero("Numeros Primos \n 1- Ingresar numero \n 2- Historial \n 0- Salir \n"))
    if menu==1:
        num=int(input_numero("Ingrese un numero: "))
        def primo(num):
            cont=0
            resultado=True
            for i  in range(1,num+1):
                if (num%i==0):
                    cont+=1
                elif (cont>2):
                    resultado=False
                    break
            return resultado
        if (primo(num)==True):
            x= "Primo"
            print("El numero", num, "es", x)
            print("----------------------------------")

            cursor = conexion.cursor()
            SQL = "INSERT INTO Problema4(Numero, Primo_NoPrimo) VALUES( %s, %s)" 
            cursor.execute(SQL,(num, x))
            conexion.commit()
            cursor.close()

        else:
            x= "No Primo"
            print("El  numero", num, "es", x)
            print("----------------------------------")

            cursor = conexion.cursor()
            SQL = "INSERT INTO Problema4(Numero, Primo_NoPrimo) VALUES( %s, %s)" 
            cursor.execute(SQL,(num, x))
            conexion.commit()
            cursor.close()

    elif menu==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM Problema1" 
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        
    elif menu==0:
        break
    else:
        print("Ingrese un valor correcto")

