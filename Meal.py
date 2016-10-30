class Meal(object):

    def __init__(self, name=None):
        self._name = name
        self.listOfIngredients = []

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
            return True
        else:
            return False

    def printIngredients(self):
        for x in self.listOfIngredients:
            print(x)

ListOfDishes = []
Jajecznica = Meal("Jajecznica")
Jajecznica.addIngredients(["Jajko", "Masło", "Cebula"])
ListOfDishes.append(Jajecznica)

Omlet = Meal("Jajecznica")
Omlet.addIngredients(["Jajko", "Masło", "Mleko"])
ListOfDishes.append(Omlet)

Rosol = Meal("Rosol")
Rosol.addIngredients(["Drób", "Włoszczyzna", "Wołowina"])
ListOfDishes.append(Rosol)

Tatar = Meal("Tatar")
Tatar.addIngredients(["Wołowina", "Jajko", "Olej", "Cebula", "Ogórek"])
ListOfDishes.append(Tatar)

Carpaccio = Meal("Carpaccio wołowe z rukolą i parmezanem")
Carpaccio.addIngredients(["Wołowina", "Rukola", "Parmezan"])
ListOfDishes.append(Carpaccio)

Barszcz = Meal("Barszcz czerwony z kołdunami")
Barszcz.addIngredients(["Bulion", "Burak", "Grzyby", "Kołduny"])
ListOfDishes.append(Barszcz)

Pierogi1 = Meal("Pierogi ze szpinakiem, suszonymi pomidorami i fetą")
Pierogi1.addIngredients(["Szpinak", "Pomidor", "Feta"])
ListOfDishes.append(Pierogi1)

Pierogi2 = Meal("Pierogi z cielęciną i borowikami z masłem szałwiowym")
Pierogi2.addIngredients(["Cielęcina", "Borowik", "Masło", "Szałwia"])
ListOfDishes.append(Pierogi2)

Zurek = Meal("Żurek z białą kiełbasą i jajkiem")
Zurek.addIngredients(["Bulion", "Zakwas", "Kiełbasa", "Jajko"])
ListOfDishes.append(Zurek)

Krem1 = Meal("Krem z dyni z mlekiem kokosowym")
Zurek.addIngredients(["Bulion", "Dynia", "Mleko kokosowe", "Śmietana"])
ListOfDishes.append(Krem1)

Krem2 = Meal("Krem z trufli z grzankami")
Krem2.addIngredients(["Bulion", "Trufle", "Śmietana", "Grzanki"])
ListOfDishes.append(Krem2)

Krem3 = Meal("Krem z pomidorów")
Krem3.addIngredients(["Bulion", "Pomidor", "Śmietana"])
ListOfDishes.append(Krem3)

Zupa = Meal("Zupa pomidorowa")
Zupa.addIngredients(["Bulion", "Pomidor", "Śmietana"])
ListOfDishes.append(Zupa)
