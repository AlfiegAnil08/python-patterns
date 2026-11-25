for r in range(4):
    for c in range(7):
        if r==0 or r==3:
            print("*",end=" ")
        elif c==0 or c==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()