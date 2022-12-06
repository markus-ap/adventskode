from _verktøy import les_fil

def finn_start(data, avvik: int):
    for i in range(len(data)):
        datapunktar = list(data[i:i+avvik])
        datasett = set(datapunktar)
        if len(datasett) is len(datapunktar): 
            print(i, datasett, datapunktar)
            return i+avvik

def hovud():
    data = les_fil("20221206.txt")
    start = finn_start(data, 14)
    print(start)

if __name__ == "__main__":
    hovud()