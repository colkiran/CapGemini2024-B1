
# read and write mode
FL = open("Myfile.txt", "r+")
# file pointer will be pointing at the begning of the file

# st = FL.read()
# print(st)

FL.write("This is the sixth line \n")

FL.close()