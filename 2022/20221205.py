from _verktøy import les_fil

def hovud():
    data = les_fil("20221205.txt")
    print("Det er femte desember!")

if __name__ == "__main__":
    hovud()