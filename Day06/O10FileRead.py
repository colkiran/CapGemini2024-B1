
FL = open("data.txt", "r")       # r = read mode
# st = FL.read()                 # reads the entire content of the file
# st = FL.read(1000)               # reads the no of bytes specified
# print(st)

# st = FL.readline()              # reads a single line
# st = FL.readline(500)             # bytes mentioned should be less than                                      the size of line
# print(st)

# reads all the lines and stores it in a list
# st = FL.readlines()
# for line in st:
#     print(line)

# which ever the byte falls in, it will print the data from BOF till the prargraph where the byte is present
st = FL.readlines(865)
print(st)

FL.close()