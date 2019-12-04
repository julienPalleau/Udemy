number = 1
count = 5
cpt = 0
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
    cpt = 0
    for x in range(0, 3):
        for y in range(0, 2):
            if (mylist[x][y] == mylist[x][y+1]):
                cpt += 1

            if (cpt == 2):
                return 1

    for y in range(0, 3):
        for x in range(0, 2):
            if (mylist[x][y] == mylist[x+1][y]):
                cpt += 1

            if (cpt == 2):
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
