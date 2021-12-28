#! usr/bin/env python
import funciones_fiados
import funciones_productos
import funciones_analisis_financiero
import funciones_misc
import json
import os
import datetime

archivo_productos = 'productos.json'
archivo_fiados = 'fiados.json'
archivo_ganancias = 'ganancias.txt'
archivo_ventas = 'ventas.json'
fecha_actual_mmddyy = datetime.datetime.now().strftime('%x')

funciones_misc.crear_archivo_guardado(archivo_productos, '1')
funciones_misc.crear_archivo_guardado(archivo_fiados, '1')
funciones_misc.crear_archivo_guardado(archivo_ventas, '2')

"""MAIN LOOP"""
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*****MI PUNTO DE VENTA*****")
    print("ESCRIBE 'salir' PARA SALIR DEL PROGRAMA")
    print('\n')
    print('MENU PRINCIPAL')
    print("Selecciona una opción")
    print("1. Caja Registradora")
    print("2. Gestión de Productos")
    print("3. Gestión de Fiados")
    print("4. Gestión de Finanzas")
    opcion = input("-->").lower()
    if funciones_misc.verificar_errores_input(4, opcion, ['salir', '1', '2', '3', '4']) or funciones_misc.verificar_errores_input(1, opcion):
        continue

    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        funciones_productos.loop_caja_registradora(archivo_productos, archivo_ventas, archivo_fiados, fecha_actual_mmddyy)
        continue

    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        funciones_productos.loop_gestion_de_productos(archivo_productos, archivo_ventas, fecha_actual_mmddyy)
        continue

    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        funciones_fiados.loop_gestion_de_fiados(archivo_fiados, archivo_productos, fecha_actual_mmddyy)
        continue

    elif opcion == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('¡EN CONSTRUCCIÓN!')
        input("Presiona Enter para continuar...")
        continue

    elif funciones_misc.salir(opcion):
        os.system('cls' if os.name == 'nt' else 'clear')
        break
