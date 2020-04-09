palabra = input('Ingrese palabra a procesar: ').lower()
letras = []

for i in palabra:
    if len(letras) > 0:
        j = 0
        while j < len(letras) and i != letras[j][0]:
            j += 1
        if j == len(letras):
            letras.append([i, 1])
        else:
            letras[j][1] += 1
    else:
        letras.append([i, 1])

for i in letras:
    print('La letra', i[0], 'aparece:', i[1], 'veces.')

letrasPrimas = ''

for i in letras:
    j = 2
    while j < i[1] and i[1] % j != 0:
        j += 1
    if j == i[1]:
        letrasPrimas = letrasPrimas + i[0]

print('Por lo tanto las letras', '"', letrasPrimas, '"', 'aparecen un numero primo de veces.')
