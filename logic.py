### koduje Marcin
import linecache

### funkcje do implementacji przez Łukasza i Kingę (Marcin przygotowuje i przekazuje argumenty w postaci listy):

def zamow(): ### argumentem będzie lista obiektów postaci [liczebnik, string z nazwą dania]
	print ("funkcja zamów")
	
def zaplac(): ### płatność gotówką (Kinga z rozmowy i analizy ile rzeczy zamówiono i za ile wnioskuje jaka jest kwota zamówienia)
	print ("funkcja zapłać")
	
def zabierz(): ### argumentem będzie słowo, co zabrać: menu/karta (dań)/talerze/
	print ("funkcja zabierz")
	
def polec(): ### brak argumentów; chodzi o polecenie czegoś losowo z menu
	print ("funkcja poleć")
	
def podejdz(): ### brak argumentów; chodzi o to, żeby kelner podszedł do stołu
	print ("funkcja podejdź")
	
def odejdz(): ### brak argumentów; chodzi o to, żeby kelner odszedł od stołu
	print ("funkcja odejdź")

def prosic(): ### implementuje Marcin
	print ("funkcja prosić")

### def dzielAkcje(): ### implementuje Marcin (jeśli jest więcej niż jedna akcja w zdaniu)
###	print ("dziel akcje")

def createobjectslist(wordlist = '', listofpartsofspeech = ''):
	w = wordlist.split(" ")
	l = listofpartsofspeech.split(" ")
	count = len(w)
	tab = [[[None] for col in range(2)] for row in range(count)]
	for i in range(count):
		tab[i][0] = w[i]
		tab[i][1] = l[i]
	return(tab)
	
### test

print (createobjectslist("poprosić kotlet schabowy frytka kapusta pekińska","V N ADJ N N ADJ"))

def whataction(word = '', file = "synonymous_words.txt" ):
    f = open(file, mode="r+")
    count = len(f.readlines())+1
    action = ''
    for i in range(count):
	    wiersz = linecache.getline(file, i).split(";")
	    if word in wiersz:
		    action=wiersz[-1]
		    action = action.replace("\n","")
		    break;
    f.close()
    if action == '':
	    action = "error"
    return(action)

### test

print (whataction("poprosić"))

def listofactions(file = "synonymous_words.txt"):
    f = open(file, mode="r+")
    count = len(f.readlines())+1
    list = []
    numbersloop = range(1, count)
    for i in numbersloop:
	    wiersz = linecache.getline(file, i).split(";")
	    list.append(wiersz[-1].replace("\n",""))
    f.close()
    return(list)

### test

print (listofactions())
	
### poniższa funkcja jest niedokończona; do dyskusji w grupie

def understanding(wordlist = '', listofpartsofspeech = ''):
	list = createobjectslist(wordlist, listofpartsofspeech)
	count = len(list)
	for i in range(count):
		if list[i][1] == "V":
			action = list[i][0]
			break;
	actionmethod = whataction(action)
	actions = listofactions()
	if actionmethod == actions[0]: ### zamiast if-ów plik z akcjami i dopełnieniami i szukanie w pliku o jaką akcję chodzi
		zamow()
	if actionmethod == actions[1]:
		zaplac()
	if actionmethod == actions[2]:
		zabierz()
	if actionmethod == actions[3]:
		polec()
	if actionmethod == actions[4]:
		podaj()
	if actionmethod == actions[5]:
		odejdz()
	if actionmethod == actions[6]:
		prosic()
	return(action)

### test

print (understanding("poprosić kotlet schabowy frytka kapusta pekińska","V N Adj N N Adj"))
