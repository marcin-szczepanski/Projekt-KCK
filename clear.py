#koduje wojciech

import re

def clearbadwords(str = "", file = "badwords.txt"): # pierwszy argument przyjmuje zdanie, drugi plik tekstowy z wyrazami do usunięcia
    f = open(file, mode ="r+")
    try:
        s = f.read()
        s = s.lower()
        str = str.lower()
        listbad = s.split()
        liststr = str.split()
        ##liststr = list(set(liststr)) ### psuje kolejność wyrazów w zdaniu

        for bs in listbad:
            for gs in liststr:
                if gs == bs:
                    liststr.remove(bs)

        ##liststr.sort() sort listy
        retstring = ' '.join(liststr)

        return(retstring)

    finally:
        f.close()
    print ('Blad')

def wordtoinfinitive(s = '', file = "dicdomyslny.dic" ):
    f = open(file, mode="r+")
    f_brak = open("brakislownikowe.txt", mode="a")
    s = clearbadwords(s)
    wordlist = s.split() ## s - podzielone wyrazy stringa zdaniowego - teraz lista
    diclist = f.read().split() ##lista słownika
    resultword = []
    resultcm = []
    poprzednia = ''
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
                if (czescmowy =="N" and poprzednia!="NUMCRD"):
                    resultcm.append('NUMCRD')
                    resultword.append('1')
                poprzednia = czescmowy
                ##print(type(word))
                ##print(type(czescmowy))
                resultword.append(word)
                resultcm.append(czescmowy)
                break;
        if(czyznaleziono == 0):
            f_brak.write(word + "\n")
            print("Brakuje słowa w słowniku: " + word )


    res_str = ' '.join(resultword)
    res_cm = ' '.join(resultcm)
    f.close()
    return(res_str,res_cm)

###test
##jajecznica tradycyjna omlet owsiany rosół tradycyjny zupa pomidorowa zupa jarzynowa zupa grzybowa żurek staropolski barszcz ukraiński gulasz węgierski leczo klasyczne tatar wołowy bigos po staropolsku sałatka jarzynowa kotlet schabowy naleśniki serowe pierogi ruskie golonka staropolska placki ziemniaczane frytki belgijskie kasza gryczana ziemniaki polskie ryż biały kawa parzona herbata tradycyjna herbata zielona sok jabłkowy woda mineralna sernik na zimno jabłecznik biszkoptowy


print (wordtoinfinitive("tatar wołowy dwa bigosy po staropolsku trzy sałatki jarzynowe kotlet schabowy naleśniki serowe pierogi ruskie golonka staropolska placki ziemniaczane frytki belgijskie kasza gryczana ziemniaki polskie ryż biały kawa parzona herbata tradycyjna herbata zielona sok jabłkowy woda mineralna sernik na zimno jabłecznik biszkoptowy"))


