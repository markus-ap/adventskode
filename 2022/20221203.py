from _verktøy import les_fil

def hovud():
    print("Det er tredje desember!")
    data = les_fil("20221203.txt")

if __name__ == "__main__":
    hovud()