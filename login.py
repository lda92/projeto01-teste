import getpass

user = str(input('Digite o usuário: ')).lower()
senha = getpass.getpass('Digite a senha: ', stream=None)

user_certo = 'lucas'
senha_certa = '1234'

cores = {
    'limpa':'\033[m',
    'verde':'\033[1;42m',
    'vermelho':'\033[1;41m'
}

print('-'*40)

if user == user_certo and senha == senha_certa:
    print('{}Login realizado com sucesso!{}'.format(cores['verde'], cores['limpa']))

if user != user_certo and senha == senha_certa:
    print('{}Usuario incorreto!{}'.format(cores['vermelho'], cores['limpa']))

if user == user_certo and senha != senha_certa:
    print('{}Senha incorreta!{}'.format(cores['vermelho'], cores['limpa']))

if user != user_certo and senha != senha_certa:
    print('{}Usuário e senha incorretos...{}'.format(cores['vermelho'], cores['limpa']))

print('-'*40)
