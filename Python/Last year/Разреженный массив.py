class Queue:
    def __init__(self, *list1):
        self.main_list = list1

    def append(self, other):
        self.main_list += other
    
    def copy(self):
        return self.main_list[:]
    
    def pop(self):
        temp = self.main_list[0][:]
        del self.main_list[0]
        if not self.main_list:
            return None
        return temp

    def extend(self, other_queue):
        self.main_list.append(other_queue)

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)