class Meal(object):

    listOfIngredients = []

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def addIngredients(self, list):
        self.listOfIngredients.extend(list)

    def isIngredient(self, x):
        if x in self.listOfIngredients:
            print("Jest skladnikiem")
        else:
            print("Nie jest skladnikiem")


Jajecznica = Meal("Jajecznica")
Jajecznica.addIngredients(["Jajko", "Maslo", "Cebula", "Sol", "Pieprz"])

Omlet = Meal("Jajecznica")
Omlet.addIngredients(["Jajko", "Maslo", "Mleko", "Sol", "Pieprz"])

Rosol = Meal("Rosol")
Rosol.addIngredients(["Uda", "Korpus", "Skrzydelka", "Serca", "Zoladek", "Wloszczyzna", "Wolowina", "Woda", "Ziele angielskie", "Lisc", "Sol", "Pieprz"])

#wyszukiwanie czy jakis skladnik jst w potrawie:

Rosol.isIngredient("Wolowina")
Rosol.isIngredient("Szynka")
