space=3
for i in range(4):
    for j in range(space):
        print(" ",end="")
    for z in range(i+1):
        print("*",end="")
    print()
    space=space-1