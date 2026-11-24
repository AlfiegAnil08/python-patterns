stars=1
space=2
for i in range(3):
    for j in range(space):
        print(" ",end=" ")
    for z in range(stars):
        print("*",end=" ")
    print()
    stars=stars+1
    space=space-1
space=0
stars=4
for i in range(4):
    for j in range(space):
        print(" ",end=" ")
    for z in range(stars):
        print("*",end=" ")
    print()
    stars=stars-1
    space=space+1

        

