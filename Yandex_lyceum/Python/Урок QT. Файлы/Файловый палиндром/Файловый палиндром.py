def palindrome():
    try:
        with open('input.dat', 'rb') as file:
            data = file.read()
        return data == data[::-1]
    
    except FileNotFoundError:
        ...