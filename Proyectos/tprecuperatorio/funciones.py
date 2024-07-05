import random
import evento
import os
import pickle

from evento import Evento

archivoBin = "eventos.dat"



def validador_mayor(cad, mayor_a_n):
    n = int(input(cad))
    while n < mayor_a_n:
        print(f"Error! El valor ingresado es menor a {mayor_a_n}. \n"
              "Intente nuevamente.\n")
        n = int(input(cad))
    return n

def menu():
    cad = '\n'\
          f'------------------------------------------------------------------------------------------------------------------------------------------------------\n' \
          'Menu de Opciones\n' \
          '------------------------------------------------------------------------------------------------------------------------------------------------------\n' \
          '1 ---> Cargar vector de eventos.\n' \
          '2 ---> Mostrar eector de eventos.\n' \
          '3 ---> Generar archivo binario de eventos.\n' \
          '4 ---> Mostrar archivo binario de eventos.\n' \
          '5 ---> Mostrar montos de producción.\n' \
          '6 ---> Buscar descripción por numero de identificación.\n' \
          '7 ---> Generar matriz de conteo.\n' \
          '8 ---> Analizar cadena de punto6.\n' \
          '0 ---> Salir.\n' \
          '------------------------------------------------------------------------------------------------------------------------------------------------------\n' \
          'Ingrese su opcion: '

    return int(input(cad))


# op1

def add_in_order(v, evento):
    izq = 0
    der = len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].codigo == evento.codigo:
            pos = med
            break

        if evento.codigo < v[med].codigo:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [evento]

def opc1(vector, n):
    for i in range(n):
        codigo = random.randint(1, 1500)
        titulo = evento.crearTitulo() + " " + str(i)
        descripcion = evento.crearDescripcion()
        costo = random.uniform(1500, 15000)
        tipo = random.randrange(0, 20)
        segmento = random.randrange(0, 10)
        ev = Evento(codigo, titulo, descripcion, costo, tipo,segmento)
        add_in_order(vector, ev)

# op2
def imprimirVector(v):
    for i in range(len(v)):
        print(v[i])

# op 3
def generarArchivo(v, mon):
    if os.path.exists(archivoBin):
        op = -1
        print('Esta opción borrara el archivo binario almacenado  ¿Desea continuar?')
        print('\t1 para Sí ')
        print('\tDiferente de 1 para No')

        op = int(input('\t-'))
        if op != 1:
            return 0

    m = open(archivoBin, 'wb')
    for ev in v:
        if ev.costo > mon:
            pickle.dump(ev, m)
    m.close()

# op 4
def imprimirArchivo(arch):
    if os.path.exists(arch):
        m = open(arch, 'rb')
        size = os.path.getsize(arch)
        print(evento.encabezado())
        while m.tell() < size:
            ev = pickle.load(m)
            print(ev)
        m.close()
    else:
        print('No existe un archivo llamado', arch)

# op 5
def generarVectorMontos(arch):
        vector = []
        m = open(arch, 'rb')
        size = os.path.getsize(arch)
        tot = 0
        while m.tell() < size:
            ev = pickle.load(m)
            if ev.tipo > 5:
                vector.append(ev.costo)
                tot += ev.costo
        m.close()
        print('Montos de producción de eventos de tipo >= 5:')
        for i in range(len(vector)):
            print(f'\t{round(vector[i], 2)}')
        prom = tot / len(vector)
        print('El promedio de costo de eventos con un numero de tipo mayor a 5 es', round(prom, 2))

# op 6
def busqueda_binaria(vec, cod):
    izq = 0
    der = len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == cod:
            return c
        if cod < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1

def op6(vec):
    cod = validador_mayor("Ingrese el codigo de identificacion del evento a buscar: ", 0)
    c = busqueda_binaria(vec, cod)
    if c != -1:
        print("_" * 150)
        print(vec[c])
        return vec[c].descripcion
    else:
        print("No existe.")
    return -1

# op7
def vali_range(r_inf, r_sup, cad):
    n = int(input(cad))
    while not r_inf <= n < r_sup:
        print(f"Error! El valor ingresado no se encuentra en el rango de tipos.\n"
              "Intente nuevamente.\n")
        n = int(input(cad))
    return n

def op7(vec):
    #filas = n = tipos de evento 0 al 19
    n = 20
    #columnas = m = segmentos 0 al 9
    m = 10
    matriz = [[0] * m for i in range(n)]
    for i in vec:
        filas = i.tipo
        columna = i.segmento
        matriz[filas][columna] += 1
    te = vali_range(0, 19, "Ingrese el tipo de evento de referencia:  ")
    print()
    for f in range(len(matriz)):
        fila = 1
        for c in range(len(matriz[f])):
            if f > te:
                if fila == 1:
                    print(f"Tipo de Evento: {f}")
                    fila = 2
                print(f"\tSegmento_{c}, Eventos: {matriz[f][c]}")

# op 8
def op8(descripcion):
    letras_palabra = 0
    if descripcion == -1:
        print("Todavia no ejecuto la opcion 6.\n"
              "Primero debe realizar esa opcion si desea correr esta opcion!!!.")
    else:
        mayuscula, T, S = False, False, False
        letras_totales, palabras_totales, palabras_M_Tt_Ss = 0, 0, 0
        for letra in descripcion:
            if letra == " " or letra == ".":
                letras_palabra = 0
                palabras_totales += 1
                if mayuscula and T and S:
                    palabras_M_Tt_Ss += 1
                mayuscula, T, S = False, False, False

            else:
                letras_palabra += 1
                if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and letras_palabra==1 :
                    mayuscula = True
                if letra in "Tt":
                    T = True
                if letra in "Ss":
                    S = True
        print(f"Cantidad de palabras que empiezan con mayúsculas, tienen al menos una T y una S: {palabras_M_Tt_Ss}")

