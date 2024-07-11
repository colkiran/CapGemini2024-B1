
# factorial

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

x = 5
print(f"Factorial of {x} is :{fact(x)}")

"""
5 * fact(4) = 5 * 24 = 120

4 * fact(3) = 4 * 6 = 24

3 * fact(2) = 3 * 2 = 6

2 * fact(1) => 2 * 1 = 2
"""