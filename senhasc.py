import secrets
quant = int(input('Quantas senhas você quer? : '))
tamanho = int(input('De quantos digitos você quer sua senha? (RECOMENDADO: Mais que 8 dígitos):'))
senhas = []
#laço de repetição enquanto isso faça isso
for i in range(quant):# ele faz até chegar no número que você definiu dentro do range
    senha = secrets.token_urlsafe(tamanho)[:tamanho]
    senhas.append(senha)#adiciona as senhas na lista senhas
resultado = '\n'.join(senhas)
save = open(r'C:\\Users\\henri\\OneDrive\\Documentos\\pograma\\paito\\projetos\\senhas\\senhas.txt', 'w')
save.write(f'{resultado}\n')
print('Suas senhas foram armazenadas no arquivo senhas.txt')
input('PRESSIONE QUALQUER TECLA PRA FINALIZAR O PROGRAMA!')

