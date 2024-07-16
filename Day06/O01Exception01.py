
# sys module
import sys

n = int(input("Enter the Numerator :"))
d = input("Enter the denominator :")
print(f"Numerator   :{n}")
print(f"Denominator :{d}")

try:
    res = n / d
    print(f"result :{res}")
except:
    print("Exception occured.....")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info())


