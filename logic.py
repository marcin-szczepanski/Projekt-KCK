import linecache

### funkcje do implementacji:

def zamow():
	print ("zamów")
	
def zaplac():
	print ("zapłać")
	
def zabierz():
	print ("zabierz")
	
def polec():
	print ("poleć")
	
def podejdz():
	print ("podejdź")
	
def odejdz():
	print ("odejdź")

### funkcje napisane (do konsultacji w grupie):
	
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

print (createobjectslist("kotlet schabowy frytka kapusta pekińska poprosić","N Adj N N Adj V"))

def whataction(word = '', file = "synonymous_words.txt" ):
    f = open(file, mode="r+")
    count = len(f.readlines())+1
    action = ''
    for i in range(count):
	    wiersz = linecache.getline(file, i).split(";")
	    if word in wiersz:
		    action=wiersz[-1]
		    break;
    f.close()
    if action == '':
	    action = "error"
    return(action.replace("\n",""))

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
	if actionmethod == actions[0]:
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
	return(action)

### test

print (understanding("kotlet schabowy frytka kapusta pekińska poprosić","N Adj N N Adj V"))
