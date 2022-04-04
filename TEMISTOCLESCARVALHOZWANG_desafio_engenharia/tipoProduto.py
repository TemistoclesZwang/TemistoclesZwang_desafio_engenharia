dicionarioProduto = {
   'Joias': '001', 
   'Livros': '111', 
   'Eletronicos': '333' ,
   'Bebidas': '555',
   'Brinquedos': '888'
}

def codigosTodosOsProdutos():
   listaCodigos = []
   for produto in dicionarioProduto:
      listaCodigos.append(dicionarioProduto[produto])
   return listaCodigos

def codProdutos(trinca):
   if trinca == '001':
      return 'Joias'

   elif trinca == '111' :
      return 'Livros'

   elif trinca == '333' :
      return 'Eletronicos'

   elif trinca == '555' :
      return 'Bebidas'

   elif trinca == '888' :
      return 'Brinquedos'

