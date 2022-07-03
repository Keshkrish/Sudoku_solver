def find_cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                return (i,j)
    return None,None
def isValid(puzzle,row,col,num):
    for i in range(9):
        if puzzle[row][i]==num:
            return False
    for i in range(9):
        if puzzle[i][col]==num:
            return False

    grid_r=(row//3)*3
    grid_c=(col//3)*3
    for i in range(grid_r,grid_r+3):
        for j in range(grid_c,grid_c+3):
            if puzzle[i][j]==num:
                return False
    return True

def Solve_Sudoku(puzzle):
    row,col=find_cell(puzzle)
    if row==None:
        return True
    for i in range(1,10):
        if isValid(puzzle,row,col,i):
            puzzle[row][col]=i
            if Solve_Sudoku(puzzle):
                return True
        puzzle[row][col]=0

    return False



