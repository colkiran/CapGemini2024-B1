
for i in range(1, 11):
    print(i, end=" ")

print()     # prints a new line

print("-" * 60)

for i in range(1, 31):
    # if i > 25:
    #     break           # exit from the loop
    if i % 2 == 1:
        continue        # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted generating even numbers.....")



