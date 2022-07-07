import math
def hexadecimal_a_binario(hexadecimal):
    a=int(hexadecimal,16)
    bstr=""
    while a>0:
        bstr = str(a % 2) + bstr 
        a = a >> 1
    binario=bstr

    return binario
