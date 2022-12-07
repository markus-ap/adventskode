from _verktøy import les_fil

def total_storleik(data):
    total = 0
    data = data.split("\n")
    for rad in data:
        rad = rad.split(" ")
        if rad[0].isdigit(): total += int(rad[0])
    return total

def alle_stiar(data):
    data = data.split("\n")
    ob = dict()
    noverande_sti = ""
    for rad in data:
        rad = rad.split(" ")
        if rad[0] == "$" and rad[1] == "cd":
            if rad[2] == "..":
                indeks = noverande_sti.rindex("/")
                noverande_sti = noverande_sti[:indeks]
                if len(noverande_sti) == 0:
                    noverande_sti = "/"
            elif len(noverande_sti) != 0 and len(noverande_sti) != 1:
                noverande_sti += f"/{rad[2]}"
            else:
                noverande_sti += rad[2]
            ob.setdefault(noverande_sti, 0)

        if rad[0].isdigit():
            ob[noverande_sti] += int(rad[0])
    return ob

def filter_mappar(ob: dict):
    summering = 0
    for mappe in ob.keys():
        total = 0
        for mappe2 in ob.keys():
            if mappe2.startswith(mappe):
                total += ob[mappe2]
        if total < 100000:
            summering += total
    return summering

def filtrer_mappar2(ob: dict, mål):
    svar = []
    for mappe, storleik in ob.items():
        total = 0
        for m2, s2 in ob.items():
            if m2.startswith(mappe):
                total += ob[m2]
        if total >= mål:
            svar.append(total)
    return sorted(svar, reverse=True)

def hovud():
    data = les_fil("20221207.txt")
    ob = alle_stiar(data)
    total = 70000000 - total_storleik(data)
    treng = 30000000 - total
    print(total, treng)

    ob = filtrer_mappar2(ob, treng)
    print(ob)


    #ob = mappe_struktur(data)
    #print(filter_mappar(ob))

if __name__ == "__main__":
    hovud()