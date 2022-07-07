from random import randint
precio_manzana=3.5 #Precio por cada manzana de caramelo
caramelos_manzana=0.5 #Precio por cada caramelo de manzana vacío
unidades_manzanas=randint(10,20)#Cantidad de manzanas de caramelos vendidas
unidades_caramelos=randint(1,200)#cantidad de caramelos vendidos
if (unidades_manzanas%20)==0:
  total_manzanas=(unidades_manzanas*precio_manzana)-(0.7*(unidades_manzanas//20))
else:
    total_manzanas=unidades_manzanas*precio_manzana

