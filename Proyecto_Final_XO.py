import random
import os

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")

def imprimir_tabla_numeros():
    numeros = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    imprimir_tablero(numeros)

def verificar_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ' or \
           tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ' or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return True

    return False

def movimiento_pc(tablero, jugador):
    if jugador == 'X':
        # La PC comienza colocando 'X' en el centro
        if tablero[1][1] == ' ':
            return 1, 1

    # Si no es el primer movimiento, realiza movimientos aleatorios
    opciones_disponibles = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']
    return random.choice(opciones_disponibles)

def obtener_nombre_jugador():
    return input("Ingresa tu nombre: ")

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def jugar_tres_en_raya_vs_pc():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'

    nombre_jugador = obtener_nombre_jugador()
    print(f"Bienvenido, {nombre_jugador}!")

    while True:
        limpiar_pantalla()
        imprimir_tabla_numeros()
        imprimir_tablero(tablero)

        if jugador == 'X':
            fila, columna = movimiento_pc(tablero, jugador)
            tablero[fila][columna] = jugador
        else:
            seleccion = int(input(f'{nombre_jugador}, elige una casilla (1-9): '))

            # Convertir selección de número a índices de fila y columna
            fila = (seleccion - 1) // 3
            columna = (seleccion - 1) % 3

            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = jugador
            else:
                print('¡Esa casilla ya está ocupada! Inténtalo de nuevo.')
                continue

        if verificar_ganador(tablero):
            limpiar_pantalla()
            imprimir_tablero(tablero)
            if jugador == 'X':
                print('¡La computadora ha ganado!')
            else:
                print(f'¡{nombre_jugador} ha ganado!')
            break

        # Cambiar al otro jugador
        jugador = 'O' if jugador == 'X' else 'X'

if __name__ == "__main__":
    jugar_tres_en_raya_vs_pc()