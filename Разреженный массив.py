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

