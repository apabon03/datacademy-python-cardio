def km_millas(km):
    if km > 0:
        return km * 0.621371
    else:
        print("Ingrese una cantidad de km positiva")

def millas_km(millas):
    if millas > 0:
        return millas * 1.609344
    else:
        print("Ingrese una cantidad de millas positiva")

def run():
    estado = True
    while estado == True:
        opcion = input('''
        Menú:
        1. Millas a Kilómetros
        2. Kilómetros a Millas
        3.Salir del programa

        Elige un opción: ''')

        if opcion == '1':
            millas = int(input("Ingrese una cantidad en millas: "))
            print(f'{millas_km(millas)} km')
            

        elif opcion == '2':
            km = int(input("Ingrese una cantidad en km: "))
            print(f'{km_millas(km)} millas')
            

        elif opcion == '3':
            estado = False
        else:
            print("Ingresa una opción válida: ")


if __name__ == "__main__":
    run()