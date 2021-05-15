def comparacion(lim_inferior, lim_superior, num_comparacion):
    if num_comparacion > lim_inferior and num_comparacion < lim_superior:
        print("El numero está en el rango")
    elif num_comparacion < lim_inferior:
        print("El número está por debajo del límite inferior")
    elif lim_superior == lim_inferior and num_comparacion == lim_inferior:
        print("El límite inferior no puede ser igual al límite superior") 
    else:
        print("El número está por encima del límite superior")


def run():
    opcion = True
    while opcion == True:

        lim_inferior = int(input("Ingresa un número para el límite inferior: "))
        lim_superior = int(input("Ingresa un número para el límite superior: "))
        num_comparacion = int(input("Ingresa un número de comparación: "))

        comparacion(lim_inferior, lim_superior, num_comparacion)

        repetir = input("Ingrese un número si desea repetir el proceso: ")

        if not (repetir.isnumeric()):
            opcion = False


if __name__ == "__main__":
    run()