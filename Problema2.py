""" Un estudiante ha tenido el siguiente registro de calificaciones (de 0 a 100) y desea conocer como ha sido su rendimiento
calculando algunos estadísticos descriptivos como la media, la mediana, la moda, el rango, la desviación estándar y la
varianza. (Ejecute para 5 calificaciones). """
#Javier Andrés Barrios del Aguila
#201801376
import numpy as np
import statistics as stat

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
    menu=int(input_numero("Registro de Calificaciones \n 1- Ingresar Calificaiones \n 2- Historial \n 0- Salir \n"))
    if menu==1:
        nota1=int(input_numero("Ingrese su primera nota: "))
        nota2=int(input_numero("Ingrese su segunda nota: "))
        nota3=int(input_numero("Ingrese su tercera nota: "))
        nota4=int(input_numero("Ingrese su cuarta nota: "))
        nota5=int(input_numero("Ingrese su quinta nota: "))
        notas=[nota1, nota2, nota3, nota4, nota5]
        grande= max(notas)
        pequeno= min (notas)

        print(grande, pequeno)

        print("Sus notas son: ",notas, "\n")

        promedio=np.mean(notas)
        media=np.median(notas)
        moda=stat.mode(notas)
        des=np.std(notas)
        var=np.var(notas)
        rang = grande-pequeno
        print("Promedio: ", promedio)
        print("Media: ", media)
        print("Moda: ", moda)
        print("Desviación Estandar: ", des)
        print("Varianza: ", var)
        print("Rango: ", rang)
        print("----------------------")

        cursor = conexion.cursor()
        SQL = "INSERT INTO Problema2(Nota_1, Nota_2 , Nota_3, Nota_4, Nota_5, Promedio, Media, Moda, Desviacion, Varianza, Rango) VALUES( %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s)" 
        cursor.execute(SQL,(nota1, nota2, nota3, nota4, nota5, promedio, media, moda, des, var, rang))
        conexion.commit()
        cursor.close()

    if menu==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM Problema2" 
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
    if menu==0:
        break
    else:
        print("Ingrese un valor correcto")