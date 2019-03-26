novotxt = ''
with open('TheZenOfPython.txt', 'r') as ler:
    for i, l in enumerate(ler.read()):
            if l in 'aeiou':
                novotxt += '*'
            else:
                novotxt += l

print(novotxt, end='')
with open('TheZenOfPythonCrypt.txt', 'w') as crypt:
    crypt.write(novotxt)

