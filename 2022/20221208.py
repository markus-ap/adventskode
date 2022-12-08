from _verktøy import les_fil

def lag_matrise(data):
    data = data.split("\n")
    radar = []
    kolonnar = []

    for indeks in range(len(data)):
        rad = data[indeks]
        radar.append([int(tal) for tal in rad])
        kolonnar.append([int(rad[indeks]) for rad in data])
    return radar, kolonnar

def finn_synlege_trær(radar, kolonnar):
    synlege_trær = 0
    for x in range(len(radar)):
        for y in range(len(kolonnar)):
            if(er_synlig(x, y, radar, kolonnar)):
                synlege_trær += 1
    return synlege_trær

def høgaste_poengsum(radar, kolonnar):
    høgast_poengsum = 0
    for x in range(len(radar)):
        for y in range(len(kolonnar)):
            poeng = utsikt_poeng(x, y, radar, kolonnar)
            if poeng > høgast_poengsum: 
                høgast_poengsum = poeng
    return høgast_poengsum

def antal_trær_før_blokkert_utsikt(treliste, verdi) -> int:
    antal = 0
    for tre in treliste:
        antal += 1
        if tre >= verdi: break
    return antal

def utsikt_poeng(x, y, radar, kolonnar):
    verdi = radar[x][y]
    rad = radar[x]
    kolonne = kolonnar[y]

    venstre_poeng = antal_trær_før_blokkert_utsikt(reversed(rad[:y]), verdi)
    høgre_poeng = antal_trær_før_blokkert_utsikt(rad[y+1:], verdi)
    
    opp_poeng = antal_trær_før_blokkert_utsikt(reversed(kolonne[:x]), verdi)
    ned_poeng = antal_trær_før_blokkert_utsikt(kolonne[x+1:], verdi)

    return venstre_poeng * høgre_poeng * opp_poeng * ned_poeng

def er_synlig(x, y, radar, kolonnar):
    if x == 0 or x == len(radar)-1: return True
    if y == 0 or y == len(kolonnar)-1: return True

    verdi = radar[x][y]
    if verdi == 0: return False

    rad = radar[x]
    kolonne = kolonnar[y]
    
    maks_vest = max(rad[:y])
    maks_aust = max(rad[y+1:])
    maks_nord = max(kolonne[:x])
    maks_syd = max(kolonne[x+1:])
    
    if maks_vest < verdi: return True
    if maks_aust < verdi: return True
    if maks_nord < verdi: return True
    if maks_syd < verdi: return True

    return False

def hovud():
    data = les_fil("20221208.txt")
    radar, kolonnar = lag_matrise(data)
    poeng = høgaste_poengsum(radar, kolonnar)
    print(poeng)

if __name__ == "__main__":
    hovud()