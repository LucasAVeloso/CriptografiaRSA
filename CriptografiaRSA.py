import math
import random


msg = "The information security is of significant importance to ensure the privacy of communications"
msgCifrada = []
msgCifradaTemp = []
msgDecifrada = []
msgDecifradaTemp = []
n,d,e,m = None,None,None,None

def sort_prime(num):
    prime_num1 = []
    prime_num2 = [True] * (num + 1)
    for i in range(2, num + 1):
        if prime_num2[i]:
            prime_num1.append(i)
            for j in range(2, int(num / i) + 1):
                prime_num2[i * j] = False
    return prime_num1

def get_random_int(min, max):
    min = math.ceil(min)
    max = math.floor(max)
    return math.floor(random.random() * (max - min + 1)) + min

def mdc(x,y):
    while(y) :
        t=y
        y=x%y
        x=t
    return x

def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

# Aumentar muito esse valor vai deixar a conta muito mas MUITO LENTA
primos = sort_prime(300)

p = primos[get_random_int(len(primos)-60,len(primos))]
q = primos[get_random_int(len(primos)-60,len(primos))]

n = p*q
m = (p-1)*(q-1)

tempE = 0
temp=(get_random_int(1,m))
e=0
while(e==0) :
  tempE = mdc(temp,m)
  if tempE==1 : e = temp
  else : temp=(get_random_int(1,m))

d = modInverse(e,m)

print("p:",p)
print("q:",q)
print("n:",n)
print("m:",m)
print("e:",e)
print("d:",d)


strBytes = bytes(msg, 'utf-8')
# actual bytes in the the string
for byte in strBytes:
    msgCifradaTemp.append(byte)

print('mensagem convertida para bytes: ')
print(msgCifradaTemp)

for index in range(len(msgCifradaTemp)):
  temp = pow(msgCifradaTemp[index],e)
  temp2 = temp % n
  msgCifrada.append(temp2)

print('\n')
print('mensagem criptografada: ')
print(msgCifrada)



for index in range(len(msgCifrada)):
  temp = pow(msgCifrada[index],e)
  temp2 = temp % n
  msgDecifradaTemp.append(pow(msgCifrada[index],d) % n)

  
print('\n')
print('mensagem decriptografada: ')
print(msgDecifradaTemp)

msgDecifrada = bytes(msgDecifradaTemp)

# for i in range(len(msgDecifradaTemp)):
#     msgDecifrada.append(str(msgDecifradaTemp[i],'utf-8'))


print('\n')
print('mensagem traduzida: ')
print(msgDecifrada)