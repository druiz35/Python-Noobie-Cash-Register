import json
import funciones_misc
import os


def loop_analisis_financiero(archivo):
    """Main Loop análisis financiero"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----ANÁLISIS FINANCIERO-----")
        print("ESCRIBE 'salir' PARA SALIR DE ANÁLISIS FINANCIERO")
        print('\n')
        print("Elige una opción:")
        print("1. Gestión de Costos")
        print("2. Contaduría")
        print("3. Reportes de Procesos")

        opcion = input("-->").lower()

        if funciones_misc.salir(opcion):
            break

        elif funciones_misc.verificar_errores_input(1, opcion) or funciones_misc.verificar_errores_input(4, opcion, ['salir', '1', '2', '3']):
            continue
        


def agregar_costo(nombre_costo, valor_costo, archivo, recurrencia='', tipo='', primordialidad=''):
    """Función para agregar un costo nuevo
        Recurrencia: Inmediato, Diaria, Semanal, Mensual, Anual
        Tipo: 
            -ServicioPublico(Agua, Luz, Gas) 
            -ServicioTecnologico(Internet, Telefonía)
            -ProductoTecnologico(Televisores, Teléfonos, Computadores, Videobin, Equipo de Sonido, Etc...)
            -Inmobiliario
            -Mobiliario
            -MateriaPrima(Ingredientes, Materiales, Etc...)
            -HerramientasInstrumentosMaquinariaDeTrabajo(Utensilios, Horno, Etc...)
            -Contrato(Mano de obra contratada, Mantenimiento, Aseo, Salarios Personal, Etc...)
            -Otro
        Primordialidad: 
    """
    
    # Abre el archivo
    lista_costos = funciones_misc.leer_archivo(archivo)


    # Agrega el nuevo item a la Lista
    lista_costos.append({"nombre": nombre_costo, "valor_monetario": int(valor_costo), 
                                    "recurrencia": recurrencia, "tipo": tipo, "primordialidad": primordialidad})


    # Agrega el nuevo item al archivo y acomoda sus codigos
    funciones_misc.actualizar_archivo(lista_costos, archivo)


    # Señal de que se añadió correctamente el nuevo item
    print("¡NUEVO ITEM AGREGADO!")
