tictactae=[["|","0","|","1","|","2","|"],
           ["|","3","|","4","|","5","|"],
           ["|","6","|","7","|","8","|"]]
def display():
    for i in tictactae:
        print(*i)
def checkX():
    winx=False
    for i in tictactae:
        if(' '.join(i)=="| X | X | X |"):
            print("X wins")
            winx=True
            break
    for j in range(1,7):
        if(j%2!=0):
            if(tictactae[0][j]=="X" and tictactae[1][j]=="X" and tictactae[2][j]=="X") :
                print("X wins")
                winx=True
                break

    if(tictactae[0][1]=="X" and tictactae[1][3]=="X" and tictactae[2][5]=="X"):
        print("X wins")
        winx=True
    elif(tictactae[0][5]=="X" and tictactae[1][3]=="X" and tictactae[2][1]=="X"):
        print("X wins")
        winx=True
    return winx

def checkO():
    wino=False
    for i in tictactae:
        if(' '.join(i)=="|O|O|O|"):
            print("O wins")
            wino=True
            break
    for j in range(1,7):
        if(j%2!=0):
            if(tictactae[0][j]=="O" and tictactae[1][j]=="O" and tictactae[2][j]=="O") :
                print("O wins")
                wino=True
                break

    if(tictactae[0][1]=="O" and tictactae[1][3]=="O" and tictactae[2][5]=="O"):
        print("O wins")
        wino=True
    elif(tictactae[0][5]=="O" and tictactae[1][3]=="O" and tictactae[2][1]=="O"):
        print("O wins")
        wino=True
    return wino

def xturn():
    print("X's Turn :")
    x=input()
    for i in range(0,3):
        for j in range(0,7):
            if(tictactae[i][j]==x):
                tictactae[i][j]="X"
    for i in tictactae:
        print(*i)
def oturn():
    print("O's Turn :")
    x=input()
    for i in range(0,3):
        for j in range(0,7):
            if(tictactae[i][j]==x):
                tictactae[i][j]="O"
    for i in tictactae:
        print(*i)
if __name__ == "__main__":
    display()
    for p in range(0,10):
        if(p==9):
            print("nobody wins")
            break
        elif(p%2==0):
            xturn()
            y=checkX()
            if(y==True):
                break
        else:
            oturn()
            z=checkO()
            if(z==True):
                break
        





