from _verktøy import les_fil

poengtavle = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

vinninger = ["A Y", "B Z", "C X"]
uavgjorter = ["A X", "B Y", "C Z"]


def poeng_for_runde(runde):
    poeng = 0

    if runde in vinninger: poeng += 6
    elif runde in uavgjorter: poeng += 3
    else: poeng += 0

    alv, meg = runde.split(" ")
    poeng += poengtavle[meg]

    return poeng

def les_runder(data):
    totalpoeng = 0
    for runde in data.split("\n"):
        alv, mål = runde.split(" ")

        if alv == "A":
            if mål == "X": runde = "A Z"
            elif mål == "Y": runde = "A X"
            elif mål == "Z": runde = "A Y"
        elif alv == "B":
            if mål == "X": runde = "B X"
            elif mål == "Y": runde = "B Y"
            elif mål == "Z": runde = "B Z"
        elif alv == "C":
            if mål == "X": runde = "C Y"
            elif mål == "Y": runde = "C Z"
            elif mål == "Z": runde = "C X"
        
        totalpoeng += poeng_for_runde(runde)
    return totalpoeng

def hovud():
    data = les_fil("20221202.txt")
    poeng = les_runder(data)
    print(poeng)

if __name__ == "__main__":
    hovud()