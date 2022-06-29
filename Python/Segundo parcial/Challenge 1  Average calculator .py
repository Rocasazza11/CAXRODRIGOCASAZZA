a=int(input('Cuanto sacaste en el primer parcial?'))
b=int(input('cuanto sacaste en el segundo parcial?'))
c=int(input('cuanto sacaste en el tercer parcial?'))

x=(a+b+c)
p=(x/3)
print('tu promedio general es: ',p)

if(p>=6):
  print('aprobaste')
  
if(p==10):
  print('ala eres magnifico')
if(p<6):
  print('reprobado JAJAJAJA')
    