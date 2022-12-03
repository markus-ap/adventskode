def lokalsti(filnamn):
    import os
    return os.path.join(os.path.dirname(__file__), f"data\{filnamn}")

def les_fil(filnamn):
    return open(lokalsti(filnamn)).read()

def lag_filar():
    for dato in range(5, 25):
        filnamn = f"202212{dato:02d}.txt"
        filsti = lokalsti(filnamn)
        open(filsti, "x", encoding="utf8")

def hovud():
    print("No har du klart å køyre fila med verktøysmetodar.")
    lag_filar()

if __name__ == "__main__":
    hovud()