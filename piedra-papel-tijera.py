def ganador(elemento1, elemento2):
    if (elemento1 == 'piedra' and elemento2 == 'papel') or (elemento1 == 'papel' and elemento2 == 'tijera') or (elemento1 == 'tijera' and elemento2 == 'piedra'):
        return 2

    elif (elemento1 == 'piedra' and elemento2 == 'tijera') or (elemento1 == 'papel' and elemento2 == 'piedra') or   (elemento1 == 'tijera' and elemento2 == 'papel'):
        return 1
    else: 
        return 0



def run():
    win_player_1 = 0
    win_player_2 = 0
    empates = 0
    estado = True

    while estado == True:

        opcion_jugador_1 = input("P1, Ingresa un opcion (piedra, papel o tijera):  ")
        opcion_jugador_2 = input("P2, Ingresa un opcion (piedra, papel o tijera):  ")
        valor = ganador(opcion_jugador_1, opcion_jugador_2)
        if valor == 1:
            win_player_1 += 1
            if win_player_1 < 2:
                
                print(f'P1: {win_player_1}\nP2: {win_player_2}\nEmpates: {empates}\n')
            else:
                print("El ganador es el jugador 1!!")
                estado = False

        elif valor == 2:
            win_player_2 += 1
            if win_player_2 < 2:
                
                print(f'P1: {win_player_1}\nP2: {win_player_2}\nEmpates: {empates}\n')
            else:
                print("El ganador es el jugador 2!!")
                estado = False
        else:
            empates += 1
            print(f'P1: {win_player_1}\nP2: {win_player_2}\nEmpates: {empates}')



if __name__ == "__main__":
    run()