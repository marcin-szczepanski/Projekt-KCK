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

def wordtoinfinitive(s = '', file = "dictionary.dic" ):
    f = open(file, mode="r+")
    wordlist = s.split() ## s - podzielone wyrazy stringa zdaniowego - teraz lista
    diclist = f.read().split() ##lista słownika
    result = []
    for word in wordlist:
        ##tutaj w petli tworzyl bym wyrazenie regularne z kazdego wyrazu
        # pattern = re.compile(word + '(.*)[;](.*)[/]')
        pattern = re.compile(word + '[;].*[/]')
        for tword in diclist:
            wynik = re.match(pattern, tword)
            if wynik != None:
                temporary = wynik.group()
                #cm = re.compile('[,].*[/]')
                #czescmowy = re.search(cm, temporary).group().strip(',').strip('/')
                ##w tej zmiennej zapisuje jaka to jest część mowy narazie nie używana ale możemy ją zwrócić gdy zajdzie potrzeba
                hti = re.compile('[;].*[,]')
                how_to_inf = re.search(hti, temporary).group().strip(',').strip(';')
                dl = int(how_to_inf[0])
                word = word[0:(len(word)-dl)] + (how_to_inf[1:])
                result.append(word)
                break;
    res_str = ' '.join(result)
    f.close()
    return(res_str)

###test

print (wordtoinfinitive(clearbadwords("Poproszę o schabowego z frytkami i kapusta pekińską")))
