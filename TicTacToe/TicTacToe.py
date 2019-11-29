number = 1
count = 5
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def initialarray():
    for i in range(0, 3):
        print("|---|---|---|")
        print(f"| {mylist[i][0]} | {mylist[i][1]} | {mylist[i][2]} |", end='')
        print("")
    print("|---"*3, end='')
    print("|")


def updatedarray():
    for i in range(0, 3):
        print("|---|---|---|")
        print(f"| {mylist[i][0]} | {mylist[i][1]} | {mylist[i][2]} |", end='')
        print("")
    print("|---"*3, end='')
    print("|")


def player1():
    number = int(
        input('Player one, what is your next choice? (type a number) :'))
    if (number == 1):
        mylist[0][0] = 'X'
    elif (number == 2):
        mylist[0][1] = 'X'
    elif (number == 3):
        mylist[0][2] = 'X'
    elif (number == 4):
        mylist[1][0] = 'X'
    elif (number == 5):
        mylist[1][1] = 'X'
    elif (number == 6):
        mylist[1][2] = 'X'
    elif (number == 7):
        mylist[2][0] = 'X'
    elif (number == 8):
        mylist[2][1] = 'X'
    elif (number == 9):
        mylist[2][2] = 'X'


def player2():
    number = int(
        input('Player two, what is your next choice? (type a number) :'))
    if (number == 1):
        mylist[0][0] = 'O'
    elif (number == 2):
        mylist[0][1] = 'O'
    elif (number == 3):
        mylist[0][2] = 'O'
    elif (number == 4):
        mylist[1][0] = 'O'
    elif (number == 5):
        mylist[1][1] = 'O'
    elif (number == 6):
        mylist[1][2] = 'O'
    elif (number == 7):
        mylist[2][0] = 'O'
    elif (number == 8):
        mylist[2][1] = 'O'
    elif (number == 9):
        mylist[2][2] = 'O'


def winnerdetection():
    i = 0
    j = 0
    if (mylist[i][j] == mylist[i][j+1]) and (mylist[i][j] == (mylist[i][j+2])):
        return 1
    if (mylist[i][j] == mylist[i+1][j]) and (mylist[i][j] == (mylist[i+2][j])):
        return 1
    if (mylist[0][0] == mylist[1][1]) and (mylist[0][0] == (mylist[2][2])):
        return 1
    if (mylist[2][0] == mylist[1][1]) and (mylist[2][0] == (mylist[0][2])):
        return 1


def winendgame():
    print("Bravo vous avez gagne :-)")


def endgame():
    print("Vous avez joue toute les cases et il n'y a aucun gangnant :-(")


initialarray()

while(count > 0):
    player1()
    updatedarray()
    if (winnerdetection() == 1):
        winendgame()
        break

    count -= 1
    if (count == 0):
        endgame()
        break

    player2()
    updatedarray()
    if (winnerdetection() == 1):
        winendgame()
        break

    print(count)
