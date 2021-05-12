"""An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure."""


from datetime import datetime


class Animal:
    def __init__(self, value):
        self.timestamp = datetime.now()
        self.value = value


class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        
    def enqueueDog(self, value):
        self.dogs.append(Animal(value))
        
    def enqueueCat(self, value):
        self.cats.append(Animal(value))
        
    def dequeueDog(self):
        return self.dogs.pop(0)
        
    def dequeueCat(self):
        return self.cats.pop(0)
        
    def dequeueAny(self):
        if self.cats[0].timestamp > self.dogs[0].timestamp:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)