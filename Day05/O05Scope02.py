
glbX = 100

def fun(x):         # local variables
    global glbX      # do not assign any value to the variable in                        this line
    print(f"x :{x}")
    glbX = 250
    print(f"inside :{glbX}")



print(f"before :{glbX}")

fun(150)

print(f"after :{glbX}")

