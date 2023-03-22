import math
n1 = float(input('Digite o angulo: '))
seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O angulo {} tem o seno de {:.2f} o cos de {:.2f} e a tan de {:.2f}'.format(n1,seno,cos,tan))