stars=1
space=3
for i in range(4):
    for j in range(space):
        print(" ",end=" ")
    for z in range(stars):
        print("*",end=" ")
    print()
    stars=stars+2
    space=space-1
stars=5
space=1
for i in range(4):
    for j in range(space):
        print(" ",end=" ")
    for z in range(stars) :
        print("*",end=" ")
    print()
    space=space+1
    stars=stars-2

    