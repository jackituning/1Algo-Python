def Getboardsize():
    while True:
            n = int(input("Taille plateau ? "))
            if n > 2: 
                return n
            else:
                print("La taille doit être un entier supérieur à 2.")


def possiblesquare(board, n, player, i, j):
    if board[i][j] != 0:
        return False

    if i > 0 and board[i-1][j] != 0 and board[i-1][j] != player:
        return False
    if i < n - 1 and board[i+1][j] != 0 and board[i+1][j] != player:
        return False
    if j > 0 and board[i][j-1] != 0 and board[i][j-1] != player:
        return False
    if j < n - 1 and board[i][j+1] != 0 and board[i][j+1] != player:
        return False

    return True

def Selectsquare(board, n, player):
    while True:   
        i = int(input(f"joueur {player} coordoné i ? "))
        j = int(input(f"joueur {player} coordoné j ? "))
        if 0 <= i < n and 0 <= j < n and possiblesquare(board, n, player, i, j):
            return i, j

def Updateboard(board, player, i, j):
    board[i][j] = player 

def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if possiblesquare(board, n, player, i, j):
                return True
    return False

def displayboard(board, n):
    
    for i in range(n):
        ligne = f"{i + 1} | "  
        for j in range(n):
            if board[i][j] == 0:
                ligne += ". "  
            elif board[i][j] == 1:
                ligne += "o " 
            elif board[i][j] == 2:
                ligne += "x " 
        print(ligne) 

    print("   " + "‾" * (2 * n + 1))  
    

    colonnes = "   "
    for j in range(n):
        colonnes += f"{j + 1} "
    print(colonnes)

def snort():
    n = Getboardsize()
    
    board = [[0] * n for i in range(n)]
    
    player = 1 
    while True:
        displayboard(board, n) 

        i, j = Selectsquare(board, n, player)
        Updateboard(board, player, i, j)

        if not again(board, n, 3 - player):
            displayboard(board, n)
            print(f"Le player {player} a gagné !")
            break

        player = 3 - player

snort()