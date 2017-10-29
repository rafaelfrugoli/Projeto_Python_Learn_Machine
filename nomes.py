def convite_nome(convites):
	posicao_inicio = len(convites)-4
	posicao_final =  len(convites)
	parte1 = convites[0:4]
	parte2 = convites[posicao_inicio:posicao_final]
	print '%s %s' % (parte1,parte2)