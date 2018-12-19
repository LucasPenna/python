'''
Estrutura Sequencial

1.
print('Alo Mundo')

2.
numero = input('Informe um número:')
print('O número informado foi', numero)

3.
numero1 = float(input('Informe um número:'))
numero2 = float(input('Informe outro número:'))
resultado = numero1+numero2

print('A soma dos números informados é', resultado)

4.
result = []
for a in range(0,4):
    print(a+1, 'Bimestre')
    number = float(input("Informe a nota:"))
    result.append(number)
soma_das_notas = sum(result)
media_das_notas = soma_das_notas/4

print('A média das notas foi:',media_das_notas)

5.
print('Conversor universal de m para cm\n')
mt = float(input('Informe a medida em m:'))
cm = mt * 100

print('O valor compativel em cm é:',cm)

6.
import math

print('Calculo de area de Círculo\n')
r = float(input('Informe o raio do circulo:'))
a = math.pi*r**2

print('O valor da area é:',a)

7.
r = float(input('Informe o lado do quadrado:'))
a = r**2
da = 2*a

print('O valor do dobro da area é:',da)

.
.
.

18.
arq = float(input('Informe o tamanho de um arquivo em MB:'))
link = float(input('Informe a velocidade da sua internet em Mbps:'))
ts = arq/link
tm = round(ts/60,2)

print('O download levará:',tm, 'minutos.')
'''
'''
Estrutura De Decisao

1.
numero1 = float(input('Informe um número:'))
numero2 = float(input('Informe outro número:'))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

print('O maior é:', maior)

2.
numero1 = float(input('Informe um número:'))
if numero1 > 0:
    num = 'positivo'
elif numero1 == 0:
    num = '0'
else:
   num = 'negativo'

print('O número é', num)

3.

'''

result = []
for a in range(0,10):
    print(a+1, 'Nota')
    number = float(input("Informe :"))
    result.append(number)

print('O maior resultado é:', max(result))














