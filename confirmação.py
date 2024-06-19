senhas = open(r'C:\\Users\\henri\\OneDrive\\Documentos\\pograma\\paito\\projetos\\senhas\\senhas.txt')
senhas = senhas.read().splitlines()
tentativa = input(str('Digite uma de suas senhas:'))
acesso = False
for senha in senhas:#passa por cada item da lista, separadamente
    if tentativa == senha:
        acesso = True
if acesso == True:
    print(f'Acesso permitido! Senha usada: {tentativa}')
else:
    print('Acesso negado! Tente novamente!')
input('CLIQUE QUALQUER TECLA PRA CONTINUAR!')