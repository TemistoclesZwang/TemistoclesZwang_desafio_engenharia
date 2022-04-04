from tipoProduto import codigosTodosOsProdutos, dicionarioProduto
from splitCodigoBarra import cortarCodigo


'''
1)A Loggi não envia produtos que não sejam dos tipos acima informados.
'''
def verificadorDeTipos (codigo):
   separarCadaTrincaDoCodigo = cortarCodigo(codigo)
   trincaFinalDoCodigoInformado = separarCadaTrincaDoCodigo[4] 
   #posicao 4 = ultima trinca do codigo
   for produto in range(0,5):
      if trincaFinalDoCodigoInformado == codigosTodosOsProdutos()[produto]:
         return True
   return False
