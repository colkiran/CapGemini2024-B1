
print("Arithmetic Operators".center(60, "-"))
print(f"Sum  10 + 3 = {10 + 3}")
print(f"Diff 10 - 3 = {10 - 3}")
print(f"Prod 10 * 3 = {10 * 3}")
print(f"Quot 10 / 3 = {10 / 3}")
print(f"Flr  10 // 3 = {10 // 3}")      # floor division
print(f"Mod  10 % 3 = {10 % 3}")
print(f"Pow  10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")
x += 5

print(f"x :{x}")
x /= 3

print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, >, <, >=, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"1 < 2  :{1 < 2}")

print(f"1 > 2  :{1 > 2}")
print(f"1 == 2 :{1 == 2}")
print(f"1 != 2 :{1 != 2}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(f"1 == 1 and 1 == 1 :{1 == 1 and 1 == 1}")
print(f"1 == 1 and 1 == 2 :{1 == 1 and 1 == 2}")

print("-" * 60)
print(f"1 == 1 or 1 == 2 :{1 == 1 or 1 == 2}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 or 1 == 2) :{not(1 == 1 or 1 == 2)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of                                                 unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print(f"chr(65) :{chr(65)}")
print(f"chr(97) :{chr(97)}")
print("orange" > "apple")
print("apple" > "orange")

print("Bitwise Operators".center(60, "-"))

print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60, "-"))
age = 19
print("Eligible" if age > 18 else "Not Eligible")
