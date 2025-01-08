class DefaultList(list):
    def __init__(self, std_value=None):
        super().__init__()
        self.std_value = std_value

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.std_value

s = DefaultList(51)
s.extend([1, 5, 7])

indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")