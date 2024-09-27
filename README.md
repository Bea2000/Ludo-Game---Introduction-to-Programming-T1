# Ludo Game - Introduction to Programming Project

This project implements a simplified version of the classic Ludo game for two players. Each player controls two pieces, and the goal is to move both pieces to the victory zone. The game includes turns, dice rolls, and movement mechanics, as well as specific rules for entering the victory zone and rebounding when over-rolling.

This project was created as part of the **Introduction to Programming** course during the second semester of 2019, as a first-year Civil Engineering student at the **Pontificia Universidad Católica de Chile**.

## How to Run the Program

To run the game, ensure you have **Python 3** installed on your system. The main program file is named `main.py`.

1. Clone or download the repository containing the project files.
2. Open a terminal or command prompt in the project directory.
3. Execute the program with the following command:

```bash
python main.py
```

`datos.txt` is the path to a text file containing the game input. The program will read the input file, simulate the game, and display the result in the terminal.

## Example of Input Format
The input consists of:

1. The number of white tiles on the board.
2. A series of turns, each starting with a dice roll and followed by the player's action (either "Liberar" or "Avanzar").

### Sample Input

```
10
4
Avanzar
1
Avanzar
Avanzar
Liberar
5
Avanzar
2
```

## Example of Expected Output

During each player's turn, the program prints the current state of the game, including dice rolls, piece movements, and other relevant events. The game ends with a summary that shows the winner, the number of pieces each player liberated, and the final positions of the losing player's pieces.

### Sample Output

```
Ha iniciado el turno de J1
Dado: 4
Ha iniciado el turno de J2
Dado: 1
No hay fichas que avanzar
El Jugador ha liberado una ficha

Resumen Ludo
Ganador: J1
Cantidad de fichas liberadas J2: 2
Posicion ficha 1: 13
Posicion ficha 2: 16
```

## Game Rules

Players alternate turns, with Player 1 starting first.

A player can release a piece from the starting zone by rolling a 1 or a 6.

When a player rolls a 1 or 6, they can either release a piece or advance an already released piece.

If a piece is in the victory zone and the player rolls a number greater than what is needed to reach the final tile, the piece will "rebound" and move back by the excess value.

The first player to move both pieces to the final tile wins.

The game ends when one player wins, and a summary is printed.

### Additional Notes

The program ensures valid moves by checking if the selected piece can be moved according to the current game state.

Invalid moves are rejected, and the player is prompted to choose another action or piece.

The program reads input until the end of the file, simulating each turn step-by-step according to the rules of the game.
