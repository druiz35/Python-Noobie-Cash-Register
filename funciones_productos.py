#! usr/bin/env python
import os
import funciones_misc
import funciones_fiados
import funciones_ventas

def imprimir_menu(archivo_productos):
    """Genera e imprime el menú de los productos con su respectivo nombre, precio y código"""
    funciones_misc.organizar_lista_alf(archivo_productos)

    # Abre el archivo de productos
    productos = funciones_misc.leer_archivo(archivo_productos)
    encabezado = "CODIGO      PRODUCTO                        PRECIO"


    lista_1, lista_2 = [], []
    longitud_lista = int(len(productos)/2)
    
    for item in productos[0:longitud_lista]:
        for codigo, item in enumerate(productos[0:longitud_lista]):
            lista_1.append(item)
        break

    for item in productos[longitud_lista::]:
        for codigo, item in enumerate(productos[longitud_lista::]):
            lista_2.append(item)
        break

    print(encabezado + "        " +  encabezado)
    # Despliega el menú

    if len(productos) % 2 == 1:
        for codigo, info_producto in enumerate(lista_1):
            item_lista_2 = lista_2[codigo]
            print(str(codigo + 1), " " * (10 - len(str(codigo + 1))), info_producto['nombre'], " " * (30 - len(info_producto['nombre'])),  info_producto['valor_monetario'], " " * (12 - len(str(info_producto["valor_monetario"]))), str(codigo + int(len(productos)/2) + 1), " " * (10 - len(str(codigo + 19))), item_lista_2['nombre'], " " * (30 - len(item_lista_2['nombre'])), item_lista_2['valor_monetario'])
            if (codigo + 1) > longitud_lista:
                break
        
        for  codigo, item in enumerate(productos):
            if codigo + 1 == len(productos):
                print(" " * len("                                                         "),str(codigo + 1), " " * (10 - len(str(codigo + 1))), item['nombre'], " " * (30 - len(item['nombre'])), item['valor_monetario'])
    
    else:
        for codigo, info_producto in enumerate(lista_1):
            item_lista_2 = lista_2[codigo]
            print(str(codigo + 1), " " * (10 - len(str(codigo + 1))), info_producto['nombre'], " " * (30 - len(info_producto['nombre'])), info_producto['valor_monetario'], " " * (12 - len(str(info_producto["valor_monetario"]))), str(codigo + int(len(productos)/2) + 1), " " * (10 - len(str(codigo + 19))), item_lista_2['nombre'], " " * (30 - len(item_lista_2['nombre'])), item_lista_2['valor_monetario'])
            if (codigo + 1) > longitud_lista:
                break

def obtener_codigos_y_precios(lista_de_productos):
    """Función para facilitarle al Loop Caja Registradora la elección de productos y el cálculo del total"""

    # Diccionario vacío para tirar cuando el loop FOR termine su tarea
    codigos_y_precios = {}

    # Loop FOR para agregar el código del producto y su precio al diccionario, como key y value respectivamente
    for codigo, producto in enumerate(lista_de_productos):
        codigos_y_precios[str(codigo + 1)] =  producto['valor_monetario']
    return codigos_y_precios

def subloop_agregar_producto(archivo_productos, archivo_ventas, fecha_actual_mmddyy):
    """Main Loop Agregar Producto"""
    while True:
        print("-----AGREGAR PRODUCTO-----")
        print("ESCRIBE 'salir' PARA VOLVER AL MENU PRINCIPAL")
        print('\n')
        # Muestra el menú actual
        print("            MENU ACTUAL")
        imprimir_menu(archivo_productos)
        print("\n")

        # Información del usuario
        nombre_producto = input("Nombre del nuevo producto: ").title()
        if funciones_misc.salir(nombre_producto):
            break
        
        elif funciones_misc.verificar_errores_input(6, nombre_producto, tipo_de_archivo='archivo_productos'):
            continue

        elif funciones_misc.verificar_errores_input(1, nombre_producto) or funciones_misc.verificar_errores_input(3, nombre_producto):
            continue

        # Comprueba que el precio sea un dato numérico
        precio = input("Precio del nuevo producto: ")
        if funciones_misc.salir(precio):
            break

        elif funciones_misc.verificar_errores_input(1, precio) or funciones_misc.verificar_errores_input(2, precio):
            continue

        # Confirmación de nuevo producto
        os.system('cls' if os.name == 'nt' else 'clear')
        print(nombre_producto, " = ", precio)
        confirmacion = input("¿Agregar nuevo producto? (S, N) \n -->").lower()
        if funciones_misc.salir(confirmacion):
            break

        elif funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']) or funciones_misc.verificar_errores_input(1, confirmacion):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡NO SE REALIZÓ NINGÚN CAMBIO!")
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # Si confirmacion es igual a sí, entonces...
        elif confirmacion == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            funciones_misc.agregar_items(nombre_producto, precio, archivo_productos, fecha_actual_mmddyy)
            funciones_misc.agregar_item_diccionario(nombre_producto, archivo_ventas, fecha_actual_mmddyy)
            print('\n')
            print("                  NUEVO MENU")
            imprimir_menu(archivo_productos)
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue


        # Pero si confirmacion es igual a no...
        elif confirmacion == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡NO SE REALIZÓ NINGÚN CAMBIO!")
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

def subloop_eliminar_producto(archivo_productos, archivo_ventas):
    """Main Loop Eliminar Producto"""
    productos = funciones_misc.leer_archivo(archivo_productos)
    while True:
        print("-----ELIMINAR PRODUCTO-----")
        print("ESCRIBE 'salir' PARA VOLVER AL MENU PRINCIPAL")
        print("\n")

        # Muestra el menú actual
        print("            MENU ACTUAL")
        imprimir_menu(archivo_productos)
        print('\n')

        # Le pregunta al usuario por el nombre que desea elminar, y lo guarda en una variable
        nombre_producto = input("Ingresa el nombre del producto que quieres eliminar \n -->").lower()
        if funciones_misc.salir(nombre_producto):
            break

        elif funciones_misc.verificar_errores_input(1, nombre_producto) or funciones_misc.verificar_errores_input(3, nombre_producto):
            continue

        elif funciones_misc.verificar_errores_input(5, nombre_producto, tipo_de_archivo='archivo_productos'):
            continue


        else:
            # Confirmación eliminar producto
            os.system('cls' if os.name == 'nt' else 'clear')
            print("VAS A ELIMINAR: ", nombre_producto)
    
            confirmacion = input("¿Continuar? (S,N) \n -->").lower()
            if funciones_misc.salir(confirmacion):
                break
            
            if funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
                continue

            # Si confirmación es igual a sí, entonces...
            elif confirmacion == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                funciones_misc.eliminar_item(nombre_producto, archivo_productos)
                #funciones_misc.eliminar_item_diccionario(nombre_producto, archivo_ventas)
                print('\n')
                print("NUEVO MENU")
                imprimir_menu(archivo_productos)
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

            # Pero si confirmación es igual a no, entonces...
            elif confirmacion == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("¡NO SE HICIERON CAMBIOS!")
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

def subloop_editar_producto(archivo_productos, archivo_ventas):
    """Main-Loop Editar Productos"""
    productos = funciones_misc.leer_archivo(archivo_productos)

    while True:
        print("-----EDITAR PRODUCTO-----")
        print("ESCRIBE 'salir' PARA VOLVER AL MENU PRINCIPAL")
        print('\n')

        # Muestra el menú actual
        print("            MENU ACTUAL")
        imprimir_menu(archivo_productos)
        print("\n")

        # Información del usuario
        nombre_producto = input("Nombre del producto a editar: ").title()
        if funciones_misc.salir(nombre_producto):
            break

        elif funciones_misc.verificar_errores_input(1, nombre_producto) or funciones_misc.verificar_errores_input(3, nombre_producto):
            continue

        elif funciones_misc.verificar_errores_input(5, nombre_producto, tipo_de_archivo='archivo_productos'):
            continue

        nuevo_nombre = input("Nuevo Nombre (Deja en blanco para no cambiar nada): ").title()
        if funciones_misc.salir(nuevo_nombre):
            break

        nuevo_precio = input("Nuevo Precio (Deja en blanco para no cambiar nada): ")
        if funciones_misc.salir(nuevo_precio):
            break

        elif funciones_misc.verificar_errores_input(2, nuevo_precio):
            continue

        # Chequeo de información
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print("INFORMACIÓN ACTUAL DEL PRODUCTO ")
        for producto in productos:
            if producto['nombre'] == nombre_producto:
                print("Nombre Actual: ", producto['nombre'])
                print("Precio Actual: ", producto['valor_monetario'])

        print('\n')
        print("NUEVA INFORMACIÓN")
        if len(nuevo_precio) == 0 and len(nuevo_nombre) > 0:
            print("Nuevo Nombre: ", nuevo_nombre)
            print("Nuevo Precio: SIN CAMBIOS")

        elif len(nuevo_nombre) == 0 and len(nuevo_precio) > 0:
            print("Nuevo Nombre: SIN CAMBIOS")
            print("Nuevo Precio: ", nuevo_precio)

        elif len(nuevo_precio) > 0 and len(nuevo_nombre) > 0:
            print("Nuevo Nombre: ", nuevo_nombre)
            print("Nuevo Precio: ", nuevo_precio)

        elif len(nuevo_precio) == 0 and len(nuevo_nombre) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡NO SE HICIERON CAMBIOS!")
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # Confirmación
        print('\n')
        confirmacion = input("¿Continuar (S,N)?\n-->").lower()
        if funciones_misc.salir(confirmacion):
            break
        
        elif funciones_misc.verificar_errores_input(4, confirmacion, ['s', 'n']):
            continue

        elif confirmacion == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            funciones_misc.editar_item(nombre_producto, nuevo_nombre, nuevo_precio, archivo_productos)
            #funciones_misc.editar_item_diccionario(nombre_producto, nuevo_nombre, archivo_ventas)
            print('\n')
            imprimir_menu(archivo_productos)
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        elif confirmacion == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡NO SE HICIERON CAMBIOS!")
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

def loop_gestion_de_productos(archivo_productos, archivo_ventas, fecha_actual_mmddyy):
    """Main Loop Gestión de Productos"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----GESTIÓN DE PRODUCTOS-----")
        print("ESCRIBE 'salir' PARA SALIR DE GESTION DE PRODUCTOS")
        print('\n')
        print("Elige una opción:")
        print("1. Agregar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Ver Menú de Productos")
        opcion = input("-->").lower()

        if funciones_misc.salir(opcion):
            break

        elif funciones_misc.verificar_errores_input(1, opcion) or funciones_misc.verificar_errores_input(4, opcion, ['salir', '1', '2', '3', '4']):
            continue

        elif opcion == '1':
            os.system('cls' if os.name == 'nt' else 'clear')           
            subloop_agregar_producto(archivo_productos, archivo_ventas, fecha_actual_mmddyy)

        elif opcion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            subloop_editar_producto(archivo_productos, archivo_ventas)

        elif opcion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            subloop_eliminar_producto(archivo_productos, archivo_ventas)

        elif opcion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('                MENU')
            imprimir_menu(archivo_productos)
            input("Presiona Enter para continuar...")            

def loop_caja_registradora(archivo_productos, archivo_ventas, archivo_fiados, fecha_actual_mmddyy):
    """Main Loop Caja Registradora"""

    # Lee el archivo de los productos
    productos = funciones_misc.leer_archivo(archivo_productos)

    codigos_y_precios = obtener_codigos_y_precios(productos)

    temp_productos_vendidos = {}
    for codigo, item in enumerate(productos):
        temp_productos_vendidos[str(codigo + 1)] = 0
    

    total = 0
    while True:
        print("-----CAJA REGISTRADORA-----")
        print("ESCRIBE 'salir' PARA VOLVER AL MENU PRINCIPAL\n")
        if total != 0:
            print("FACTURA ACTUAL: ")
            for codigo_temp, cantidad_temp in temp_productos_vendidos.items():
                if cantidad_temp != 0:
                    dic_producto = productos[int(codigo_temp) - 1]
                    print("- ", dic_producto["nombre"], " X ", cantidad_temp)
            print("TOTAL ACUMULADO: ", total)

        print('                MENU')
        imprimir_menu(archivo_productos)

        codigo_producto = input('¿Qué quieres llevar? (Ingresa el código del producto, '
                                'Ingresa "reset" para limpiar el valor total, ingresa "fiar" para agregar total a una deuda '
                                'o Ingresa "total" para ver el costo total) \n -->').lower()

        if funciones_misc.salir(codigo_producto):
            break
            
        # Si codigo_producto es igual a fiar, crea una nueva deuda o agrega el total a una deuda existente
        elif codigo_producto.lower() == 'fiar':
            if total == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("¡NO SE SUMÓ NINGÚN PRODUCTO!")
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                print('\n')
                nuevo_deudor = input("Nombre del Deudor: ").title()
                if funciones_misc.verificar_errores_input(1, nuevo_deudor) or funciones_misc.verificar_errores_input(3, nuevo_deudor):
                    continue
                elif funciones_misc.verificar_errores_input(6, nuevo_deudor, tipo_de_archivo='archivo_fiados'):
                    os.system('cls' if os.name=='nt' else 'clear')
                    objeto_deuda = funciones_misc.obtener_info_item(nuevo_deudor, archivo_fiados)
                    print("DEUDOR: ", objeto_deuda['nombre'])
                    print("DEUDA ACTUAL: ", objeto_deuda['valor_monetario'])
                    print("NUEVA DEUDA DESPUÉS DE LA CONFIRMACION: ", objeto_deuda['valor_monetario'] + total)
                    print("\n")
                    continuar = input("¿Incrementar Deuda (S/N)? \n -->").lower()
                    if funciones_misc.salir(continuar):
                        break

                    elif funciones_misc.verificar_errores_input(1, continuar):
                        continue

                    elif funciones_misc.verificar_errores_input(4, continuar, ["s", "n"]):
                        continue
    
                    elif continuar == 's':
                        os.system('cls' if os.name == 'nt' else 'clear')    
                        funciones_fiados.incrementar_deuda(nuevo_deudor, total, archivo_fiados)
                        print('\n')
                        funciones_fiados.imprimir_fiados(archivo_fiados)
                        print('\n')
                        input("Presiona Enter para continuar...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        total = 0
                        for codigo in temp_productos_vendidos.keys():
                            temp_productos_vendidos[codigo] = 0
                        continue
    
                    elif continuar == 'n':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    productos_fiados = {}
                    print("-----FIAR PRODUCTO-----")
                    print("NUEVO DEUDOR: ", nuevo_deudor)
                    for codigo_temp, cantidad_temp in temp_productos_vendidos.items():
                        if cantidad_temp != 0:
                            dic_producto = productos[int(codigo_temp) - 1]
                            productos_fiados[dic_producto["nombre"]] = cantidad_temp
                            print("- ", dic_producto["nombre"], " X ", cantidad_temp)
                    print("NUEVA DEUDA TOTAL: ", total)
                    continuar = input("¿Agregar nuevo deudor? (S, N) \n -->").lower()

                    if funciones_misc.verificar_errores_input(1, continuar):
                        continue
                
                    elif funciones_misc.verificar_errores_input(1, continuar) or funciones_misc.verificar_errores_input(4, continuar, ['s','n']):
                        continue
    
                    elif continuar == 's':
                        os.system('cls' if os.name == 'nt' else 'clear')    
                        funciones_fiados.agregar_fiado_productos(nuevo_deudor, total, archivo_fiados, fecha_actual_mmddyy, productos_fiados)
                        print('\n')
                        funciones_fiados.imprimir_fiados(archivo_fiados)
                        print('\n')
                        input("Presiona Enter para continuar...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        total = 0
                        continue
    
                    elif continuar == 'n':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue   
        
        # Si codigo_producto es igual a total, muestra el costo total de los productos previamente sumados
        elif codigo_producto == 'total':
            if total == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("¡NO SE SUMÓ NINGÚN PRODUCTO!")
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FACTURA FINAL:")
            for codigo_temp, cantidad_temp in temp_productos_vendidos.items():
                if cantidad_temp != 0:
                    dic_producto = productos[int(codigo_temp) - 1]
                    print("- ", dic_producto["nombre"], " X ", cantidad_temp)
            print("\n")
            print('TOTAL: ', total)
            pago = input('Pago: ')
            if funciones_misc.salir(pago):
                break
            
            elif funciones_misc.verificar_errores_input(1, pago) or funciones_misc.verificar_errores_input(2, pago):
                continue

            cambio = total - int(pago)

            while cambio > 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("¡PAGO INCOMPLETO!")
                print("Faltan: ", cambio)
                pago = input("Pago: ")
                if funciones_misc.verificar_errores_input(1, pago) or funciones_misc.verificar_errores_input(2, pago):
                    continue
                cambio -= int(pago)

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                funciones_misc.actualizar_fechas_ventas(archivo_ventas, fecha_actual_mmddyy)
                funciones_ventas.actualizar_ventas(temp_productos_vendidos, archivo_ventas, fecha_actual_mmddyy)
                print("¡VENTA TERMINADA!")
                print("CAMBIO:", cambio * -1)
                print('\n')
                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                total = 0
                for codigo in temp_productos_vendidos.keys():
                    temp_productos_vendidos[codigo] = 0
            continue
        
        elif codigo_producto == 'reset':
            total = 0
            for codigo in temp_productos_vendidos.keys():
                temp_productos_vendidos[codigo] = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡TOTAL LIMPIADO!")
            print("¡NO SE VENDIÓ NINGÚN PRODUCTO!")
            print('\n')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        elif funciones_misc.verificar_errores_input(1, codigo_producto) or funciones_misc.verificar_errores_input(2, codigo_producto):
            continue
        
        elif codigo_producto not in codigos_y_precios.keys():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡CÓDIGO INEXISTENTE!")
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        else:
            cantidad = input('¿Qué cantidad? \n -->')
            if funciones_misc.salir(cantidad):
                break
            
            if funciones_misc.verificar_errores_input(1, cantidad) or funciones_misc.verificar_errores_input(2, cantidad):
                continue


            for codigo_precio in codigos_y_precios.keys():
                if codigo_precio == codigo_producto:
                    total += codigos_y_precios[codigo_producto] * int(cantidad)
                    os.system('cls' if os.name == 'nt' else 'clear')
            
            for codigo_venta in temp_productos_vendidos.keys():
                if codigo_venta == codigo_producto:
                    temp_productos_vendidos[codigo_venta] += int(cantidad)
            continue


