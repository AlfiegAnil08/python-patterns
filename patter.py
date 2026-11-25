space=4
stars=1
for i in range(5):
    for j in range(space):
        print(" ",end="")
    for z in range(stars):
        print("*",end="")
    print()
    stars=stars+1
    space=space-1

space=1
stars=4
for i in range(4):
    for j in range(space):
        print(" ",end="")
    for z in range(stars):
        print("*",end="")
    print()
    stars=stars-1
    space=space+1