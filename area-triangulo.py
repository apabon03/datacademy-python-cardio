def tipo_triangulo(lado_a, lado_b, lado_c):
    if lado_a== lado_b and lado_b == lado_c:
        print("El triángulo es equilatero")
    elif lado_a != lado_b and lado_b == lado_c:
        print("El triángulo es Isósceles")
    else:
        print("El triángulo es Escaleno")


def area(base, altura):
    return (base * altura)/2


def run():
    menu = True
    while menu == True:
        opcion = input('''
            Menú:
            1. Área del triángulo.
            2. Tipo de triángulo: Escaleno, Isósceles, Equilátero
            3. Salir del programa.

            Bienvenido, elige qué deseas calcular: ''')
        
        if opcion == '1':

            base = int(input("Ingresa la base: "))
            altura = int(input("Ingresa la altura: "))
            print(f'El área del triángulo es: {area(base, altura)}')
            

        elif opcion == '2':
            lado_a = int(input("Ingresa el primer lado: "))
            lado_b = int(input("Ingresa el segundo lado: "))
            lado_c = int(input("Ingresa el tercer lado: "))
            tipo_triangulo(lado_a, lado_b, lado_c)
            

        elif opcion == '3':
            menu = False
        else:
            print("Ingrese una opción válida: ")

if __name__ == "__main__":
    run()