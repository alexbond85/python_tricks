

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __repr__(self):
        return f"<Person: {self.name}, {self.age}"

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.name == other.name and self.age == other.age
        return NotImplemented

    def __hash__(self):
        return hash((self.name, self.age))


p1 = Person("A", 75)
p2 = Person("A", 75)

print(hash(p1))
print(hash(p2))
