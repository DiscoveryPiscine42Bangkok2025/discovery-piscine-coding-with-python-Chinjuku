def bishop_algorithm(board_size, bishop_position):
    can_check = []
    bishop_cols = bishop_position[0]
    bishop_rows = bishop_position[1]
    for i in range(1, board_size+1):
        # ล่างขวา
        if bishop_cols+i < board_size+1 and bishop_rows+i < board_size+1: 
            can_check.append([bishop_cols+i, bishop_rows+i])
        # บนซ้าย
        if bishop_cols-i > 0 and bishop_rows-i > 0:
            can_check.append([bishop_cols-i, bishop_rows-i])
        # บนขวา
        if bishop_cols+i < board_size+1 and bishop_rows-i > 0:
            can_check.append([bishop_cols+i, bishop_rows-i])
        # ล่างซ้าย
        if bishop_cols-i > 0 and bishop_rows+i < board_size+1:
            can_check.append([bishop_cols-i, bishop_rows+i])
    return can_check

def pawn_algorithm(board_size, pawn_position):
    can_check = []
    pawn_cols = pawn_position[0]
    pawn_rows = pawn_position[1]
    # ซ้ายบน
    if pawn_cols-1 > 0 and pawn_rows-1 > 0:
        can_check.append([pawn_cols-1, pawn_rows-1])
    # ขวาบน
    if pawn_cols+1 < board_size and pawn_rows-1 > 0:
        can_check.append([pawn_cols+1, pawn_rows-1])
    return can_check

def rook_algorithm(board_size, rook_position):
    can_check = []
    rook_cols = rook_position[0]
    rook_rows = rook_position[1]
    for i in range(1, board_size+1):
        #  (add rows) and cols lock
        if i < board_size+1 and [rook_cols, i] != rook_position:
            can_check.append([rook_cols, i])
        #  (add cols) and rows lock
        if i < board_size+1 and [i, rook_rows] != rook_position:
            can_check.append([i, rook_rows])
    return can_check

def queen_algorithm(board_size, queen_position):
    return bishop_algorithm(board_size, queen_position) + rook_algorithm(board_size, queen_position)

def chess_board(table):
    rows = table.split("\n")
    board_check = True
    size = len(rows)

    for cols in rows:
        if len(cols) != len(rows):
            board_check = False
            break

    return board_check, size

def chess_position(table):
    """
    x = cols, y = rows
    """
    rows = table.split("\n")
    king, bishop, pawn, queen, rook = [], [], [], [], []
    y=1
    for cols in rows:
        x=1
        for char in cols:
            if char == "K":
                king = [x, y]
            if char == "B":
                bishop = [x, y]
            if char == "P":
                pawn = [x, y]
            if char == "Q":
                queen = [x, y]
            if char == "R":
                rook = [x, y]
            x+=1
        y+=1
    return [king, bishop, pawn, queen, rook]

def checkmate(table):
    board_check, size = chess_board(table)
    if board_check == False:
        return print("Error")

    units = chess_position(table)
    check_all = []

    if units[1] != []:
        check_all += bishop_algorithm(size, units[1])
    if units[2] != []:
        check_all += pawn_algorithm(size, units[2])
    if units[3] != []:
        check_all += queen_algorithm(size, units[3])
    if units[4] != []:
        check_all += rook_algorithm(size, units[4])

    # for rows in range(1, size+1):
    #     for cols in range(1, size+1):
    #         if units[0] not in check_all and [cols, rows] == units[0]:
    #             print("K", end="")
    #         elif [cols, rows] == units[1]:
    #             print("B", end="")
    #         elif [cols, rows] == units[2]:
    #             print("P", end="")
    #         elif [cols, rows] == units[3]:
    #             print("Q", end="")
    #         elif [cols, rows] == units[4]:
    #             print("R", end="")
    #         else:
    #             print("x", end="") if [cols, rows] in check_all else print(".", end="")
    #     print("")
    
    if units[0] in check_all and board_check:
        return print("Success")
    else:
        return print("Fail")
    
    