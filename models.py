# -*- coding: UTF-8 -*-

class Perfil():
	'Classe padrão para perfis de usuários'

	def __init__(self, nome_completo, telefone, empresa):
		self.nome = nome_completo
		self.telefone = telefone
		self.empresa = empresa


	def imprimir(self):
		print 'Nome %s, Telefone %s, Empresa %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def total_curtir(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(nome_arquivo):
		arquivo = open(nome_arquivo,'r')
		perfis=[]
		for linha in arquivo:
			valores = linha.split(',')
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Perfil_vip(Perfil):
	'Classe padrão para perfis de usuários vips'

	def obter_creditos(self):
		return  super(Perfil_vip,self).total_curtir()* 10
