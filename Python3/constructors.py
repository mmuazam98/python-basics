class Animal:
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound

def printAnimal(o):
    if not isinstance(o, Animal):
        raise TypeError('printAnimal(): requires an animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}"')

def main():
    printAnimal(Animal('Kitten','Fluffy','Meow'))
    printAnimal(Animal('Duck','Donald','Quack'))

main()