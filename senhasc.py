import secrets
quant = int(input('Quantas senhas você quer? : '))
size = int(input('De quantos digitos você quer sua senha? (RECOMENDADO: Mais que 8 dígitos):'))
passwords = []
#laço de repetição enquanto isso faça isso
for i in range(quant):# ele faz até chegar no número que você definiu dentro do range
    password = secrets.token_urlsafe(size)[:size]
    passwords.append(password)#adiciona as senhas na lista senhas
results= '\n'.join(passwords)
save = open(r'C:\\Users\\henri\\OneDrive\\Documentos\\pograma\\paito\\projetos\\senhas\\senhas.txt', 'w')
save.write(f'{results}\n')
print('Suas senhas foram armazenadas no arquivo senhas.txt')
input('PRESSIONE QUALQUER TECLA PRA FINALIZAR O PROGRAMA!')

