
for i in range(1, 6):
    for k in range(6-i, 0, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
for i in range(5, 0, -1):
    for k in range(7-i, 0, -1):
        print(" ", end="")
    for j in range(1, i):
        print(j, end=" ")
    print()
