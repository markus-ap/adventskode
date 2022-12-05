from _verktøy import les_fil

def finn_buntar(data):
    rå = data.split("\n")[:9]
    tal = [int(siffer) for siffer in rå[-1].split(" ") if siffer != ""]

    buntar = {
        1: ["D", "H", "R", "Z", "S", "P", "W", "Q"],
        2: ["F", "H", "Q", "W", "R", "B", "V"],
        3: ["H", "S", "V", "C"],
        4: ["G", "F", "H"],
        5: ["Z", "B", "J", "G", "P"],
        6: ["L", "F", "W", "H", "J", "T", "Q"],
        7: ["N", "J", "V", "L", "D", "W", "T", "Z"],
        8: ["F", "H", "G", "J", "C", "Z", "T", "D"],
        9: ["H", "B", "M", "V", "P", "W"]
    }
    return buntar

def cm9000_flytt_kasse(frå, til, buntar):
    flytt = buntar[frå][0]
    buntar[frå] = buntar[frå][1:]

    ny_til = [flytt]
    ny_til.extend(buntar[til])
    buntar[til] = ny_til
    return buntar

def cm9001_flytt_kasse(antall, frå, til, buntar):
    flytt = buntar[frå][:antall]
    buntar[frå] = buntar[frå][antall:]

    ny_til = flytt
    ny_til.extend(buntar[til])
    buntar[til] = ny_til
    return buntar

def cm9000_prosesser_kommando(kommando, buntar):
    komm, antall, frå, frå_bunte, til, til_bunte = kommando.split(" ")
    for i in range(int(antall)):
        buntar = cm9000_flytt_kasse(int(frå_bunte), int(til_bunte), buntar)

    return buntar

def cm9001_prosesser_kommando(kommando, buntar):
    komm, antall, frå, frå_bunte, til, til_bunte = kommando.split(" ")
    return cm9001_flytt_kasse(int(antall), int(frå_bunte), int(til_bunte), buntar)
    
def topp_bunte(buntar):
    resultat = ""
    for bunte, liste in buntar.items():
        resultat += liste[0]
    return resultat

def flytt_kassar(data):
    buntar = finn_buntar(data)
    for rad in data.split("\n")[10:]:
        cm9001_prosesser_kommando(rad, buntar)
    return topp_bunte(buntar)

def hovud():
    data = les_fil("20221205.txt")
    resultat = flytt_kassar(data)
    print(resultat)

if __name__ == "__main__":
    hovud()