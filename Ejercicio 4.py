import math
def hexadecimal_a_binario(hexadecimal):
    a=int(hexadecimal,16)
    bstr=""
    while a>0:
        bstr = str(a % 2) + bstr 
        a = a >> 1
    binario=bstr

    return binario
def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal
