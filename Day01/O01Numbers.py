
"""
int
float
complex
"""

a = 10
b = -10
print(f"a :{a}")          # f - fstring used for interpolation
print(type(a))            # RTTI - runtime type identification

print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 1.0
d = -1.0
print(f"c :{c}")
print(type(c))

print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3        # 2 * e ** 3 = 2 * 1000 = 2000.0
f = -2e3

print(f"e :{e}")
print(type(e))

print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.14j
h = -13.14j

print(f"g :{g}")
print(type(g))

print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(32, 43, 18, 35, 40))
print(min(32, 43, 18, 35, 40))

x = 3 + 2.5
print(type(x))

x = 3
y = 2.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print('z =', type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))