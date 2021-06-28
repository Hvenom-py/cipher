import random

slowo = "szyfr"

def szyfrowanie(slowo):
    nowe = ""
    for x in slowo:
        rnd = (random.randint(1,366))%25
        if ord(x)+rnd > 122:
            x=ord(x)+rnd-25
            nowe+=chr(x)   
        else:
            x=ord(x)+rnd
            nowe+=chr(x)   
    return nowe


print(szyfrowanie(slowo))
