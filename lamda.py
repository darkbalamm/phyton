libros=[
    {'titulo':'el principito','año':1934},
    {'titulo':'el arte de la guerra','año':1772},
    {'titulo':'la ciudad de la bestias','año':2002},
    {'titulo':'el hobbit','año':1984},
    {'titulo':'la grieta','año':2007}
]

#libros.short()

def flibros(libros):
    return libros['titulo'].upper()
def fanio(libros):
    return libros['año']

print(libros)
print()

print('libros ordenados por año')
libros.sort(key=fanio)
print(libros)

print('libros por titulo')
libros.sort(key=flibros)
print(libros)

libros.sort(key=lambda libro:libro['año'] )
for libro in libros:
  #  print(f'el libros {libro['titulo']} fue publicado {libro['año']})
#print(libros)

libros.sort(key=lambda x:x['titulo'])
print(libros)
