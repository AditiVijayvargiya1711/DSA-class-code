def solveNQueens(n: int) -> list[list[str]]:
        board=[["."]*n for i in range(n)]
        y=[]
        def main(i):
            if i==n:
                y.append(["".join(row[:]) for row in board])
                return 
            for j in range(n):
                if placable(i,j):
                    board[i][j]="Q"
                    main(i+1)
                    board[i][j]="."
            return y
        def placable(i,j):
            for k in range(i):
                if board[k][j]=="Q":
                    return False
                if j-(i-k)>=0 and j-(i-k)<n and board[k][j-(i-k)]=="Q":
                    return False
                if j+(i-k)>=0 and j+(i-k)<n and board[k][j+(i-k)]=="Q":
                    return False
            return True

        return main(0)
print(solveNQueens(6))