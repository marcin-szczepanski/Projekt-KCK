### koduje Marcin
import linecache
import clear

### na samym dole uwagi do części Wojtka i Kingi!!!

### funkcje do implementacji przez Łukasza i Kingę (Marcin przygotowuje i przekazuje argumenty w postaci listy):

def zamowF(list): ### argumentem będzie lista obiektów postaci [liczebnik (int), string z nazwą dania], np. list=[[2, "zupa pomidorowa"],[1, "sałatka jarzynowa]]; uwaga na nazwę funkcji: zamowF !
	print ("funkcja zamów")
	
def zaplac(): ### płatność (tylko) gotówką (Kinga z rozmowy i analizy ile rzeczy zamówiono i za ile wnioskuje jaka jest kwota zamówienia)
	print ("funkcja zapłać")
	
def zabierz(list): ### argumentem będzie słowo, co zabrać (lista w pliku words.txt)
	if list[0][0] == "zabranie":
		list[0][0] = list[1][0]
	x = list[0][0]
	### po prostu wpiszcie te 3 linijki powyżej na początku funkcji w swoich częściach, żeby działało; ten x traktujcie jako argument funkcji zamiast samego list :)
	print ("funkcja zabierz")
	
def przyniesF(list): ### argumentem będzie słowo, co zabrać (lista w pliku words.txt); uwaga na nazwę funkcji: przyniesF !
	if list[0][0] == "przyniesienie":
		list[0][0] = list[1][0]
	x = list[0][0]
	### po prostu wpiszcie te 3 linijki powyżej na początku funkcji w swoich częściach, żeby działało; ten x traktujcie jako argument funkcji zamiast samego list :)
	print ("funkcja przynieś")

def polec(): ### brak argumentów; chodzi o polecenie czegoś losowo z menu
	print ("funkcja poleć")

def odejdz(): ### brak argumentów; chodzi o to, żeby kelner odszedł od stołu
	print ("funkcja odejdź")
	
def error(): ### gdy nie zrozumiemy o co chodzi klientowi :)
	print("Nie zrozumiałem.")

###############################	

def clbadwds(list):
	args = []
	while (list):
		if list[0][1] != 'NUMCRD':
			args.append(list.pop(0))
		else:
			list.pop(0)
	return (args)

def zamow(list): ### funkcja przekształca listę do postaci argumentów postaci [liczebnik, string z nazwą dania]
	meals = []
	count = len(list)//3
	meals = [[[None] for col in range(2)] for row in range(count)]
	for i in range(count):
		number = list.pop(0)
		meals[i][0] = int(number[0])
		noun = list.pop(0)
		adj = list.pop(0)
		meals[i][1] = noun[0] + " " + adj[0]
	zamowF(meals)
	return

def prosic(list, file="words.txt"):
	f = open(file, mode="r+")
	j = 0
	k = 0
	action = ''
	word = ''
	count = len(f.readlines())+1
	c = len(list)
	while (j != c):
		for i in range(count):
			wiersz = linecache.getline(file, i).split(";")
			word = list[j][0]
			if word in wiersz:
				action = wiersz[-1].replace("\n","")
				k = 1
				break
		j = j + 1
		if k != 0:
			break
	f.close();
	if action == '':
		zamow(list)
	else:
		value = whataction(action)
		how_many_args = value[1]
		word = value[0]
		possibles = globals().copy()
		possibles.update(locals())
		method = possibles.get(word)
		listargs = clbadwds(list)
		args = []
		while (listargs):
			args.append(listargs[0])
			listargs.pop(0)
		if how_many_args != '0':
			method(args)
		else:
			method()
	return

def createobjectslist(wordlist = '', listofpartsofspeech = ''):
	w = wordlist.split(" ")
	l = listofpartsofspeech.split(" ")
	count = len(w)
	tab = [[[None] for col in range(2)] for row in range(count)]
	for i in range(count):
		tab[i][0] = w[i]
		tab[i][1] = l[i]
	return(tab)

def whataction(word, file = "synonymous_words.txt" ):
    f = open(file, mode="r+")
    count = len(f.readlines())+1
    k = 0
    for i in range(count):
	    wiersz = linecache.getline(file, i).split(";")
	    if word in wiersz:
		    action=wiersz[-2]
		    how_many_args=wiersz[-1]
		    how_many_args = how_many_args.replace("\n","")
		    k = 1
		    break;
    f.close()
    if k == 0:
	    action = "error"
	    how_many_args = '0'
    return(action, how_many_args)


def understanding(s):
	x=clear.wordtoinfinitive(s)
	wordlist = x[0]
	listofpartsofspeech = x[1]
	list = createobjectslist(wordlist, listofpartsofspeech)
	count = len(list)
	action = "error"
	for i in range(count):
		if list[i][1] == 'V':
			action_list = list.pop(i)
			action = action_list[0]
			break;
	value = whataction(action)
	word = value[0]
	how_many_args = value[1]
	possibles = globals().copy()
	possibles.update(locals())
	method = possibles.get(word)
	args = []
	while (list):
		args.append(list[0])
		list.pop(0)
	if how_many_args != '0':
		method(args)
	else:
		method()
	return

understanding("zamówić jajecznica tradycyjna omlet owsiany rosół tradycyjny zupa pomidorowa zupa jarzynowa zupa grzybowa żurek staropolski barszcz ukraiński gulasz węgierski leczo klasyczne tatar wołowy bigos po staropolsku sałatka jarzynowa kotlet schabowy naleśniki serowe pierogi ruskie golonka staropolska placki ziemniaczane frytki belgijskie kasza gryczana ziemniaki polskie ryż biały kawa parzona herbata tradycyjna herbata zielona sok jabłkowy woda mineralna sernik na zimno jabłecznik biszkoptowy")

### test
##print (understanding("poprosić 2 Zupa pomidorowa 1 Sałatka jarzynowa","V NUMCRD N Adj NUMCRD N Adj"))


### Wojtek - zrób, proszę takie coś, żeby przed rzeczownikiem jeśli stoi liczebnik np. "dwa" to żeby zamieniało go na postać liczbową; jeśli przed rzeczownikiem nie ma liczebnika to postaw na sztywno 1 i w stringu z częściami moży w odpowiednim miejscu NUMCRD

### Kinga - przerób, proszę plik menu.txt tak, aby nie zawierał dużych liter (żebym zamiast "Zupa" mógł 2 linijki wyżej napisać "zupa", bo taką postać dostanę od Wojtka;
### menu.txt powinno zawierać tylko dania, które składają się z jednego rzeczownika i jednego przymiotnika, żeby działało :D
