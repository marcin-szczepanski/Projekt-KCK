import linecache

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
    return(action)

### test

print (whataction("poprosić"))

### poniższa funkcja jest niedokończona; do dyskusji w grupie
def understanding(wordlist = '', listofpartsofspeech = ''):
	list = createobjectslist(wordlist, listofpartsofspeech)
	count = len(list)
	for i in range(count):
		if list[i][1] == "V":
			action = list[i][0]
			break;
	return(action)
	
### test

print (understanding("kotlet schabowy frytka kapusta pekińska poprosić","N Adj N N Adj V"))
