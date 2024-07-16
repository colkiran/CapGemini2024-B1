
num = int(input("Enter a number :"))
inv = 0

try:
    inv = 1 / num

except ZeroDivisionError as z:
    print("Exception Occured......")
    print(z)
except TypeError as t:
    print("Exception Occured......")
    print(t)

except Exception as e:
    print("Exception Occured Exception class ......")
    print(e)

else:
    print(f"Inverse of {num} is :{inv}")
finally:
    print("Completed dividing the number......")