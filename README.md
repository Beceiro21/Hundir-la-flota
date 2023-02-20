# Hundir-la-flota



## Introducción
En este ejercicio vas a crear tu propio juego de **Hundir la flota** en Python :snake: . Para el desarrollo del programa necesitarás conocimientos de la librería `numpy`, módulos, bucles, funciones y colecciones de Python. Se recomienda desarrollar el programa en un IDE como Pycharm, Visual Studio Code o Spyder. **Por lo que la entrega deberá constar de uno o varios scripts de Python (archivos .py), los que necesite el alumno**.

## ¿Cómo funciona el juego?
Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: la máquina y tú
2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto la máquina como tú tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la máquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
