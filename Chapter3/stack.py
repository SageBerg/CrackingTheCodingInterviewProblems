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
        try:
            value = self.lst[-1]
            if value == self.mins[-1]:
                self.mins = self.mins[0:-1]
            self.lst = self.lst[0:-1]
            return value 
        except:
            traceback.print_exc()

    def get_min(self):
        return self.mins[-1]
