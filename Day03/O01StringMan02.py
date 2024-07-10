
print("find".center(60, "-"))
st = "hello world"
print(f"st :{st}")

pos = st.find("w")
print(f"position 'w' :{pos}")

pos = st.find("l")
print(f"position 'l' :{pos}")

# pos = st.find("l", 3)
pos = st.find("l", st.find("l") + 1)
print(f"position 'l' :{pos}")

pos = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"position 'l' :{pos}")

print("replace".center(60, "-"))
st = "hello world"
print(f"st :{st}")

res = st.replace("h", "H")
print(f"res :{res}")
# print(f"st :{st}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print(f"index".center(60, "-"))
st = "hello world"
print(f"st :{st}")

idx = st.index("w")
print(f"index :{idx}")

# index function will throw an error message if the character is not found
# idx = st.index("b")
# print(f"index :{idx}")

idx = st.index("l")
print(f"index 'l' :{idx}")

idx = st.index("l", st.index("l") + 1)
print(f"index 'l' :{idx}")

print("maketrans".center(60, "-"))
st = 'hello world'
print(f"st :{st}")

a = 'helowrd'       # find
b = 'HELOWRD'       # replace

# length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"result table :{resTbl}")

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"result :{res}")

print("count".center(60,"-"))
st = 'hello world'

print(f"count 'h' :{st.count('h')}")
print(f"count 'l' :{st.count('l')}")

st = 'the quick brown fox jumps over the lazy dog'
print(f"st :{st}")

print(f"count 'o' :{st.count('o')}")
print(f"count 'e' :{st.count('e')}")





