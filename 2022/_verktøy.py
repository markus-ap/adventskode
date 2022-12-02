def les_fil(filnamn):
    import os
    filnamn = os.path.join(os.path.dirname(__file__), f"data/{filnamn}")
    return open(filnamn).read()

def hovud():
    print("No har du klart å køyre fila med verktøysmetodar.")

if __name__ == "__main__":
    hovud()