nombre= 'paulina'
print(nombre[0])
nombres =['paulina','moises','hector','balamm',"raul",'joselyn']
print(nombres)

nombres[0]='max'
print(nombres)

nombres.sort()
print(nombres)

nombres.append('paulina')
nombres.reverse()
print(nombres)

#tuplas
tupla=(1,2,3,4,5,3,5)

print(tupla)
print(tupla.count(3))
print(tupla.index(3))
#tupla[0]=23

#set
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

s.remove(3)

print(s)

s.add(2)
s.add(2)
s.add(2)

print(s)

#diccionarios
edades={'pailina':21,'moises':22,'hector':23,'balamm':24,'raul':25,'joselyn':26}

colores={'rojo':255}

print(edades['joselyn'])

edades['raul']=20
print(edades)

edades['balamm']+=1
print(edades)

#matrices
m=[[1,2,3],[4,5,6]]
print(m)

#for
for i in [1,2,3,4]:
    print(i)
for i in range(5):
    print(i)
for i in range(2,4):
    print(i)

for i in range(0,21,5):
    print(i)

nombres=['paulina','moises','hector','balam','raul','joselyn']

for nombre in nombres:
     print(nombre)
for caracter in nombre:
    print(caracter)

cordenadaX=10
cordenadaY= 5.3
cordenadas=(cordenadaX,cordenadaY)
print(cordenadas)
cordenadas[0]=34
print(cordenadas)