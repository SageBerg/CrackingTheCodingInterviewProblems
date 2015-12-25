import traceback

class Stack(object):

    def __init__(self):
        self.lst = []
        self.mins = [float("inf")]

    def push(self, value):
        if (value <= self.mins[-1]):
            self.mins.append(value)
        self.lst.append(value)

    def pop(self):
        value = self.lst[-1]
        if value == self.mins[-1]:
            self.mins = self.mins[0:-1]
        self.lst = self.lst[0:-1]
        return value 

    def get_min(self):
        return self.mins[-1]

    def peek(self):
        if len(self.lst) == 0:
            return float("inf")
        return self.lst[-1]

    def is_empty(self):
        if self.lst == []:
            return True
        return False
