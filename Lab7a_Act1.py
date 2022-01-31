# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jake Alepa
#               Gregory Clarke
#               James Cullis
#               Elliot Petcosky
# Section:      535
# Assignment:   Lab7a Activity 1
# Date:         10 06 2021
Game = True
O = chr(9675)  # prints white circle
OO = chr(9679)  # prints colored in circle

row1 = [O, ".", O, ".", O, ".", O, "."]
row2 = [".", O, ".", O, ".", O, ".", O]
row3 = [O, ".", O, ".", O, ".", O, "."]
row4 = [".", ".", ".", ".", ".", ".", ".", "."]
row5 = [".", ".", ".", ".", ".", ".", ".", "."]
row6 = [".", OO, ".", OO, ".", OO, ".", OO]
row7 = [OO, ".", OO, ".", OO, ".", OO, "."]
row8 = [".", OO, ".", OO, ".", OO, ".", OO]

Board = [row1, row2, row3, row4, row5, row6, row7, row8]

while Game:  # this loop will play the game until the user enters 9

    for row in Board:  # prints out each row of Board one list at a time
        print(*row)

    row = int(input("In what row is the piece you want to "
                    "move? 1 - 8 (Top to Bottom) (Enter 9 to stop): "))
    if row == 9:  # if the user enters 9, the game will stop
        print("Thanks for playing!")
        exit()

    if row > 9 or row <= 0:  # checks if the space exists
        print("\nPlease enter a valid row!\n")
    col = int(input("In what column is the piece you "
                    "want to move? 1 - 8 (Left to Right): "))  # user enters the column of the
                                                               # piece they want to move
    if col > 8 or col <= 0:  # checks if the space exists
        print("\nPlease enter a valid column!\n")

    error = 0  # determines if there is actually a piece to move
    if row % 2 != 0:
        if col % 2 == 0:
            error = 1

    elif row % 2 == 0:
        if col % 2 != 0:
            error = 1

    if error == 0:
        move_row = int(input("What row do you want to move the"
                             " piece to? row 1 - 8 (Top to Bottom): "))  # user enters the row of
                                                                         # where the piece will move
        if move_row > 8 or move_row <= 0:  # checks if the space exists
            print("\nPlease enter a valid row!\n")

        move_col = int(input("What column do you want to move the piece"
                             " to? 1 - 8 (Left to Right): "))  # user enters the column of
                                                               # where the piece will move
        if move_col > 8 or move_col <= 0:  # checks if the space exists
            print("\nPlease enter a valid column!\n")

        if move_row % 2 == 0:  # checks to for correct piece placement in even columns
            if move_col % 2 != 0:
                error = 2

        elif move_row % 2 != 0:  # checks for correct piece placement in odd columns
            if move_col % 2 == 0:
                error = 2

        if error == 0:  # this part will determine where to move the piece to
            char = Board[row - 1][col - 1]  # 1 is subtracted from the inputted
            Board[row - 1][col - 1] = "."   # value because lists start with 0
            Board[move_row - 1][move_col - 1] = char

        elif error == 2:  # this message will print if the user moves their square to an illegal space
            print("\nPlease enter a valid square!\n")

    elif error == 1:  # prints this message if the user entered an invalid piece
        print("\nPlease select a valid piece!\n")


