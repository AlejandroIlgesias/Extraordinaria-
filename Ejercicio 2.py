a=1#Valor de prueba
def calcular(dollar_amount):
  dollar_value_euros=20514#precio en usd por bitcoin
  euros_value_usd=0.98#un dolar vale 0.98 euros
  euros_value=(dollar_amount*dollar_value_euros)*euros_value_usd #Euros que tengo en bitcoin.
  return euros_value

b=calcular(a)

def valor_futuro(capital, tipo, periodo,o):#apartado 3,valor futuro
  res=0
  for t in range(periodo):
        if o==1:
            res = res+capital*(1+tipo)**(t+1)
            print("Valor futuro cada año",res)
        else:
            res = res+capital*(1+tipo)**(t)
            print("Valor futuro cada año",res)
  print("El valor futuro es:", round(res,2))
  
  def valor_actual(capital,tipo,periodo,o):#apartado 4 valor final
    res=0
    for t in range(periodo):
        if o==1:
            res=res+capital/(1+tipo)**(t)
            print("Valor actual cada año",res)
        else:
            res=res+capital/(1+tipo)**(t+1)
            print("Valor actual cada año",res)
