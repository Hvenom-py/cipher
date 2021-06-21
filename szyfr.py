import random

massage = input("Enter massage to code\n")


def code(massage):
    nowe=""
    for x in massage:
        rnd=random.randint(0,366)
        x = chr(ord(x)+rnd)
        nowe+=x
        
    return nowe 


print(code(massage))





