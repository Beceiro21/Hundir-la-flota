import pandas as pd
import random

tablero1 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])
tablero2 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])
tablerovacio1 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])
tablerovacio2 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])

def func_random(jugador1,jugador2):
    x = random.randint(0,6)
    y = random.randint(0,6)
    print("1º número:", x)
    print("2º número", y)
    if x > y:
        print("El jugador 1 es:",jugador1, "y el jugador 2 es:", jugador2)
        return jugador1, jugador2
    else:
        print("El jugador 1 es:",jugador2, "y el jugador 2 es:", jugador1)
        return jugador1, jugador2

""" Definimos la Clase Barco con la función colocar barco, la cual los coloca en el tablero:

df = tablero1
size = dimensiones del barco ( pequeño: 2, mediano: 3, grande: 4, gigante: 5)
fil = fila
col = columna"""

class Barco: 
    def __init__(self, df): 
        self.df = df

    def colocar_barco(self, size, df): # Introducimos el DataFrame (tablero que escogemos) y el size
        self.size = size
        while True:
            try:

                fil = int(input("Introduce la coordenada fila con números entre el 1 y el 10:")) 
                col = int(input("Introduce la coordenada columna con números entre el 1 y el 10:"))

                if isinstance((fil,col),int):
                    pass
                break
            except Exception:
                print("Por favor, inserta un número, caracter no admidido")

# Si tenemos ya barco en la coordenada introducida:
        if df.loc[fil,col] == "#" : 
            print("En esta coordenada ya hay un barco, por favor, introduce otra")
        
        else:

# Pedimos cómo queremos colocar el barco a partir de la coordenada inicial:
            h_v = input("Escribe 'h' si quieres horizontal o 'v' si quieres vertical")

# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 
            if h_v != "h" or h_v != "v":
                print("Por favor, introduzca 'h' o 'v' ")

            if h_v == "h":

                if col == 10:
                    print("Fuera de alcance")

                elif size == 5 and (col == 7 or col == 8 or col == 9):
                    print("Fuera de alcance")
                
                elif size == 4 and (col == 9 or col == 8):
                    print("Fuera de alcance")
                
                elif size == 3 and (col == 9):
                    print("Fuera de alcance")

                elif size == 2 and df.loc[fil,col + 1 ] == "#": 
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 3 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!!")
                
                elif size == 4 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

                elif size == 5 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#" or df.loc[fil,col + 4] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

            

# Si todo está bien, entonces rellena el tablero con el barco indicado:
                else:
                    fil = fil 
                    col_f = col + size - 1
            
                    df.loc[fil,col:col_f] = "#"
                    print(df)
                    return df
        

# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 
            if h_v == "v":

                if fil == 10:
                    print("Fuera de alcance")
                
                elif size == 5 and (fil == 7 or fil == 8 or fil == 9):
                    print("Fuera de alcance")
                
                elif size == 4 and (fil == 9 or fil == 8):
                    print("Fuera de alcance")
                
                elif size == 3 and (fil == 9):
                    print("Fuera de alcance")

                elif size == 2 and (df.loc[fil + 1, col] == "#"): 
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 3 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 4 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#"):
                        print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

                elif size == 5 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#" or df.loc[fil + 4 , col] == "#"):
                        print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

# Si todo está bien, ya puedes rellenar el tablero con el barco indicado:
                else: 
                    fil_f = fil + size -1
                    col = col
                    df.loc[fil:fil_f,col] = "#"
                    print(df)
                    return df


    def colocar_barco_aleatorio(self, size, df): # Introducimos el DataFrame (tablero que escogemos) y el size
        self.size = size
        while True:
            try:

                fil = int(random.randint(1,10))
                col = int(random.randint(1,10))

                if isinstance((fil,col),int):
                    pass
                break
            except Exception:
                print("Por favor, inserta un número, caracter no admidido")

# Si tenemos ya barco en la coordenada introducida:
        if df.loc[fil,col] == "#" : 
            print("En esta coordenada ya hay un barco, por favor, introduce otra")
        
        else:

# Pedimos cómo queremos colocar el barco a partir de la coordenada inicial:
            h_v = random.randint(1,2)
            if h_v == 1:
                h_v = "h"
            else:
                h_v = "v"
# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 

            if h_v == "h":

                if col == 10:
                    print("Fuera de alcance")

                elif size == 5 and (col == 7 or col == 8 or col == 9):
                    print("Fuera de alcance")
                
                elif size == 4 and (col == 9 or col == 8):
                    print("Fuera de alcance")
                
                elif size == 3 and (col == 9):
                    print("Fuera de alcance")

                elif size == 2 and df.loc[fil,col + 1 ] == "#": 
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 3 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!!")
                
                elif size == 4 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

                elif size == 5 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#" or df.loc[fil,col + 4] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

            

# Si todo está bien, entonces rellena el tablero con el barco indicado:
                else:
                    fil = fil 
                    col_f = col + size - 1
            
                    df.loc[fil,col:col_f] = "#"
                    return df
        

# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 
            if h_v == "v":

                if fil == 10:
                    print("Fuera de alcance")
                
                elif size == 5 and (fil == 7 or fil == 8 or fil == 9):
                    print("Fuera de alcance")
                
                elif size == 4 and (fil == 9 or fil == 8):
                    print("Fuera de alcance")
                
                elif size == 3 and (fil == 9):
                    print("Fuera de alcance")

                elif size == 2 and (df.loc[fil + 1, col] == "#"): 
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 3 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#"):
                    print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")
                
                elif size == 4 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#"):
                        print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

                elif size == 5 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#" or df.loc[fil + 4 , col] == "#"):
                        print("Te estás cruzando con otro barco. ¡Intentalo de nuevo!")

# Si todo está bien, ya puedes rellenar el tablero con el barco indicado:
                else: 
                    fil_f = fil + size -1
                    col = col
                    df.loc[fil:fil_f,col] = "#"
                    return df
                    
# Definimos una función para que te vaya pidiendo los barcos que hay que colocar:
# n_barcos = número de barcos que hay que introducir
# tamaño: pequeño, mediano, grande o gigante
# n: la dimensión del barco (2, 3, 4, 5)
# tablero: el tablero sobre el que colocamos los barcos


    def coloca_tus_barcos(n_barcos,barco,tamaño,n, tablero):
        contador = 1
        print("contador1:", contador)
        while contador < n_barcos: 
            print(f'Coloca el barco{contador} de tamaño {tamaño} en el tablero')
            
            if type(barco.colocar_barco(n,tablero)) != pd.core.frame.DataFrame:
                print("Try Again!") 
                contador -= 1
            contador += 1

        return tablero


    def coloca_tus_barcos_ale(n_barcos,barco,tamaño,n, tablero):
        contador = 1
        print("contador1:", contador)
        while contador < n_barcos: 
            print(f'Coloca el barco{contador} de tamaño {tamaño} en el tablero')
            
            if type(barco.colocar_barco_aleatorio(n,tablero)) != pd.core.frame.DataFrame:
                print("Try Again!") 
                contador -= 1
            contador += 1

        return tablero
barco_pequeño = Barco(tablero1)
barco_mediano = Barco(tablero1)
barco_grande = Barco(tablero1)
barco_gigante = Barco(tablero1)


def coloca_jugador1():
    Barco.coloca_tus_barcos(2, barco_gigante, "gigante", 5, tablero1)
    Barco.coloca_tus_barcos(3, barco_grande, "grande", 4, tablero1)
    Barco.coloca_tus_barcos(4, barco_mediano, "mediano", 3, tablero1)
    Barco.coloca_tus_barcos(5, barco_pequeño, "pequeño", 2, tablero1)
def coloca_maquina():
    Barco.coloca_tus_barcos_ale(2, barco_gigante, "gigante", 5, tablero2)
    Barco.coloca_tus_barcos_ale(3, barco_grande, "grande", 4, tablero2)
    Barco.coloca_tus_barcos_ale(4, barco_mediano, "mediano", 3, tablero2)
    Barco.coloca_tus_barcos_ale(5, barco_pequeño, "pequeño", 2, tablero2)

class jugador1:
    def __init__(self, nombre,tablero1,tablerovacio1):
        self.nombre = nombre
        self.tablerovacio1 = tablerovacio1
        self.tablero1 = tablero1
    def atacar(self, jugador2):
        fil=int(input("Introduce la fila"))
        col=int(input("Introduce la columna"))
        try:
            if jugador2.tablero2.loc[fil,col]== "#":
                jugador2.tablero2.loc[fil,col]="X"
                self.tablerovacio1.loc[fil,col] = "X"
                print("Has atacado en:","\n", self.tablerovacio1)
                print("Tus barcos son:","\n", self.tablero1)
                return self.tablerovacio1, self.tablero1
            elif jugador2.tablero2.loc[fil,col]== "~":
                self.tablerovacio1.loc[fil,col]="O"
                jugador2.tablero2.loc[fil,col]="O"
                print("Has atacado en:","\n", self.tablerovacio1)
                print("Tus barcos son:","\n", self.tablero1)
                return self.tablerovacio1, self.tablero1
            elif jugador2.tablero2.loc[fil,col]=="X" or jugador2.tablero2.loc[fil,col]=="O":
                print("Ya has atacado aqui")
                self.atacar(jugador2)
        except Exception:
            print("Algo ha ido mal, intentalo de nuevo")
            self.atacar(jugador2)


class jugador2:
    def __init__(self, nombre,tablero2,tablerovacio2):
        self.nombre = nombre
        self.tablerovacio2 = tablerovacio2
        self.tablero2 = tablero2
    def atacar(self, jugador1):
        fil=random.randint(1,10)
        col=random.randint(1,10)
        try:
            if jugador1.tablero1.loc[fil,col]== "#":
                jugador1.tablero1.loc[fil,col]="X"
                self.tablerovacio2.loc[fil,col] = "X"
                print("Has atacado en:","\n", self.tablerovacio2)
                print("Tus barcos son:","\n", self.tablero2)
                return self.tablerovacio2, self.tablero2
            elif jugador1.tablero1.loc[fil,col]== "~":
                self.tablerovacio2.loc[fil,col]="O"
                jugador1.tablero1.loc[fil,col]="O"
                print("Te han atacado en:","\n", self.tablerovacio2)
                return self.tablerovacio2, self.tablero2
            elif jugador1.tablero1.loc[fil,col]=="X" or jugador1.tablero1.loc[fil,col]=="O":
                print("Ya has atacado aqui")
                self.atacar(jugador1)
        except Exception:
            print("Algo ha ido mal, intentalo de nuevo")
            self.atacar(jugador2)


jugador1 = jugador1(nombre='Jugador 1',tablero1 =tablero1, tablerovacio1= tablerovacio1)
jugador2 = jugador2(nombre='Jugador 2',tablero2 =tablero2, tablerovacio2= tablerovacio2)
