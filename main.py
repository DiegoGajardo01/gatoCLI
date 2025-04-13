import random
M1 = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
bcl = True

print("Bienvenido al gato (tiptaptoe, 3 en raya)")

turno = random.randint(0, 1)
if turno == 1:
    print("Empieza la maquina\n")
else:
    print("Es tu turno de jugar\n")



def printMat():
    print("\n")
    for row in M1:
        print(" | ".join(row))
        print("-" * 9)

def updateMat(row, col, player):
    print("\n")
    if M1[row][col] == "-":
        M1[row][col] = player
        return True
    return False

def checkWin(player):
    for i in range(3):
        if all(M1[i][j] == player for j in range(3)) or all(M1[j][i] == player for j in range(3)):
            return True
    if all(M1[i][i] == player for i in range(3)) or all(M1[i][2 - i] == player for i in range(3)):
        return True
    return False

def checkDraw():
    return all(cell != "-" for row in M1 for cell in row)

printMat()

while bcl: 
    if turno == 1:
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if updateMat(row, col, "O"):
                break
        print("La máquina ha jugado:")
    else:
        print("Es tu turno de jugar. Ingresa fila y columna (0 2):")
        row, col = map(int, input().split())
        if updateMat(row, col, "X"):
            print("Has jugado:")
        else:
            print("Movimiento inválido, intenta de nuevo.")
            continue

    printMat()
    
    if checkWin("O"):
        print("Haz perdido. más suerte en la próxima")
        break
    elif checkWin("X"):
        print("Haz ganado")
        break
    elif checkDraw():
        print("Haz empatado")
        break

    turno = 1 - turno