def display6():
    code = '''N = 4
ld = [0] * (2 * N - 1)  
rd = [0] * (2 * N - 1)   
cl = [0] * N             

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if ld[i - col + N - 1] == 0 and rd[i + col] == 0 and cl[i] == 0:
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
    return False
def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution doesn't exist")
        return False

    printSolution(board)
    return True

if __name__ == "__main__":
    solveNQ()'''
    print(code)
