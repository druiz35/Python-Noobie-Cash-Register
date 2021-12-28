import funciones_productos
import os
import json
import datetime

def leer_archivo(archivo):
    """Función para abrir el archivo y retornar su contenido"""
    with open(archivo, 'r') as f:
        contenido = json.load(f)
    return contenido


def actualizar_archivo(nueva_informacion, archivo):
    """Función que guarda los cambios que se le hicieron a la lista de productos"""
    with open(archivo, 'w') as f:
        json.dump(nueva_informacion, f, indent=4)

    organizar_lista_alf(archivo)


def verificar_errores_input(tipo_de_error, dato_para_verificar, lista_comandos_admitidos_usuario=[], tipo_de_archivo = ''):
    """Función para verificar que no salte ningún tipo de error
    Tipos de Errores:
    1. No se ingresó ningún dato: verificar_errores_input(1, 'Input del usuario')
    2. Solo se pueden ingresar datos numéricos: verificar_errores_input(2, 'Input numérico del usuario')
    3. Solo se pueden ingresar datos alfabéticos: verificar_errores_input(3, 'Input alfabético del usuario')
    4. Comando inválido: verificar_errores_input(4, input_usuario, 'Lista de comandos admitidos')
    5. Item inexistente: verificar_errores_input(5, input_usuario, 'Tipo de Archivo (archivo_productos, archivo_fiados)')
    6. Item ya existente: verificar_errores_input(6, input_usuario, 'Tipo de Archivo (archivo_productos, archivo_fiados)')
    7. KEY inexistente en el diccionario:
    """
    
    archivo_productos = 'productos.json'
    archivo_fiados = 'fiados.json'
    archivo_ventas = 'ventas.json'

    # 1. No se ingresó ningún dato
    if tipo_de_error == 1:
        if len(dato_para_verificar) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡NO INGRESASTE NINGÚN DATO!")
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return True

    # 2. Solo se pueden ingresar datos numéricos
    elif tipo_de_error == 2:
        try:
            int(dato_para_verificar)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('¡SOLO PUEDES INGRESAR DATOS NUMÉRICOS!')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        else:
            pass

    # 3. Solo se pueden ingresar datos alfabéticos.
    elif tipo_de_error == 3:
        try:
            int(dato_para_verificar)
        except ValueError:
            pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('¡SOLO PUEDES INGRESAR DATOS ALFABÉTICOS!')
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return True

    # 4. Comando inválido
    elif tipo_de_error == 4:
        comandos_admitidos = []
        for comando_admitido_usuario in lista_comandos_admitidos_usuario:
            comandos_admitidos.append(comando_admitido_usuario)

        if dato_para_verificar not in comandos_admitidos:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡COMANDO INVÁLIDO! \n")
            input("Presiona Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return True

    # 5. Item inexistente
    elif tipo_de_error == 5:
        if tipo_de_archivo.lower() == 'archivo_productos':
            if verificar_nombre(dato_para_verificar, archivo_productos):
                pass
            elif verificar_errores_input(3, dato_para_verificar):
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('¡ITEM INEXISTENTE!')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                return True

        elif tipo_de_archivo.lower() == 'archivo_fiados':
            if verificar_nombre(dato_para_verificar, archivo_fiados):
                pass
            elif verificar_errores_input(3, dato_para_verificar):
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('¡ITEM INEXISTENTE!')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
    
    # 6. Item ya existente
    elif tipo_de_error == 6:
        if tipo_de_archivo.lower() == 'archivo_productos':
            if verificar_nombre(dato_para_verificar, archivo_productos):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('¡ESTE ITEM YA EXISTE!')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
                        
        elif tipo_de_archivo.lower() == 'archivo_fiados':
            if verificar_nombre(dato_para_verificar, archivo_fiados):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('¡ESTE ITEM YA EXISTE!')
                input('Presiona Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                return True

    # 7. KEY inexistente en el diccionario


def crear_archivo_guardado(archivo, tipo_de_archivo):
    """Función para que, en caso de que no exista un archivo de guardado en la carpeta de guardado, crea uno
        1. Archivo Productos, Archivo Fiados.
        2. Archivo Ventas.
    """
    
    if tipo_de_archivo.lower() == '1':
        try:
            with open(archivo, 'r') as f:
                json.load(f)
        except FileNotFoundError:
            with open(archivo, 'w') as f:
                items = []
                json.dump(items, f)
        else:
            pass

    elif tipo_de_archivo.lower() == '2':
        fecha_actual = datetime.datetime.now()
        try:
            with open(archivo, 'r') as f:
                json.load(f)
        except FileNotFoundError:
            with open("productos.json", 'r') as f:
                productos = json.load(f)
            
            items_nuevos = {}
            for item in productos:
                items_nuevos[item["nombre"]] = {str(fecha_actual.strftime('%x')): 0}
            with open(archivo, 'w') as f_object:
                json.dump(items_nuevos, f_object, indent=4)


def salir(input_usuario):
    """Función para leer si el input del usuario es igual a 'Salir'. Si es así, sale del programa que se esté utilizando """
    if input_usuario.lower() == 'salir':
        return True

"""
def guardar_ganancias(total, archivo='ganancias.txt'):
    Función para guardar todos los totales para después gestionarlos
    
    # Lee el archivo donde están las ganancias
    with open(archivo, 'r') as f:
        ganancias = f.read()

    # Suma el total de la compra al valor total del archivo "Ganancias"
    ganancias = int(ganancias) + total

    # Actualiza el archivo ganancias
    with open(archivo, 'w') as f:
        f.write(str(ganancias))
"""


def agregar_items(nombre_item, nuevo_valor_monetario, archivo, fecha_actual_mmddyy):
    """Agrega un item al archivo donde se guardan los productos"""

    # Abre el archivo
    lista_items = leer_archivo(archivo)


    # Agrega el nuevo item a la Lista
    lista_items.append({"nombre": nombre_item, "valor_monetario": int(nuevo_valor_monetario), "fecha_creacion": fecha_actual_mmddyy, "historial_modificaciones": {fecha_actual_mmddyy: {"nombre": nombre_item, "valor_monetario": nuevo_valor_monetario}}})

    # Agrega el nuevo item al archivo y acomoda sus codigos
    actualizar_archivo(lista_items, archivo)

    # Señal de que se añadió correctamente el nuevo item
    print("¡NUEVO ITEM AGREGADO!")


def eliminar_item(nombre_item, archivo):
    """Elimina un item que el usuario quiera eliminar"""

    # Lee el archivo de items y los guarda en una variable
    lista_items = leer_archivo(archivo)

    # Iteración para buscar el código del item que el usuario quiere eliminar, y eliminarlo.
    for codigo, info in enumerate(lista_items):
        if info['nombre'] == nombre_item.title():
            del(lista_items[codigo])

    # Guarda los cambios
    actualizar_archivo(lista_items, archivo)

    # Señal de que el item se eliminó
    print("¡ITEM ELIMINADO!")


def editar_item(nombre_item, nuevo_nombre, nuevo_valor_monetario, archivo):
    """Función para editar un item"""

    # Lee el archivo de los items
    items = leer_archivo(archivo)

    # Lista que va a contener los items actualizados
    nuevos_items = []

    # Si el usuario solo quiere cambiar el nombre...
    if len(nuevo_valor_monetario) == 0 and len(nuevo_nombre) > 0:
        for item in items:
            if item['nombre'] == nombre_item:
                nuevos_items.append({'nombre': nuevo_nombre, 'valor_monetario': item['precio']})
            else:
                nuevos_items.append(item)

    #Si el usuario solo quiere cambiar el precio...
    elif len(nuevo_nombre) == 0 and len(nuevo_valor_monetario) > 0:
        for item in items:
            if item['nombre'] == nombre_item:
                nuevos_items.append({'nombre': item['nombre'], 'valor_monetario': int(nuevo_valor_monetario)})
            else:
                nuevos_items.append(item)

    #Si el usuario quiere cambiar toda la información...
    elif len(nuevo_nombre) > 0 and len(nuevo_valor_monetario) > 0:
        for item in items:
            if item['nombre'] == nombre_item:
                nuevos_items.append({'nombre': nuevo_nombre, 'valor_monetario': int(nuevo_valor_monetario)})
            else:
                nuevos_items.append(item)

    #Si el usuario no cambia nada...
    elif len(nuevo_nombre) == 0 and len(nuevo_valor_monetario) == 0:
        print("¡NO SE HICIERON CAMBIOS!")


    # Guarda los cambios
    actualizar_archivo(nuevos_items, archivo)

    # Confirmación
    print("¡CAMBIO REALIZADO!")


def verificar_nombre(nombre_item, archivo):
    """Función para verificar si el nombre del item ingresado existe
    """

    # Lee el archivo con los items
    lista_items = leer_archivo(archivo)

    # Iteración para encontrar el nombre del item. Si el nombre del item existe, tira True.
    for item in lista_items:
        if item['nombre'] == nombre_item.title():
            return True


def obtener_info_item(nombre_item, archivo):
    """Función para obtener la información de un item"""

    # Lee el archivo con los items
    lista_items = leer_archivo(archivo)

    # Iteración para encontrar toda la información del item. Al encontrarla, retorna el diccionario completo
    for item in lista_items:
        if item['nombre'] == nombre_item.title():
            return item


def organizar_lista_alf(archivo):
    with open(archivo, 'r') as f_obj:
        lista_archivo = json.load(f_obj)


    nombres = []
    for item in lista_archivo:
        nombres.append(item['nombre'])

    nombres.sort()

    lista_ordenada = []
    for nombre in nombres:
        for item in lista_archivo:
            if nombre == item['nombre']:
                lista_ordenada.append(item)

    with open(archivo, 'w') as f_obj:
        json.dump(lista_ordenada, f_obj, indent=4)


def organizar_diccionario_alf(archivo):
    with open(archivo, 'r') as f_obj:
        dic_archivo = json.load(f_obj)

    nombres = []
    for producto in dic_archivo.keys():
        nombres.append(producto)
    nombres.sort()

    dic_ordenado = {}
    for nombre in nombres:
        for nombre_archivo, contenido_archivo in dic_archivo.items():
            if nombre == nombre_archivo:
                dic_ordenado[nombre] = contenido_archivo

    with open(archivo, 'w') as f_obj:
        json.dump(dic_ordenado, f_obj, indent=4)


def eliminar_item_diccionario(nombre_item, archivo):
    dic_archivo = leer_archivo(archivo)

    del dic_archivo[nombre_item.title()]

    with open(archivo, 'w') as f_obj:
        json.dump(dic_archivo, f_obj, indent=4)


def agregar_item_diccionario(nombre_item, archivo, fecha_actual_mmddyy):
    dic_archivo = leer_archivo(archivo)
    dic_archivo[nombre_item] = {fecha_actual_mmddyy: 0}

    with open(archivo, 'w') as f_obj:
        json.dump(dic_archivo, f_obj, indent=4)

    organizar_diccionario_alf(archivo)


def editar_item_diccionario(nombre_item, nuevo_nombre, archivo):
    dic_archivo = leer_archivo(archivo)
    for nombre_archivo, contenido_archivo in dic_archivo.items():
        if nombre_archivo == nombre_item:
            info_nuevo_item = contenido_archivo

    del dic_archivo[nombre_item.title()]
    dic_archivo[nuevo_nombre] = contenido_archivo
    
    with open(archivo, 'w') as f_obj:
        json.dump(dic_archivo, f_obj, indent=4)

    organizar_diccionario_alf(archivo)


def actualizar_fechas_ventas(archivo_productos_vendidos, fecha_actual_mmddyy):
    dic_archivo = leer_archivo(archivo_productos_vendidos)
    for dic_archivo_fechas in dic_archivo.values():
        if fecha_actual_mmddyy in dic_archivo_fechas.keys():
            pass
        else:
            dic_archivo_fechas[fecha_actual_mmddyy] = 0

    with open(archivo_productos_vendidos, 'w') as f:
        json.dump(dic_archivo, f, indent=4)
