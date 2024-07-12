
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

iter = int(input("Enter the series of numbers to be generated :"))

for i in range(iter):
    print(fib(i), end=" ")
print()

print("-"  * 60)

