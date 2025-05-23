# Gato (Tic-Tac-Toe)

## Descripción
Este es un juego de Gato (también conocido como Tic-Tac-Toe o 3 en raya) que permite jugar contra una máquina. El juego se desarrolla en una cuadrícula de 3x3 donde los jugadores alternan turnos para colocar sus marcas (X o O) en las celdas vacías.
Este es un juego singleplayer donde compites contra la maquina, en un Tic-Tac-Toe en la linea de comandos..

## Requisitos
- Python 3.x

## Cómo Jugar
1. Ejecuta el script `main.py`.
2. El juego comenzará y te indicará si es tu turno o el de la máquina.
3. Si es tu turno, ingresa la fila y la columna donde deseas colocar tu marca (0, 1 o 2). El formato es primero fila (del 0 al 2) y luego columna (del 0 al 2), por ejemplo 0 2, el cual lo pondría el la primera fila y ultima columna.
4. La máquina jugará automáticamente después de tu turno.
5. El juego continuará hasta que haya un ganador o un empate.

## Funciones Principales
- `printMat()`: Imprime el estado actual del tablero.
- `updateMat(row, col, player)`: Actualiza el tablero con la marca del jugador si la celda está vacía.
- `checkWin(player)`: Verifica si el jugador ha ganado.
- `checkDraw()`: Verifica si el juego ha terminado en empate.

## Ejecución
Para ejecutar el juego, utiliza el siguiente comando en tu terminal:

   ```bash
   python main.py
   ```


## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el juego, siéntete libre de hacer un fork del repositorio y enviar un pull request.

## Posibles mejoras
1. Implementarle un contador de victorias y derrotas.
2. Añadirle ML a las desiciones de la computadora. Ya que elige de forma totalmente random.
3. Añadirle niveles de dificultad.
    - Básico: Con desiciones random como está actualmente
    - Medio: Un nivel de ML jugable
    - Imposible: Que sepa jugar tanto que sea entre un 99% de chances de ganar o imposible.

- Cualquier otra sugerencia, no dudes en mandar un PR.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.