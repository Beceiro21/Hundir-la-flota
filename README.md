# Hundir-la-flota 🌊


## Introducción 📝
En este ejercicio vas a crear tu propio juego de **Hundir la flota** en Python :snake: . Para el desarrollo del programa necesitarás conocimientos de la librería `pandas`, módulos, bucles, funciones y colecciones de Python. 

## ¿Cómo funciona el juego? :video_game: 

Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: :smile:

2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos pequeños
    * 3 barcos normales
    * 2 barcos grandes
    * 1 barco gigante

4. Tanto la máquina como tú tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la máquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.

## Descripción: :heavy_exclamation_mark:


En el archivo "hundir.py" importamos las librerías que neceistamos, creamos los objetos y definimos funciones.

1. En primer lugar creamos los tableros (2 por jugador).
2. Después definimos la función random para definir quien juega primero.
3. Definimos las clases para colocar los barcos en el tablero con el tamaño correspondiente, (de gigante a mas pequeño).
4. Definimos la función para colocar un barco aleatorio.
5. Funciones para colocar los barcos de manera manual y aleatoria.
6. Y por último las clases para definir el jugador1 y al jugador2.

Y en el archivo batalla naval, ¡empieza el juego!

1. importamos las funciones necesarias.
2. Y ¡¡A JUGAR!!


## Autores 	:black_nib:

Alberto 

Fernando Martínez
