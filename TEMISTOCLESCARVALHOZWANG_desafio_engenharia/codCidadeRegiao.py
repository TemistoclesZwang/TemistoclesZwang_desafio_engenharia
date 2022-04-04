'''
Centro-oeste 201 até 299
Nordeste 300 até 399
Norte 400 até 499
Sudeste 001 até 099
Sul 100 até 199
'''

def codCidadeRegiao(codCidade):
   if codCidade >= 201 and codCidade <= 299:
      return 'centroOeste'
   elif codCidade >= 100 and codCidade <= 199:
      return 'sul'
   elif codCidade >= 400 and codCidade <= 499:
      return 'norte'
   elif codCidade >= 300 and codCidade <= 399:
      return 'nordeste'
   elif codCidade >= 1 and codCidade <= 99: 
      return 'sudeste'

