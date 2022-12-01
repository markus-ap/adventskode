from _verktøy import les_fil
    
def tell_kaloriar_per_alv(data):
    ob = {}
    alvenummer = 0
    for line in data.split("\n"):
        if line == "":
            alvenummer += 1
            continue
        ob.setdefault(alvenummer, 0)
        ob[alvenummer] += int(line)
    
    return sorted(ob.items(), key= lambda alv: alv[1], reverse=True)

def topp_tri_total(data):
    return sum(alv[1] for alv in data[:3])

def hovud():
    data = les_fil("data/20221201.txt")
    alvedata = tell_kaloriar_per_alv(data)
    print(alvedata)
    print(topp_tri_total(alvedata))

if __name__ == "__main__":
    hovud()