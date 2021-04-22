def check_rows(grid): # Function to verify if a row is valid
    for i in grid:
        if 1 not in i or 2 not in i or 3 not in i or 4 not in i or 5 not in i or 6 not in i or 7 not in i or 8 not in i or 9 not in i:
            return False
        if 1 in i and 2 in i and 3 in i and 4 in i and 5 in i and 6 in i and 7 in i and 8 in i and 9 in i:
            for j in i:
                contador = i.count(j)
                if contador != 1:
                    return False
    return True

def check_cols(grille): # Function to verify in a column is valid, where a column is converted into a row and verified bt the check_rows function
    coluna1 = []
    coluna2 = []
    coluna3 = []
    coluna4 = []
    coluna5 = []
    coluna6 = []
    coluna7 = []
    coluna8 = []
    coluna9 = []
    for i in grille:
        coluna1.append(i[0])
    for i in grille:
        coluna2.append(i[1])
    for i in grille:
        coluna3.append(i[2])
    for i in grille:
        coluna4.append(i[3])
    for i in grille:
        coluna5.append(i[4])
    for i in grille:
        coluna6.append(i[5])
    for i in grille:
        coluna7.append(i[6])
    for i in grille:
        coluna8.append(i[7])
    for i in grille:
        coluna9.append(i[8])
    matriz = [coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7, coluna8, coluna9]
    return check_rows(matriz)

def check_regions(grille): #Function to verify each region (3x3 square)
    region1 = [grille[0][0], grille[0][1], grille[0][2], grille[1][0], grille[1][1], grille[1][2], grille[2][0], grille[2][1], grille[2][2]]
    region2 = [grille[0][3], grille[0][4], grille[0][5], grille[1][3], grille[1][4], grille[1][5], grille[2][3], grille[2][4], grille[2][5]]
    region3 = [grille[0][6], grille[0][7], grille[0][8], grille[1][6], grille[1][7], grille[1][8], grille[2][6], grille[2][7], grille[2][8]]
    region4 = [grille[3][0], grille[3][1], grille[3][2], grille[4][0], grille[4][1], grille[4][2], grille[5][0], grille[5][1], grille[5][2]]
    region5 = [grille[3][3], grille[3][4], grille[3][5], grille[4][3], grille[4][4], grille[4][5], grille[5][3], grille[5][4], grille[5][5]]
    region6 = [grille[3][6], grille[3][7], grille[3][8], grille[4][6], grille[4][7], grille[4][8], grille[5][6], grille[5][7], grille[5][8]]
    region7 = [grille[6][0], grille[6][1], grille[6][2], grille[7][0], grille[7][1], grille[7][2], grille[8][0], grille[8][1], grille[8][2]]
    region8 = [grille[6][3], grille[6][4], grille[6][5], grille[7][3], grille[7][4], grille[7][5], grille[8][3], grille[8][4], grille[8][5]]
    region9 = [grille[6][6], grille[6][7], grille[6][8], grille[7][6], grille[7][7], grille[7][8], grille[8][6], grille[8][7], grille[8][8]]
    if 1 not in region1 or 2 not in region1 or 3 not in region1 or 4 not in region1 or 5 not in region1 or 6 not in region1 or 7 not in region1 or 8 not in region1 or 9 not in region1:
            return False
    if 1 in region1 and 2 in region1 and 3 in region1 and 4 in region1 and 5 in region1 and 6 in region1 and 7 in region1 and 8 in region1 and 9 in region1:
            for j in region1:
                contador = region1.count(j)
                if contador != 1:
                    return False
    if 1 not in region2 or 2 not in region2 or 3 not in region2 or 4 not in region2 or 5 not in region2 or 6 not in region2 or 7 not in region2 or 8 not in region2 or 9 not in region2:
            return False
    if 1 in region2 and 2 in region2 and 3 in region2 and 4 in region2 and 5 in region2 and 6 in region2 and 7 in region2 and 8 in region2 and 9 in region2:
            for j in region2:
                contador = region2.count(j)
                if contador != 1:
                    return False
    if 1 not in region3 or 2 not in region3 or 3 not in region3 or 4 not in region3 or 5 not in region3 or 6 not in region3 or 7 not in region3 or 8 not in region3 or 9 not in region3:
            return False
    if 1 in region3 and 2 in region3 and 3 in region3 and 4 in region3 and 5 in region3 and 6 in region3 and 7 in region3 and 8 in region3 and 9 in region3:
            for j in region3:
                contador = region3.count(j)
                if contador != 1:
                    return False
    if 1 not in region4 or 2 not in region4 or 3 not in region4 or 4 not in region4 or 5 not in region4 or 6 not in region4 or 7 not in region4 or 8 not in region4 or 9 not in region4:
            return False
    if 1 in region4 and 2 in region4 and 3 in region4 and 4 in region4 and 5 in region4 and 6 in region4 and 7 in region4 and 8 in region4 and 9 in region4:
            for j in region4:
                contador = region4.count(j)
                if contador != 1:
                    return False
    if 1 not in region5 or 2 not in region5 or 3 not in region5 or 4 not in region5 or 5 not in region5 or 6 not in region5 or 7 not in region5 or 8 not in region5 or 9 not in region5:
            return False
    if 1 in region5 and 2 in region5 and 3 in region5 and 4 in region5 and 5 in region5 and 6 in region5 and 7 in region5 and 8 in region5 and 9 in region5:
            for j in region5:
                contador = region5.count(j)
                if contador != 1:
                    return False
    if 1 not in region6 or 2 not in region6 or 3 not in region6 or 4 not in region6 or 5 not in region6 or 6 not in region6 or 7 not in region6 or 8 not in region6 or 9 not in region6:
            return False
    if 1 in region6 and 2 in region6 and 3 in region6 and 4 in region6 and 5 in region6 and 6 in region6 and 7 in region6 and 8 in region6 and 9 in region6:
            for j in region6:
                contador = region6.count(j)
                if contador != 1:
                    return False
    if 1 not in region7 or 2 not in region7 or 3 not in region7 or 4 not in region7 or 5 not in region7 or 6 not in region7 or 7 not in region7 or 8 not in region7 or 9 not in region7:
            return False
    if 1 in region7 and 2 in region7 and 3 in region7 and 4 in region7 and 5 in region7 and 6 in region7 and 7 in region7 and 8 in region7 and 9 in region7:
            for j in region7:
                contador = region7.count(j)
                if contador != 1:
                    return False
    if 1 not in region8 or 2 not in region8 or 3 not in region8 or 4 not in region8 or 5 not in region8 or 6 not in region8 or 7 not in region8 or 8 not in region8 or 9 not in region8:
            return False
    if 1 in region8 and 2 in region8 and 3 in region8 and 4 in region8 and 5 in region8 and 6 in region8 and 7 in region8 and 8 in region8 and 9 in region8:
            for j in region8:
                contador = region8.count(j)
                if contador != 1:
                    return False
    if 1 not in region9 or 2 not in region9 or 3 not in region9 or 4 not in region9 or 5 not in region9 or 6 not in region9 or 7 not in region9 or 8 not in region9 or 9 not in region9:
            return False
    if 1 in region9 and 2 in region9 and 3 in region9 and 4 in region9 and 5 in region9 and 6 in region9 and 7 in region9 and 8 in region9 and 9 in region9:
            for j in region9:
                contador = region9.count(j)
                if contador != 1:
                    return False
    return True

def check_sudoku(grille): #Function to verify if the complete solution for the puzzle is correct
    if check_regions(grille) == True and check_cols(grille) == True and check_rows(grille) == True:
        return True
    return False

grille = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 7, 8, 9, 1, 2, 3, 4],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]]

print(check_sudoku(grille))