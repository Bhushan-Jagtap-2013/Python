#!/usr/bin/python3
# --- MODEL ---- 
class Animal:
    def sound(self): return self._doAction('sound')
    def work(self): return self._doAction('work') 
    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'Action : {} : not found in : {}'.format(action, self.AnimalName())
    def AnimalName(self):
        return self.__class__.__name__.lower()

# --- VIEW ---
class Dog(Animal):
    strings = dict(
        sound = "Bhoo Bhoo",
        work = "Guard Home"
    )
class Person(Animal):
    strings = dict(
        sound = "hahaha"
    )

# --- CONTROLLER --
def getAll(obj):
    print(obj.sound())
    print(obj.work())

p = Person()
d = Dog()

for o in (p, d):
    getAll(o)

