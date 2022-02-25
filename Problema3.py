"""Realice un programa que ingrese un precio en quetzales, e indique cuanto de esa totalidad es IVA y cuanto es el precio sin
IVA. (Recuerda que el IVA en Guatemala es del 12%)"""
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
    menu=int(input_numero("Precios \n 1- Ingrese el Precio \n 2- Historial \n 0- Salir \n"))
    if menu==1:
        precio=int(input_numero("Ingrese el precio en (Q): "))
        iva=precio * 0.12
        precio2= precio - iva
        
        print("El precio con IVA es: ", precio)
        print("El del IVA es: ", iva)
        print("El precio sin IVA es: ", precio2)
        print("-------------------------------")

        cursor = conexion.cursor()
        SQL = "INSERT INTO Problema3(Precio,  Iva, Precio_Sin_Iva) VALUES( %s, %s,%s)" 
        cursor.execute(SQL,(precio, iva, precio2))
        conexion.commit()
        cursor.close()


    elif menu==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM Problema3" 
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
    elif menu== 0:
        break
    else:
        print("Ingrese un valor correcto")