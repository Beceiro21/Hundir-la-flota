
from hundir import Barco
from hundir import func_random
from hundir import jugador1
from hundir import jugador2
from hundir import coloca_jugador1
from hundir import coloca_jugador2

##Aquí empieza el juego!##
print("¡Que empiece el juego!")
print()
import time
turno = 1

func_random(input("Nombre 1"),input("Nombre 2"))
print()
print("Coloca jugador 1""\n")
coloca_jugador1()
print()
print("Coloca jugador 2""\n")
coloca_jugador2()


while "#" in jugador1.tablero1.values or "#" in jugador2.tablero2.values:

    print("Turno:", turno)
    time.sleep(1)
    print("Ataca el jugador 1")
    jugador1.atacar(jugador2)
    print("Ataca el jugador 2")
    jugador2.atacar(jugador1)
    turno = turno + 1
    print("---------")

else:
    if "#" in jugador1.tablero1.values:
        print("¡Gana el jugador 1!")
    elif "#" in jugador2.tablero2.values:
        print("¡Gana el jugador 2!")
    else:
        "GAME OVER, caputto"
