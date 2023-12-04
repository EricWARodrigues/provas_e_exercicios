numero = int(input('Digite um número para verificar a tabuada: '))

for mult in range(1, 11):
    print(f'{numero} x {mult} = {numero * mult}')