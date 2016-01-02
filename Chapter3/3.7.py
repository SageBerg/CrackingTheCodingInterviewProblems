import imp
import time
moduled = imp.load_source('', '../Chapter2/linked_list.py')
LinkedList = moduled.LinkedList

class Animal(object):
    
    def __init__(self, kind, name):
        self.kind = kind 
        self.name = name

class AnimalShelter(object):

    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
    
    def enqueue(self, animal):
        if animal.kind == "cat":
            self.cats.prepend((animal, time.time()))
        elif animal.kind == "dog":
            self.dogs.prepend((animal, time.time()))

    def dequeue(self, lst):
         prev = None
         node = lst.head
         if node == None:
             return None
         while not node is lst.tail:
              prev = node
              node = node.nxt
         lst.tail = prev
         if node is lst.head:
             lst.head = None
         return node.data[0]

    def dequeue_any(self):
        if self.cats.tail.data[1] <= self.dogs.tail.data[1]:
            return self.dequeue(self.cats)
        else:
            return self.dequeue(self.cats)
       
    def dequeue_cat(self):
        return self.dequeue(self.cats)

    def dequeue_dog(self):
        return self.dequeue(self.dogs)


def main():
    shelter = AnimalShelter()
    shelter.enqueue(Animal("cat", "Mr. Fuzzball"))
    shelter.enqueue(Animal("dog", "Good Boy"))
    shelter.enqueue(Animal("cat", "Mr. Fluffball"))
    shelter.enqueue(Animal("dog", "Rex"))
    shelter.enqueue(Animal("dog", "Fido"))
        
    print shelter.dequeue_dog().name 
    print shelter.dequeue_any().name 
    print shelter.dequeue_dog().name 
    print shelter.dequeue_cat().name 

main()
