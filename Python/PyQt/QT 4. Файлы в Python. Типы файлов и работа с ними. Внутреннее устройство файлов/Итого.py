try:
    with open("prices.txt", 'r', encoding='utf-8') as f:
        strings = f.readlines()
        if strings:
            result = 0.00
            for line in strings:
                _, num, price = line.rstrip().rsplit('\t', 2)
                result += float(num) * float(price)
            print(f'{result:.2f}')
        else:
            ...

except Exception:
    print(0)
