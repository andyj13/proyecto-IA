# proyecto-IA
Juego 4 en línea

Entradas:
-	Coordenadas de la matriz
-	Estado de la posición
Estados de posición de la matriz:
-	0 = en blanco 
-	1 = jugador
-	2 = agente inteligente 
Como recibir los datos:

El agente inteligente deberá de hacer un recorrido para verificar el estado de la matriz, al inicio del juego se puede encontrar con dos opciones:

Agente Inteligente - azul
Jugador - rojo 

1-	Que la matriz se encuentre en blanco, si ese es el caso se puede optar por iniciar desde el centro de la matriz.
	
2-	Que el jugador haya iniciado con el primer movimiento, en este caso se pueden tomar varias estrategias, si el jugador eligió uno de los lados, empezar por la mitad

Si el jugador empezó por la mitad, utilizar los lados

Colocarse encima de la ficha del oponente.
 
O colocarse a la par, cuando el jugador comience una jugada.
 
Entrenamiento:

Para entrenar al Agente Inteligente, se empezará si es primero la primera jugada siempre será en medio, caso contrario que sea segundo, anteriormente se explican unas estrategias, después del movimiento del jugador se buscara que el agente complete 4 posiciones consecutivas, ya sean horizontales, verticales o diagonales.

También se le puede enseñar a partir de los movimientos del jugador

Después de que aprenda lo básico el siguiente entrenamiento es que el agente pueda  crear una estrategia, por ejemplo: intentar ocupar tres posiciones, desde el centro hacia los lados.


	Una variante de las tres posiciones puede ser:
                               


También tratar de hacer una fila de tres en diagonal vinculada a una de tres horizontal, así el jugador solo puede bloquear una, para perder al siguiente turno.

Interacción:
Se puede notar que el modo como se comunicara el agente será a través de matriz visual, ya sea que el inicie una jugada o el jugador empiece, Cada vez que se realice un movimiento la salida del agente será otro movimiento intentando completar cuatro puntos consecutivos.
Después de que el agente sea entrenado será capaz de dar una dificultad al jugador 

