def trend(*data, **functions):
    m_res = [x[1] for x in data]
    for f in functions:
        t = list(map(functions[f], [x[0] for x in data]))
        temp = []
        for i in range(len(data)):
            if -1 < float(t[i]) - float(m_res[i]) <= 0.001:
                temp.append(1)
        if len(temp) == len(data):
            return f


data = [(0, 2.0), (-1.0, 3.05), (3.0, -1), (-2.0, 4.0), (18, -16.001)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3,
             "line_1": lambda x: -x + 2}
print(trend(*data, **functions))
data = [(0, 0), (-1.0, 1.001), (3.0, 8.999), (-2.0, 4.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))
data = [(0, 0), (-1.0, -3.01), (3.0, 9.0), (-2.0, -6.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))