
from collections import namedtuple

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y

    nmdTpl = namedtuple("Arith", "s d p q")
    calc = nmdTpl(s = sum, d = diff, p = prod, q = quot)
    return calc

arith = arithCalc(30, 12)
# print(arith)
print(f"Sum  = {arith.s}")
print(f"Diff = {arith.d}")
print(f"Prod = {arith.p}")
print(f"Quot = {arith.q}")


