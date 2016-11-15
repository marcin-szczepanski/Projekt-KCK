list = []
def findMealWithIngredient(x):
    isItFound = False
    with open('Menu.txt', 'r') as searchfile:
        for line in searchfile:
            if x in line:
                line = line[0:line.find(';')]
                list.append(line.rstrip('\n'))
        a = len(list)
        if a>0:
            print("Oto dania z podanym składnikiem:")
            for y in range(0, a):
                print(list[y])
        else:
            print("Nie ma dań z podanym składnikiem :(")

def printMenu():
    with open('Menu.txt', 'r') as searchfile:
        print('** Menu restauracji **')
        i=1
        for line in searchfile:
            line = line.replace(';','. Składniki: ').rstrip('\n')
            print(str(i) + '. ' + line + '.')
            i=i+1

def greeting():
    print('Dzień dobry, witamy w naszej restauracji! W czym mogę pomóc?')

#findMealWithIngredient("Bulion")
#printMenu()
