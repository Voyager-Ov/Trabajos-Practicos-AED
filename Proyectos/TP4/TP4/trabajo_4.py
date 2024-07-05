from funciones import *

paises = [  # paises en los que se puede COBRAR en su respectivo orden de craga
    "Argentina",
    "Bolivia",
    "Brasil",
    "Paraguay",
    "Uruguay",
]
vehiculos = ["motocicletas ", "automoviles ", "camiones"]  # tipos de vehículos en su respectivo orden de carga


def principal():
    op = -1
    matriz = []
    while op != 0:
        print("\nMenú de opciones:")
        print("1. Cargar tickets a un archivo binario desde archivo.csv")
        print("2. Almacenar ticket manualmente")
        print("3. Mostrar tickets almacenados")
        print("4. Buscar ticket por patente")
        print("5. Buscar ticket por código de identificación")
        print("6. Mostrar cantidad de vehículos que pasaron por las cabinas de cada pais")
        print("7. Mostrar cantidad total de vehículos por tipo y pais")
        print("8. Mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos")
        print("0. Salir")

        op = input("ingrese su opción: ")

        if op == "1":
            op1()
        elif op == "2":
            op2()
        elif op == "3":
            op3()
        elif op == "4":
            op4()
        elif op == "5":
            print("ingrese el código identificador que desea buscar.")
            cod = int(input("(en caso de ingresar menos de 10 dígitos se llegara a los 10 con ceros a la izquierda "
                            "automáticamente): "))
            # si no tiene 10 digitos lo llenamos de ceros al inicio hasta llegar a 10 digitos
            if len(str(cod)) != 10:
                o = "0" * (10 - len(str(cod)))
                cod = o + str(cod)
            op5(cod)
        elif op == "6":
            matriz = op6()
            cant = len(matriz)
            for i in range(cant):
                # también podemos poner 5, pero para hacerlo escalable lo dejamos asi
                j = len(matriz[i])
                for k in range(j):
                    print("cantidad de", vehiculos[i], "que pasaron por el pais ", paises[k], "son:", matriz[i][k])
        elif op == "7":
            op7(matriz)
        elif op == "8":
            op8()
        elif op == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()
