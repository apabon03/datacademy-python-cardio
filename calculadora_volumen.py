from math import pi


def area_cuadrado(lado):
    if lado >0:
        print(f"El área del cuadrado es: {lado*lado}")
    else:
        print("Ingresa un valor positivo")


def area_circulo(radio):
    if radio > 0:
        print(f'El área del círculo es: {round(pi * (radio**2), 2)}')
    else:
        print("Ingresa valores positivos")

def volumen_cilindro(radio, altura):
    if radio >0 and altura >0:
        volumen = pi * (radio**2) * altura
        print(f'El volumen del cilindro es: {round(volumen, 2)} cm3')
    else:
        print("Ingresa valores Positivos")



def run():
    estado = True

    while estado == True:
        opcion = input('''
        Menú:
        1.Calcular volúmen del cilindro
        2.Calcular área del círculo
        3.Calcular área del cuadrado
        4.Salir del programa

        Elige una opción: ''')


        if opcion == '1':

            radio = int(input("Ingresa el radio del cilindro: "))
            altura = int(input("Ingresa la altura del cilindro: "))
            volumen_cilindro(radio, altura)


        elif opcion== '2':

            radio = int(input("Ingresa el radio del círculo: "))
            area_circulo(radio)


        elif opcion == '3':
            lado = int(input("Ingresa un el lado del cuadrado: "))
            area_cuadrado(lado)

        elif opcion == '4':
            estado = False
        
        else:
            print("Ingrese una opción válida")



if __name__ == "__main__":
    run()