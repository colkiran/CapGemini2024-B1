
i = 1
while (i <= 10):
    print(i, end = " ")
    i += 1      # i = i + 1 or i++
print()
print(f"after :{i}")

i -= 1
print("-" * 60)

while(True):
    print(i, end = " ")
    i -= 1
    if i == 0:
        break