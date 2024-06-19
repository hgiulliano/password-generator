import secrets
tamanho = int(input('De quantos digitos você quer sua senha? (RECOMENDADO: Mais que 8 dígitos):'))
senha = secrets.token_urlsafe(tamanho)[:tamanho]
#[:] -> em caso de strings é um limitador, já que seleciona os primeiros caracteres da lista baseado no tamanho fornecido
senha2 = secrets.token_bytes(tamanho).hex()[:tamanho]
senha3 = secrets.token_hex(tamanho)[:tamanho]
print(f'As opções de senhas geradas foram: \n {senha} \n {senha2:} \n {senha3}')
#open serve pra abrir ou criar um arquivo, o w é de write, que é uma arquivo que pode receber texto
save = open(r'C:\\Users\\henri\\OneDrive\\Documentos\\pograma\\paito\\projetos\\senhas\\senhas.txt', 'w')
#a estrutura do open é path|mode
save.write(f'{senha}\n{senha2}\n{senha3}')
print('Suas senhas foram armazenadas no arquivo senhas.txt')
input('PRESSIONE QUALQUER TECLA PRA FINALIZAR O PROGRAMA!')
