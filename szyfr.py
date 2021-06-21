massage = input("Enter massage to code\n")


def code(massage):
    nowe=""
    for x in massage:
        x = chr(ord(x)+3)
        nowe+=x
        
    return nowe 


print(code(massage))


