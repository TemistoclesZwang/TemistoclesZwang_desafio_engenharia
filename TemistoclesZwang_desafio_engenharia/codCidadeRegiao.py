'''
Centro-oeste 201 até 299
Nordeste 300 até 399
Norte 400 até 499
Sudeste 001 até 099
Sul 100 até 199
'''

def codCidadeRegiao(codCidade):
   if codCidade >= 201 and codCidade <= 299:
      return 'Centro-oeste'
   elif codCidade >= 300 and codCidade <= 399:
      return 'Nordeste'
   elif codCidade >= 400 and codCidade <= 499:
      return 'Norte'
   elif codCidade >= 1 and codCidade <= 99: 
      #!verificar o uso do 0 se influencia no calculo
      return 'Sudeste'
   elif codCidade >= 100 and codCidade <= 199:
      return 'Sul'
   else:
      return 'Código inválido'