def reverse():
    with open("input.dat", "rb") as f:
        temp = f.read()
    with open("output.dat", 'wb') as out:
        out.write(temp[::-1])

reverse()