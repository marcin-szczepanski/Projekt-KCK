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

print (createobjectslist("ala ma czarnego kota","N V Adj N"))

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

