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
def mayor(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max    
 
def menor(lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
    return min
lista=["AA55", "1010", "BEBE", "0101", "0FEA"]
lista_bin=[]
lista_dec=[]
for e in lista:
    conversion=hexadecimal_a_binario(e)
    lista_bin.append(conversion)
print(lista_bin)

for j in lista_bin:
    convert=binario_a_decimal(j)
    lista_dec.append(convert)

print(lista_dec)

menor_lista=menor(lista_dec)
mayor_lista=mayor(lista_dec)

print("El menor es",menor_lista)
print("El mayor es",mayor_lista)
