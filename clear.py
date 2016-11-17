#koduje wojciech

def clearbadwords(str = "", fa = "badwords.txt"):
    f = open(fa, mode ="r+")
    s = f.read()
    s = s.lower()
    str = str.lower()
    listbad = s.split()
    liststr = str.split()
    liststr = list(set(liststr))

    for bs in listbad:
        for gs in liststr:
            if gs == bs:
                liststr.remove(bs)

    liststr.sort()
    retstring = ' '.join(liststr)

    return(retstring)

    f.close()

def infintivewords(str = ' ',file = "#slownik" )

    for

###test

print(clearbadwords("Prosze Alu alaa ala ale alae o  konkretna konkretna konkretna marke piwka o z o o o da prosze o prosze konKRETNA piwka "))