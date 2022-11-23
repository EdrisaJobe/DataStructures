#Define people and pass object class
class people(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

#Sets the name of person to Edrisa
person = people("Edrisa", 19, 6.0, 170)
#Prints out the name defined above
print (person.name, person.age, person.height, person.weight)
