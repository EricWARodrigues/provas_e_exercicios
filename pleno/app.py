import requests
from poo import Funcionarios
# url = 'https://viacep.com.br/ws/01001000/json/'
# consulta = requests.get(url)
# print(consulta.json())

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    consulta = requests.get(url)
    resposta = dict(consulta.json())
    print(resposta)
    return resposta

def menu():
    try:
        opcao = int(input("Digite a opção desejada:\n1) Cadastrar novo Funcionário\n2) Consultar funcionário\n3) Sair: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            consultar()
        elif opcao == 3:
            return sair()
        else:
            print('Opção inválida, tente novamente')
            return 'Continuar'
    except:
        print('Opção inválida, tente novamente')
        return 'Continuar'

def cadastrar():
    nome = input('Informe o nome completo do funcionário: ')
    while True:
        data_nascimento = input('Informe a data de nascimento do funcionário: ')
        try:
            if not len(data_nascimento) == 10 and not data_nascimento[2] == "/" and not data_nascimento[5] == "/":
                print("Data de nascimento inválida. Tente novamente")
                continue
            dia = int(data_nascimento[:2])
            mes = int(data_nascimento[3:5])
            ano = int(data_nascimento[6:])
            if dia > 0 and dia < 32 and mes > 0 and mes < 13 and ano < 2010 and ano > 1924:
                break
            else:
                print("Data de nascimento inválida. Tente novamente")
        except:
            print("Data de nascimento inválida. Tente novamente")
    setor = ''
    while True:
        try:
            selecao_setor = int(input('Selecione o setor do funcionário\n1) Operação\n2) Fiscal: '))
            if selecao_setor == 1:
                setor = "Operação"
                break
            elif selecao_setor == 2:
                setor == "Fiscal"
                break
            else:
                print('Setor inválido, tente novamente.')
        except:
            print('Entrada inválida. Tente novamente.')
    while True:
        try:
            salario = float(input('Informe o salário do colaborador: '))
            if salario > 0:
                break
            else:
                print('Salário inválido, tente novamente.')
        except:
            print('Salário inválido, tente novamente.')
    while True:
        cep = perguntar_cep()
        endereco_completo = consulta_cep(cep)
        print('Encontrei o seguinte endereço:')
        print(f"Logradouro: {endereco_completo['logradouro']}")
        print(f"Bairro: {endereco_completo['bairro']}")
        print(f"Cidade: {endereco_completo['localidade']}")
        print(f"Estado: {endereco_completo['uf']}")
        try:
            verificacao = int(input('Está correto?\n1) Sim\n2)Não: '))
            if verificacao == 1:
                break
            else:
                print('Opção inválida. Tente novamente.')
        except:
            print('Opção inválida. Tente novamente.')

def perguntar_cep():
    while True:
        try:
            cep = int(input('Informe o CEP do colaborador: '))
            if len(str(cep)) == 8:
                return str(cep)
            else:
                print('CEP inválido, tente novamente.')
        except:
            print('CEP inválido, tente novamente.')

def consultar():
    pass

def sair():
    return 'Sair'

while True:
    execucao = menu()
    if execucao == 'Sair':
        break