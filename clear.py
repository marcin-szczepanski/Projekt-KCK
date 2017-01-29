#koduje wojciech
import sys
import re
import string


def clearbadwords(str = "", file = "badwords.txt"): # pierwszy argument przyjmuje zdanie, drugi plik tekstowy z wyrazami do usunięcia
    f = open(file, mode ="r+")
    try:
        s = f.read()
        s = s.lower()
        str = str.lower()
        listbad = s.split()
        # .,?![]{}();:-_
        str = str.replace("!", " ").replace(".", " ").replace(",", " ").replace("?", " ")
        str = str.replace("[", " ").replace("]", " ").replace("(", " ").replace(")", " ").replace("{", " ").replace("}", " ")
        str = str.replace(";", " ").replace(":", " ").replace("-", " ").replace("_", " ").replace("+", " ").replace("`", " ")
        str = str.replace("@", " ").replace("#", " ").replace("$", " ").replace("%", " ").replace("^", " ").replace("&", " ")
        str = str.replace("*", " ").replace("<", " ").replace(">", " ").replace("/", " ").replace("|", " ")


        liststr = str.split()
        for bs in listbad:
            for gs in liststr:
                if gs == bs:
                    liststr.remove(bs)

        retstring = ' '.join(liststr)
        return(retstring)

    finally:
        f.close()
    print ('Blad')
def szukajdania(x): #funkcja do znajdywania w pliku menu.txt odpowiedniego posiłku, o który prosi klient
    lista = []
    isItFound = False
    lines = 0
    with open('Menu.txt', 'r', encoding='utf-8') as searchfile:
        for line in searchfile:
            lines = lines + 1
            if x in line:
                line = line[0:line.find(';')]
                lista.append(line.rstrip('\n'))
                break
        a = len(lista)
        if a>0:
            return line
        else:
            return False

def wordtoinfinitive(s = '', file = "dicdomyslny.dic" ):
    f = open(file, mode="r+")
    f_brak = open("brakislownikowe.txt", mode="a")
    s = clearbadwords(s)
    wordlist = s.split() ## s - podzielone wyrazy stringa zdaniowego - teraz lista
    diclist = f.read().split() ##lista słownika
    resultword = []
    resultcm = []
    poprzednia = ''
    lastword = ''
    for word in wordlist:
        czyznaleziono = 0
        ##tutaj w petli tworzyl bym wyrazenie regularne z kazdego wyrazu
        # pattern = re.compile(word + '(.*)[;](.*)[/]')
        pattern = re.compile(word + '[;].*[/]')
        for tword in diclist:
            wynik = re.match(pattern, tword)
            if wynik != None:
                czyznaleziono = 1
                temporary = wynik.group()
                cm = re.compile('[,].*[/]')
                czescmowy = re.search(cm, temporary).group().strip(',').strip('/')
                ##print(czescmowy)
                ##w tej zmiennej zapisuje jaka to jest część mowy narazie nie używana ale możemy ją zwrócić gdy zajdzie potrzeba
                hti = re.compile('[;].*[,]')
                how_to_inf = re.search(hti, temporary).group().strip(',').strip(';')
                dl = int(how_to_inf[0])
                word = word[0:(len(word)-dl)] + (how_to_inf[1:])
                if (poprzednia == "N" and czescmowy !='ADJ'):
                    if (szukajdania(lastword)!=False):
                        resultword.append(szukajdania(lastword).split()[1])
                        resultcm.append('ADJ')
                if (czescmowy == "N" and poprzednia != "NUMCRD"):
                    resultcm.append('NUMCRD')
                    resultword.append('1')
                lastword = word
                poprzednia = czescmowy
                ##print(type(czescmowy))
                resultword.append(word)
                resultcm.append(czescmowy)
                break;

        if(czyznaleziono == 0):
            f_brak.write(word + "\n")
            #print("Brakuje słowa w słowniku: " + word )

    if (czescmowy == "N" and (szukajdania(lastword) != False)):
        resultword.append(szukajdania(word).split()[1])
        resultcm.append('ADJ')

    res_str = ' '.join(resultword)
    res_cm = ' '.join(resultcm)
    f.close()
    return(res_str,res_cm)

###test
##jajecznica tradycyjna omlet owsiany rosół tradycyjny zupa pomidorowa zupa jarzynowa zupa grzybowa żurek staropolski barszcz ukraiński gulasz węgierski leczo klasyczne tatar wołowy bigos po staropolsku sałatka jarzynowa kotlet schabowy naleśniki serowe pierogi ruskie golonka staropolska placki ziemniaczane frytki belgijskie kasza gryczana ziemniaki polskie ryż biały kawa parzona herbata tradycyjna herbata zielona sok jabłkowy woda mineralna sernik na zimno jabłecznik biszkoptowy

#.,?![]{}();:-_
##print (wordtoinfinitive("poproszę omlet i żurek staropolski i kotlet"))

#print(szukajdania('menu'))
