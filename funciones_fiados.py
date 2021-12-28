#! usr/bin/env python
import json
import os
import funciones_misc
import funciones_productos

def imprimir_fiados(archivo):
    fiados = funciones_misc.leer_archivo(archivo)
    print('           FIADOS')
    print("CODIGO      DEUDOR                DEUDA")
    for codigo, info_fiado in enumerate(fiados):
        print(str(codigo + 1), " " * (10 - len(str(codigo + 1))), info_fiado['nombre'], " " * (20 - len(info_fiado['nombre'])), info_fiado['valor_monetario'])

def loop_gestion_de_fiados(archivo_fiados, archivo_productos, fecha_actual_mmddyy):
    """Main Loop Gestión de Fiados"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----GESTIÓN DE FIADOS-----")
        print("ESCRIBE 'salir' PARA VOLVER AL MENÚ PRINCIPAL")
        print('\n')
        print("Elige una opción:")
        print("1. Agregar Deuda")
        print("2. Cobrar Deuda")
        print("3. Incrementar Deuda")
        print("4. Ver Deudas")
        opcion = input("-->").lower()

        if funciones_misc.salir(opcion):
            break

        elif funciones_misc.verificar_errores_input(1, opcion) or funciones_misc.verificar_errores_input(4, opcion, ['salir', '1', '2', '3', '4', '5']):
            continue

        elif opcion == '1':
            os.system('cls' if os.name == 'nt' else 'clear')           
            subloop_agregar_deuda(archivo_fiados, archivo_productos, fecha_actual_mmddyy)

        elif opcion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            subloop_cobrar_deuda(archivo_fiados)

        elif opcion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            subloop_incrementar_deuda(archivo_fiados, archivo_productos, fecha_actual_mmddyy)

        elif opcion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-----VER DEUDAS-----")
            print('\n')
            imprimir_fiados(archivo_fiados)
            print('\n')
            input("Presiona Enter para continuar...")      
            continue      

def subloop_agregar_deuda(archivo_fiados, archivo_productos, fecha_actual_mmddyy):
    """Sub-Loop de Gestión de Fiados para Cobrar Deudas"""
    fiados = funciones_misc.leer_archivo(archivo_fiados)
    while True:
        print("-----AGREGAR DEUDA-----")
        print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS")
        
        print('\n')
        imprimir_fiados(archivo_fiados)
        print('\n')
        
        nuevo_deudor = input('Ingresa el nombre del deudor: ').title()
        if funciones_misc.salir(nuevo_deudor):
            break

        elif funciones_misc.verificar_errores_input(1, nuevo_deudor) or funciones_misc.verificar_errores_input(3, nuevo_deudor):
            continue

        elif funciones_misc.verificar_errores_input(6, nuevo_deudor, tipo_de_archivo='archivo_fiados'):
            opcion = input("¿Incrementar deuda? (S,N) \n-->").lower()
            if funciones_misc.salir(opcion):
                break

            elif funciones_misc.verificar_errores_input(4, opcion, ['s', 'n']) or funciones_misc.verificar_errores_input(1, opcion):
                continue

            elif opcion == 's':
                info_deudor = funciones_misc.obtener_info_item(nuevo_deudor, archivo_fiados)
                print('\n')
                print('DEUDOR:', info_deudor['nombre'])
                print("DEUDA ACTUAL: ", info_deudor['valor_monetario'])

                incremento = input("Incremento: ")
                if funciones_misc.salir(incremento):
                    break

                elif funciones_misc.verificar_errores_input(1, incremento) or funciones_misc.verificar_errores_input(2, incremento):
                    continue

                os.system('cls' if os.name == 'nt' else 'clear')
                for fiado in fiados:
                    if fiado['nombre'] == nuevo_deudor.title():
                        incrementar_deuda(nuevo_deudor, incremento, archivo_fiados)

                print('\n')
                imprimir_fiados(archivo_fiados)
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            
            elif opcion == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

        print("\n")
        print("¿QUÉ VAS A FIAR?:")
        print("1. Productos")
        print("2. Dinero")
        opcion = input("-->").lower()

        if funciones_misc.salir(opcion):
            break

        elif funciones_misc.verificar_errores_input(4, opcion, ["1", "2", "salir"]):
            break

        elif opcion == "1":
            os.system("cls" if os.name == "nt" else "clear")
            fiar_producto(archivo_fiados, archivo_productos, nuevo_deudor, fecha_actual_mmddyy)

        elif opcion == '2':
            os.system("cls" if os.name == 'nt' else 'clear')
            print("-----FIAR DINERO-----")
            print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS")
            print("\n")

            nueva_deuda = input("Ingresa el valor de la deuda:")
            if funciones_misc.salir(nueva_deuda):
                break

            elif funciones_misc.verificar_errores_input(1, nueva_deuda) or funciones_misc.verificar_errores_input(2, nueva_deuda):
                continue

            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n')

            print("NUEVO DEUDOR: ", nuevo_deudor)
            print("DEUDA: ", nueva_deuda)
            print('\n')
            confirmacion = input("¿Agregar nuevo deudor? (S, N ) \n -->").lower()
            if funciones_misc.salir(confirmacion):
                break
        
            elif funciones_misc.verificar_errores_input(1, confirmacion) or funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            elif confirmacion == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                funciones_misc.agregar_items(nuevo_deudor, nueva_deuda, archivo_fiados, fecha_actual_mmddyy)
                print('\n')
                imprimir_fiados(archivo_fiados)
                print('\n')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif confirmacion == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('¡NO SE HA HECHO NINGÚN CAMBIO!')
                print('\n')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

def subloop_cobrar_deuda(archivo_fiados):
    """Sub-Loop de Gestión de Fiados para Cobrar Deudas"""
    fiados = funciones_misc.leer_archivo(archivo_fiados)
    while True:
        print("-----COBRAR DEUDA-----")
        print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS")
        
        print('\n')
        imprimir_fiados(archivo_fiados)
        print('\n')


        nombre_deudor = input('Nombre del deudor: ').title()
        if funciones_misc.salir(nombre_deudor):
            break
        
        elif funciones_misc.verificar_errores_input(1, nombre_deudor) or funciones_misc.verificar_errores_input(3, nombre_deudor):
            continue

        elif funciones_misc.verificar_errores_input(5, nombre_deudor, tipo_de_archivo='archivo_fiados'):
            continue

        else:
            pago = input("Pago: ")
            if funciones_misc.salir(pago):
                break

            elif funciones_misc.verificar_errores_input(1, pago) or funciones_misc.verificar_errores_input(2, pago):
                continue

            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n')
            info_fiado = funciones_misc.obtener_info_item(nombre_deudor, archivo_fiados)
            print("DEUDOR: ", info_fiado['nombre'])
            print("DEUDA ACTUAL: ", info_fiado['valor_monetario'])

            nueva_deuda = info_fiado['valor_monetario'] - int(pago)

            if nueva_deuda <= 0:
                print("NUEVA DEUDA DESPUÉS DEL PAGO: 0")
                print("CAMBIO: ", nueva_deuda * - 1)
                print('\n')
                confirmacion = input('¿Continuar? (S/N) \n-->').lower()
                if funciones_misc.salir(confirmacion):
                    break
                elif funciones_misc.verificar_errores_input(1, confirmacion) or funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
                    continue
            
                elif confirmacion == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    funciones_misc.eliminar_item(nombre_deudor, archivo_fiados)
                    imprimir_fiados(archivo_fiados)
                    print('\n')
                    input("Presiona Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                elif confirmacion == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('¡NO SE HA HECHO NINGÚN CAMBIO!')
                    print('\n')
                    input('Presiona Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            else:
                print("NUEVA DEUDA DESPUÉS DEL PAGO: ", nueva_deuda)
                print('\n')
                confirmacion = input('¿Continuar? (S/N) \n-->').lower()
                if funciones_misc.salir(confirmacion):
                    break
                elif funciones_misc.verificar_errores_input(1, confirmacion) or funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
                    continue
            
                elif confirmacion == 's':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if nueva_deuda < 0:
                        funciones_misc.eliminar_item(nombre_deudor, archivo_fiados)
                    else:
                        abonar_deuda(nombre_deudor, pago, archivo_fiados)
                    print('\n')
                    imprimir_fiados(archivo_fiados)
                    print('\n')
                    input("Presiona Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                elif confirmacion == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('¡NO SE HA HECHO NINGÚN CAMBIO!')
                    print('\n')
                    input('Presiona Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
           
def subloop_incrementar_deuda(archivo_fiados, archivo_productos, fecha_actual_mmddyy):
    """Sub-Loop INCREMENTAR Deuda"""
    while True:
        print("-----INCREMENTAR DEUDA-----")
        print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS")
        
        print('\n')
        imprimir_fiados(archivo_fiados)
        print('\n')
    
        nombre_deudor = input("Ingresa el nombre del deudor: ").lower()
        if funciones_misc.salir(nombre_deudor):
            break
        elif funciones_misc.verificar_errores_input(1, nombre_deudor) or funciones_misc.verificar_errores_input(3, nombre_deudor):
            continue
        elif funciones_misc.verificar_errores_input(5, nombre_deudor, tipo_de_archivo='archivo_fiados'):
            continue


        incremento = input("Incremento: ")
        if funciones_misc.salir(incremento):
            break
        elif funciones_misc.verificar_errores_input(1, incremento) or funciones_misc.verificar_errores_input(2, incremento):
            continue
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        info_fiado = funciones_misc.obtener_info_item(nombre_deudor, archivo_fiados)
        print("DEUDOR: ", info_fiado['nombre'])
        print("DEUDA ACTUAL: ", info_fiado['valor_monetario'])                
        
        nueva_deuda = info_fiado['valor_monetario'] + int(incremento)

        print("NUEVA DEUDA DESPUES DE LA CONFIRMACION: ", nueva_deuda)
        print("\n")
        confirmacion = input("¿Continuar? (S,N) \n -->").lower()
        if funciones_misc.salir(confirmacion):
            break
        elif funciones_misc.verificar_errores_input(1, incremento) or funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
            continue

        elif confirmacion == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            incrementar_deuda(nombre_deudor, incremento, archivo_fiados)
            print('\n')
            imprimir_fiados(archivo_fiados)
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
                            
        elif confirmacion == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('¡NO SE HA HECHO NINGÚN CAMBIO!')
            print('\n')
            input('Presiona Enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            continue    

def incrementar_deuda(nombre_deudor, incremento, archivo_fiados):
    fiados = funciones_misc.leer_archivo(archivo_fiados)
    
    fiados_actualizada = []
    for fiado in fiados:
        if fiado['nombre'] == nombre_deudor.title():
            nueva_deuda = fiado['valor_monetario'] + int(incremento)
            fiados_actualizada.append({'nombre': fiado['nombre'], 'valor_monetario': nueva_deuda})
        else:
            fiados_actualizada.append(fiado)

    funciones_misc.actualizar_archivo(fiados_actualizada, archivo_fiados)
    print("¡DEUDA INCREMENTADA!")

def abonar_deuda(nombre_deudor, pago, archivo_fiados):
    fiados = funciones_misc.leer_archivo(archivo_fiados)
    
    fiados_actualizada = []
    for fiado in fiados:
        if fiado['nombre'] == nombre_deudor.title():
            nueva_deuda = fiado['valor_monetario'] - int(pago)
            fiados_actualizada.append({'nombre': fiado['nombre'], 'valor_monetario': nueva_deuda})
        else:
            fiados_actualizada.append(fiado)

    funciones_misc.actualizar_archivo(fiados_actualizada, archivo_fiados)
    print("¡PAGO REALIZADO!")

def fiar_producto(archivo_fiados, archivo_productos, nuevo_deudor, fecha_actual_mmddyy):
    os.system("cls" if os.name == "nt" else "clear")
    productos = funciones_misc.leer_archivo(archivo_productos)
    codigos_y_precios = funciones_productos.obtener_codigos_y_precios(productos)
    temp_productos_vendidos = {}
    for codigo, item in enumerate(productos):
        temp_productos_vendidos[str(codigo + 1)] = 0
    deuda_total = 0
    productos_fiados = {}
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("-----FIAR PRODUCTO-----")
        print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS\n")

        if deuda_total != 0:
            print("DEUDA ACTUAL: ")
            for codigo_temp, cantidad_temp in temp_productos_vendidos.items():
                if cantidad_temp != 0:
                    dic_producto = productos[int(codigo_temp) - 1]
                    print("- ", dic_producto["nombre"], " X ", cantidad_temp)
            print("DEUDA TOTAL ACUMULADA: ", deuda_total)

        print('                MENU')
        funciones_productos.imprimir_menu(archivo_productos)
        codigo_producto = input(
            "Ingresa el código del producto a fiar o Ingresa 'fiar' para agregar nueva deuda \n -->").lower()
        if funciones_misc.salir(codigo_producto):
            os.system("cls" if os.name == "nt" else "clear")
            break

        elif codigo_producto == 'fiar':
            os.system("cls" if os.name == "nt" else "clear")
            print("-----FIAR PRODUCTO-----")
            print("ESCRIBE 'salir' PARA VOLVER A GESTION DE FIADOS\n")
            print("NUEVO DEUDOR: ", nuevo_deudor)
            print("PRODUCTOS A FIAR:")
            for codigo_temp, cantidad_temp in temp_productos_vendidos.items():
                if cantidad_temp != 0:
                    dic_producto = productos[int(codigo_temp) - 1]
                    productos_fiados[dic_producto["nombre"]] = cantidad_temp
                    print("- ", dic_producto["nombre"], " X ", cantidad_temp)
            print("NUEVA DEUDA TOTAL: ", deuda_total)
            confirmacion = input("¿Agregar nuevo deudor? (S, N) \n -->").lower()
            if funciones_misc.salir(confirmacion):
                break
            elif funciones_misc.verificar_errores_input(1, confirmacion) or funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            elif confirmacion == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                agregar_fiado_productos(nuevo_deudor, deuda_total, archivo_fiados, fecha_actual_mmddyy, productos_fiados)
                break
            elif confirmacion == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                break


        elif funciones_misc.verificar_errores_input(1, codigo_producto) or funciones_misc.verificar_errores_input(2, codigo_producto):
            continue

        elif codigo_producto not in codigos_y_precios.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡CÓDIGO INEXISTENTE!")
            input("Presiona Enter para continuar...")

            continue

        else:
            cantidad = input("¿Qué cantidad? \n -->")
            if funciones_misc.salir(cantidad):
                break

            if funciones_misc.verificar_errores_input(1, cantidad) or funciones_misc.verificar_errores_input(2, cantidad):
                continue

            for codigo_precio in codigos_y_precios.keys():
                if codigo_precio == codigo_producto:
                    deuda_total += codigos_y_precios[codigo_producto] * int(cantidad)

            for codigo_venta in temp_productos_vendidos.keys():
                if codigo_venta == codigo_producto:
                    temp_productos_vendidos[codigo_venta] += int(cantidad)
            continue

def agregar_fiado_productos(nuevo_deudor, deuda_total, archivo_fiados, fecha_actual_mmddyy, productos_fiados):
    lista_items = funciones_misc.leer_archivo(archivo_fiados)
    lista_items.append({"nombre": nuevo_deudor, "valor_monetario": int(deuda_total), "fecha_creacion": fecha_actual_mmddyy, "productos_fiados": productos_fiados, "historial_modificaciones": {fecha_actual_mmddyy: {"nombre": nuevo_deudor, "valor_monetario": deuda_total, "productos_fiados": productos_fiados}}})

    funciones_misc.actualizar_archivo(lista_items, archivo_fiados)

    print("¡NUEVA DEUDA AGREGADA!")
    print('\n')
    imprimir_fiados(archivo_fiados)
    input("Presiona ENTER para continuar...")
