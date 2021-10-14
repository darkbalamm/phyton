x =input('x: ')
y= input('y: ')
#print(f'{x} / {y}= {x/y}')
try:
    x=int(input('x: '))
    y=int(input('y: '))
except ValueError:
    print('error de valor')
    sys.exit(1)
try:
    resultado=x/y
except ZeroDivisionError:
    print('es indefinido al divideir entre cero')
    sys.exit(1)

print(f'{x} /{y} = {resultado}')