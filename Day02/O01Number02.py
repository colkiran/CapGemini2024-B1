
print("Number System".center(60, "-"))
print(11)       # decimal
print(0b11)     # Binary    =>  1 * 2 ** 1  + 1 * 2 ** 0 = 2 + 1 = 3
print(0b101)    # Binary    => 5
print(0o11)     # octal     =>  1 * 8 ** 1 + 1 * 8 ** 0 = 8 + 1 = 9
print(0o111)    # octal     => 1 * 8 ** 2 + 1 * 8 ** 1 + 1 * 8 ** 0
                        #   =>   64 + 8 + 1 =  73

print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(f"Binary 100 :{bin(a)}")
print(f"Octal 100  :{oct(a)}")
print(f"Hexa 100   :{hex(a)}")

"""
hexa
----
0x64 => 6 * 16 ** 1 + 4 * 16 ** 0
     => 96 + 4 => 100

Octal - 0o144
-------------    
144 => 1 * 64 + 4 * 8 + 4
    => 64 + 32 + 4
    => 100
"""
