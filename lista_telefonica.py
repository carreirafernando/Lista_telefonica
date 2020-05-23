lista_telefonica = {}
def lista(nome):
    if nome in lista_telefonica:
        print(f'Nome: {nome.title()} - Número: {lista_telefonica[nome]}')
    else:
        pergunta = str(input('Não existe esse nome na lista, quer gravar? '))
        if pergunta == 'sim':
            numero = input('Digite o número de telefone: ').strip()
            lista_telefonica[nome] = numero
            print('Contato salvo com sucesso!')

while True:
    print('[SAIR] TERMINAR\n[LISTA] MOSTRA TODOS OS CONTATOS')
    entrada = str(input('Digite um nome: ')).strip()
    if entrada == 'sair':
        break
    elif entrada == 'lista':
        for chave, valor in lista_telefonica.items():
            print(f'Nome: {chave.title()} Número: {valor}')
        break
    lista(entrada)
