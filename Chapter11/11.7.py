class Performer(object):
    
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __repr__(self):
        return "(" + str(self.height) + ", " + str(self.weight) + ")"

def sort_performers(performers):
    pass #hint it's a longest increasing subsequence problem

def main():
     performers = [Performer(65, 100), Performer(70, 150), Performer(56, 90), Performer(75, 190),
                   Performer(60, 95), Performer(69, 151), Performer(68, 110)] 
     print sort_performers(performers)
 
main()
        


