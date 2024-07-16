
FL = open("Myfile1.txt", "w+")

while(True):
    st = input("Enter the contents of the file :")
    FL.write(st + "\n")
    ch = input("Do you wish to continue :")
    if ch == 'n':
        break

# moves the file pointer from one place to another
FL.seek(0, 0)
st = FL.read()
print(st)

FL.close()