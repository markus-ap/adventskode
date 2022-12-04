from _verktøy import les_fil


def seksjon_til_sett(seksjon):
    start, slutt = seksjon.split("-")
    rekkevidde = range(int(start), int(slutt)+1)
    return set(rekkevidde)

def samenlikn_sett(s1 : set, s2: set):
    likt = s1.intersection(s2)
    return len(likt) is len(s1) or len(likt) is len(s2)

def delvis_like_sett(s1: set, s2: set):
    likt = s1.intersection(s2)
    return len(likt) > 0

def spisopp(data):
    poeng = 0
    for rad in data.split("\n"):
        alv1, alv2 = rad.split(",")
        alv1 = seksjon_til_sett(alv1)
        alv2 = seksjon_til_sett(alv2)
        likt = samenlikn_sett(alv2, alv1)    
        if likt: poeng += 1
    return poeng
        
def delvis_spistopp(data):
    poeng = 0
    for rad in data.split("\n"):
        alv1, alv2 = rad.split(",")
        alv1 = seksjon_til_sett(alv1)
        alv2 = seksjon_til_sett(alv2)
        likt = delvis_like_sett(alv1, alv2)
        if likt: poeng += 1
    return poeng


def hovud():
    data = les_fil("20221204.txt")
    poeng = delvis_spistopp(data)
    print(poeng)

if __name__ == "__main__":
    hovud()