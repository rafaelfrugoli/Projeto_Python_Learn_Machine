# -*- coding: UTF-8 -*-

def cadastrar (nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual nome deseja remover?'
	remover = raw_input()
	nomes.remove(remover)

def alterar(nomes):
	print 'Digite o nome a ser alterado'
	alterado = raw_input()
	if (alterado in nomes):
		v = nomes.index(alterado)
		print 'Digite o novo nome:'
		alterado = raw_input()
		nomes[v] = alterado
	else:
		print ' Esse nome não existe! '

def nome_procurar(nomes):
	print 'Digite o nome a ser procurado:'
	procurar = raw_input()
	if (procurar in nomes):
		print nomes.index(procurar)


def menu():
	nomes = []
	escolha = ''
	while (escolha != '0'):
		print 'Digite 1 para cadastrar ou 0 para terminar!'
		escolha = raw_input()

		if (escolha =='1'):
			cadastrar(nomes)
		if (escolha=='2'):
			listar(nomes)
		if (escolha == '3'):
			remover(nomes)
		if (escolha =='4'):
			alterar(nomes)
		if (escolha =='5'):
			nome_procurar(nomes)

menu()