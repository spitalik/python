rows = 5

for row_number in range(1, rows + 1):
    for col_number in range(1, row_number + 1):
        print(col_number," ",end="")
    print(" ")

for row_number in range(rows, 1, -1):
    for col_number in range(1, row_number):
        print(col_number," ",end="")
    print(" ")

row = rows;
while row > 0:
    row -= 1
    col = rows;
    while col > row:
        print(rows - col + 1 ," ",end="")
        col -= 1
    print(" ");     

row = rows;
while row > 1:
    row -= 1
    col = row + 1
    while col > 1:
        col-=1
        print(row-col+1, " ", end = "");
    print("");    