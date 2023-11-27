velocidade = float(input('Digite a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 20
    print(f'Você deverá pagar R${multa:.2f} de multa por excesso de velocidade')
else:
    print('Sem registro de excesso de velocidade.')