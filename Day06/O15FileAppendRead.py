
FL = open("Myfile1.txt", "a+")

st = input("Enter the contents of the file :")
FL.write(st + "\n")

FL.seek(0, 0)
st = FL.read()
print(st)

FL.close()