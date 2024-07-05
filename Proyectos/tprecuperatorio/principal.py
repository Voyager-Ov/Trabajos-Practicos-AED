from funciones import *
import os

def principal():
    vec = []
    opc = -1
    cargado = False
    archivoCargado = False
    archivoBin = 'eventos.dat'
    descripcion = -1
    while opc != 0:
        opc = menu()
        print()
        if opc == 1:
            cant = validador_mayor("Ingrese cantidad de Eventos a generar: ", 0)
            opc1(vec, cant)
            cargado = True
            print("Vector cargado correctamente")
        if opc == 2:
            if cargado:
                print(evento.encabezado())
                imprimirVector(vec)
            else:
                print("Error! No hay cargas en el vector.\nVuelva a la opción 1.")
        if opc == 3:
            if cargado:
                monto = int(input("Ingrese el monto minimo de producción a guardar en el archivo: "))
                generarArchivo(vec, monto)
                archivoCargado = True
            else:
                print("Primero debe generar el vector, elija la opción 1")
        if opc == 4:
            if os.path.exists(archivoBin):
                imprimirArchivo(archivoBin)
            else:
                print('primero debe generar el archivo binario, elija la opción 3')
        if opc == 5:
            if os.path.exists(archivoBin):
                generarVectorMontos(archivoBin)
        elif opc == 6:
            descripcion = op6(vec)
        elif opc == 7:
            op7(vec)
        elif opc == 8:
            op8(descripcion)

print('\nFin del programa.')

if __name__ == '__main__':
    principal()
