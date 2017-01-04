import re
import linecache

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

###test

print (whataction("poprosić"))
