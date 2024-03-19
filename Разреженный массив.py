class Polynomial:
    def __init__(self, list1):
        if len(list1) == 2:
            list1.insert(0, 0)
        self.free, self.x1, self.x2 = list1

    def poly(self):
        ...

poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))