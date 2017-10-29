from models import *
try:
	open('nao_existe.txt','r')
	print('arquivo foi aberto')
	arquivo.close()
except IOError as erro:
	print ('Deu IOError %s' % erro)