email = 'prova@python.com'
senha = 'infinity*school'

while True:
    email_informado = input('Informe seu e-mail: ')
    senha_informada = input('Digite sua senha: ')
    if email_informado == email and senha_informada == senha:
        print('Acesso liberado!')
        break
    else:
        print('E-mail ou senha inválidos, tente novamente!')