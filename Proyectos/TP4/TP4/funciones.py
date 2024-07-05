from clases import *
import pickle
import os.path

ruta = 'peajes-tp4.csv'
bin = 'datos.dat'
paises = [  # paises en los que se puede COBRAR en su respectivo orden de craga
    "Argentina",
    "Bolivia",
    "Brasil",
    "Paraguay",
    "Uruguay",
]
vehiculos = ["motocicletas", "automoviles", "camiones"]  # tipos de vehiculos en sus respectivo orden de carga


def op1():
    op = 0
    if os.path.exists("datos.dat"):
        print("Ya existe un archivo binario cargado con tickets desde un archivo.csv")
        print("Desea borrar esos tickets almacenados y cargar unicamente con los del archivo")
        print("1_Si\n"
              "2_No")
        op = int(input("Ingrese su opcion: "))
    else:
        cont = 0
        archivo = open(ruta)  # archivo de texto csv de donde vienen los datos
        datos = open(bin, "wb")  # archivo de datos de tipo binario
        for line in archivo:
            cont += 1
            a = line.split(",")
            if cont > 2:
                t = Ticket(a[0], a[1], a[2], a[3], a[4], a[5])
                pickle.dump(t, datos)
        archivo.close()
        datos.close()
        print("datos cargados correctamente.")
    if op == 1:
        cont = 0
        archivo = open(ruta) #archivo de texto csv de donde vienen los datos
        datos = open(bin, "wb") #archivo de datos de tipo binario
        for line in archivo:
            cont += 1
            a = line.split(",")
            if cont > 2:
                t = Ticket(a[0],a[1],a[2],a[3],a[4],a[5])
                pickle.dump(t,datos)
        archivo.close()
        datos.close()
        print("datos cargados correctamente.")
    elif op == 2:
        print("Los datos no se sobreescribieron")


def validacion_incorrecta_por_cantidad(n, subclase, condicion):
    while len(subclase) != int(n):
        print("no se cumple " + condicion)
        subclase = input("ingrese de nuevo los parametros: ")
        # verifica que la cantidad de numeros ingresados en la subclase sdea la de n y la condicion es el mensaje de error


def validacion_incorrecta_por_numero(desde, hasta, subclase, condicion):
    while not (desde <= int(subclase) <= hasta):
        print("no se cumple " + condicion)
        subclase = input("ingrese de nuevo los parametros: ")
    # valida que el valor de subclase este entre esos dos numeros desde y hasta,


def detectar_pais_por_patente(patente):
    valores_numericos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    patron = []

    for caracter in patente[:7]:
        if caracter == ' ':
            patron.append('_')
        elif caracter in valores_numericos:
            patron.append('N')
        else:
            patron.append('L')

    if patron == ['L', 'L', 'N', 'N', 'N', 'L', 'L']:
        origen_patente = 1  # "Argentina"
    elif patron == ['L', 'L', 'N', 'N', 'N', 'N', 'N']:
        origen_patente = 3  # "Bolivia"
    elif patron == ['L', 'L', 'L', 'N', 'L', 'N', 'N']:
        origen_patente = 2  # "Brasil"
    elif patron == ['_', 'L', 'L', 'L', 'L', 'N', 'N']:
        origen_patente = 0  # "Chile"
    elif patron == ['L', 'L', 'L', 'L', 'N', 'N', 'N']:
        origen_patente = 4  # "Paraguay"
    elif patron == ['L', 'L', 'L', 'N', 'N', 'N', 'N']:
        origen_patente = 5  # "Uruguay"
    else:
        origen_patente = 6  # "otros"

    return origen_patente


def op2():  # carga manual de un ticket
    print("ingrese el código identificador de 10 digitos")
    cod = int(input("(en caso de ingresar menos se llegara a los 10 digitos con ceros a la izquierda): "))
    # si no tiene 10 digitos lo llenamos de ceros al inicio hasta llegar a 10 digitos
    if (len(str(cod)) != 10):
        o = "0" * (10 - len(str(cod)))
        cod = o + str(cod)
    pat = input(
        "\nIngrese la patente del vehiculo 7 caracteres alfanuméricos.\n"
        "Recuerde que si es de Chile, el primer carácter debe ser un espacio: "
    )
    validacion_incorrecta_por_cantidad("7", pat, "con la patente")
    vehiculo = int(
        input(
            "\nTIPO DE VEHICULO\n"
            "0 - Si es una moto.\n"
            "1 - Si es un auto.\n"
            "2 - Si es un camión.\n"
            "Ingrese el tipo de vehiculo: "
        )
    )
    validacion_incorrecta_por_numero(0, 2, vehiculo, "con el tipo de vehiculo")
    pago = int(
        input(
            "\nFORMA DE PAGO\n"
            "1 - Si es manual.\n"
            "2 - Si es telepeaje.\n"
            "Ingrese la forma de pago: "
        )
    )
    validacion_incorrecta_por_numero(1, 2, pago, "con la forma de pago")
    paisdecobro = int(
        input(
            "\nPAIS\n"
            "0 - Argentina.\n"
            "1 - Bolivia.\n"
            "2 - Brasil.\n"
            "3 - Paraguay.\n"
            "4 - Uruguay.\n"
            "Ingrese el país donde nos encontramos: "
        )
    )
    validacion_incorrecta_por_numero(
        0, 4, paisdecobro, "con el pais en donde nos encontramos"
    )
    # en ninguna parte el enunciado dice que no pueden ser mas de tres digitos, solo dice que asi viene en el
    # archivo txt, lo que si por logica no puede ser menor de 0 (tambien dice el enunciado que puede ser 0)
    distancia = int(input(
        "\nIngrese la cantidad de km recorridos.\n"
    ))
    while distancia < 0:
        distancia = int(input("la distancia debe ser 0 o mayor a 0, intente nuevamente: "))

    t = Ticket(cod, pat, vehiculo, pago, paisdecobro, distancia)
    datos = open(bin, "ab")
    pickle.dump(t, datos)
    datos.close()


# definición de una función que ordena al vector v de menor a mayor según su codigo de verificacion
def ordenar_menor_mayor(v):
    n = len(v)
    if n > 1:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v[i].codigo > v[j].codigo:
                    v[i].codigo, v[j].codigo = v[j].codigo, v[i].codigo
    return v


def op3():
    if os.path.exists(bin):
        t = os.path.getsize(bin)  # tamaño del archivo
        datos = open(bin, 'rb')
        print("los registros que guardados en el archivo son :")
        # se usa el método tell() para controlar si el valor del file pointer (el puntero del archivo)
        # del archivo gestionado con 'datos' es menor que el tamaño en bytes del archivo (ficha 23)
        while datos.tell() < t:
            tick = pickle.load(datos)  # tickets en el archivo de datos
            print(tick)
        datos.close()
    else:
        print("primero debe cargar datos, elija opcion 1 o 2")


def op4():
    patente = input("\nDigite la patente a buscar:")
    tam = os.path.getsize(bin)
    file = open(bin, 'rb')
    contador = 0
    encontro = False
    while file.tell() < tam:

        ticket = pickle.load(file)
        # comparar cada ticket del archivo binario con la patente que le pasas a la funcion
        if ticket.patente == patente:
            print('\n', ticket, '\n')
            contador += 1
            encontro = True
            pass

    file.close()
    # Mostrar el número de registros mostrados
    if encontro:
        print(f"Se mostraron {contador} registros con la patente {patente}\n")
    else:
        print(f"No se encontraron patentes iguales a la ingresada.\n"
              f"Patente ingresada:  {patente}\n")


def op5(num):
    bandera = None
    if not os.path.exists(bin):
        print('El archivo', bin, 'no existe...')
        return

    m = open(bin, "rb")
    t = os.path.getsize(bin)

    while m.tell() < t:
        bandera= False
        # buscamos en el archivo binario cada ticket guardado
        tickGuardado = pickle.load(m)
        if tickGuardado.codigo == num:
            print(tickGuardado)
            bandera = True
            break
    #una vez recorrido el archivo, lo cerramos
    m.close()
    #con la bandera sabemos si fue encontrado un registro o no, si no fue encontrado le avisamos al usuario
    if(bandera == False):
        print ("no se encontro ningun registro con el codigo identificador",num)




def op6():  # devuelve la matriz bi dimensional para ser usada en el print del main y en el punto 7
    if os.path.exists(bin):
        # Listado de paises
        conteo_combinacion = [[0] * 5, [0] * 5, [0] * 5]
        t = os.path.getsize(bin)  # tamaño del archivo
        datos = open(bin, 'rb')
        print("los registros que guardados en el archivo son :")
        # se usa el método tell() para controlar si el valor del file pointer (el puntero del archivo)
        # del archivo gestionado con 'datos' es menor que el tamaño en bytes del archivo (ficha 23)
        while datos.tell() < t:
            tick = pickle.load(datos)  # tickets en el archivo de datos
            vehiculo = int(tick.vehiculo)
            pais = int(tick.paisdecobro)
            conteo_combinacion[vehiculo][pais] += 1
        datos.close()

        return conteo_combinacion
    else:
        print("primero debe cargar datos, elija opcion 1 o 2")


def totalizador_vehiculos(matriz):
    m = len(matriz)
    n = len(matriz[0])
    q = -1
    print("Cantidad total de vehículos contados por cada tipo de vehículo posible")
    for f in range(m):
        ac = 0
        q += 1
        for c in range(n):
            ac += matriz[f][c]
        print(vehiculos[q] + ": ", ac)


def totalizador_paises(matriz):
    m = len(matriz)
    n = len(matriz[0])
    q = -1
    print("Cantidad de vehículos que pasan por cada pais")
    for c in range(n):
        ac = 0
        q += 1
        for f in range(m):
            ac += matriz[f][c]
        print(paises[q] + ": ", ac)


def op7(matriz):
    if matriz == []:
        matriz = op6()
    totalizador_vehiculos(matriz)
    totalizador_paises(matriz)


def calcular_monto(ticket):
    pais = paises[(detectar_pais_por_patente(ticket.patente))]
    if pais == "Bolivia":
        monto = 200
    elif pais == "Brasil":
        monto = 400
    else:
        monto = 300

    if ticket.pago == 1 and ticket.vehiculo == 0:
        monto = monto / 2
    if ticket.pago == 1 and ticket.vehiculo == 1:
        monto = monto
    if ticket.pago == 1 and ticket.vehiculo == 2:
        monto = monto + ((monto * 60) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 0:
        monto = (monto / 2) - ((10 * (monto / 2)) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 1:
        monto = monto - ((10 * monto) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 2:
        monto = (
                monto + ((monto * 60) / 100) - (((monto + ((monto * 60) / 100)) * 10) / 100)
        )

    return monto


def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].distancia > temp.distancia:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def op8():
    #Funcion de Nano
    if os.path.exists(bin):
            t = os.path.getsize(bin)  # Tamaño del archivo
            datos = open(bin, 'rb')

        # Paso 1: Calcular la distancia promedio
            total_distancia = 0
            total_registros = 0

            while datos.tell() < t:
                ticket = pickle.load(datos)  # Tickets en el archivo de datos
                distancia = int(ticket.distancia)
                total_distancia += distancia
                total_registros += 1

            distancia_promedio = total_distancia // total_registros

            # Paso 2: Crear un arreglo de objetos con distancias superiores a la distancia promedio
            datos.seek(0)  # Regresar el puntero al inicio del archivo

            total = 0
            tickets = []
            while datos.tell() < t:
                ticket = pickle.load(datos)
                distancia = int(ticket.distancia)
                if distancia > distancia_promedio:
                    tickets.append(ticket)
                    total += 1

            datos.close()

        # Paso 3: Aplicar Shellsort para ordenar el arreglo de objetos por distancia recorrida
            shellsort(tickets)

            # Imprimir el arreglo ordenado
            print("Los vehículos con mayor distancia al promedio guardados en el archivo son:")
            for ticket in tickets:
                print(f"TICKET: {ticket}")
    else:
        print("Primero debe cargar datos, elija opción 1 o 2")
    print("Distancia promedio desde la ultima cabina entre todos los tickets:", distancia_promedio)

    return True

   
