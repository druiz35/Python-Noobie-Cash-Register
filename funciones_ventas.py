import json
import datetime
import funciones_misc
import os


def actualizar_ventas(temp_productos_vendidos, archivo_productos_vendidos, fecha_actual_mmddyy):
	dic_archivo = funciones_misc.leer_archivo(archivo_productos_vendidos)
	dics_ventas = []
	for dics in dic_archivo.values():
		dics_ventas.append(dics)

	for posicion, nombre_producto in enumerate(dic_archivo):
		for codigo_temp, vendido_temp in temp_productos_vendidos.items():
			if str(posicion + 1) == codigo_temp:
				x = dics_ventas[posicion]
				for fecha_archivo, vendido_archivo in x.items():
					if fecha_archivo == fecha_actual_mmddyy:
						x[fecha_archivo] = vendido_temp ++ vendido_archivo

	actualizado = {}
	for posicion, nombre_producto in enumerate(dic_archivo):
		actualizado[nombre_producto] = dics_ventas[posicion]

	with open(archivo_productos_vendidos, 'w') as f:
		json.dump(actualizado, f, indent=4)

def loop_gestion_de_finanzas(archivo_productos, archivo_ventas, archivo_fiados, fecha_actual_mmddyy):
	"""Main Loop Gestión de Finanzas"""
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-----GESTIÓN DE FINANZAS-----")
		print("ESCRIBE 'salir' PARA SALIR DE GESTION DE PRODUCTOS")
		print('\n')
		print("Elige una opción:")
		print("1. Informe de Ventas")
		opcion = input("-->").lower()

		if funciones_misc.salir(opcion):
			break

		elif funciones_misc.verificar_errores_input(1, opcion) or funciones_misc.verificar_errores_input(4, opcion, ['salir', '1']):
			continue

		elif opcion == '1':
			subloop_informe_ventas(archivo_productos, archivo_ventas, archivo_fiados, fecha_actual_mmddyy)

def subloop_informe_ventas(archivo_productos, archivo_ventas, archivo_fiados, fecha_actual_mmddyy):
	"""Subloop Informe de Ventas"""
	while True:
		os.system("cls" if os.name == "nt" else "clear")
		print("-----INFORME DE VENTAS-----")
		print("ESCRIBE 'salir' PARA SALIR DE INFORME DE VENTAS")
		print("\n")
		print("Elige una opción:")
		opcion = input("-->").lower()

		if funciones_misc.salir(opcion):
			break
