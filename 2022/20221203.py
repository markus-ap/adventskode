from _verktøy import les_fil

def få_prioritet(ting):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    alfabet += alfabet.upper()
    return alfabet.index(ting) + 1

def ryggsekk(rad):
    midtpunkt = int(len(rad)/2)
    lomme1 = rad[:midtpunkt]
    lomme2 = rad[midtpunkt:]

    felles = [ting for ting in lomme1 if ting in lomme2][0]
    return få_prioritet(felles)

def ryggsekk_grupper(ryggsekk_gruppe):
    rs1, rs2, rs3 = ryggsekk_gruppe
    felles = [ting for ting in rs1 if ting in rs2 and ting in rs3][0]
    return få_prioritet(felles)

def les_alle_ryggsekkar(data):
    prioritet = 0
    noverande_gruppe = []
    for rad in data.split("\n"):
        noverande_gruppe.append(rad)
        if(len(noverande_gruppe) == 3):
            prioritet += ryggsekk_grupper(noverande_gruppe)
            noverande_gruppe = []

    return prioritet


def hovud():
    data = les_fil("20221203.txt")
    prioritet = les_alle_ryggsekkar(data)
    print(prioritet)

if __name__ == "__main__":
    hovud()