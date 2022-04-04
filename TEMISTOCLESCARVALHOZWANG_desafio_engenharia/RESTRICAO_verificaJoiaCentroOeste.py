from splitCodigoBarra import cortarCodigo
from tipoProduto import codigosTodosOsProdutos


'''
2)Não é possível despachar pacotes contendo jóias tendo como região de
origem o Centro-oeste;
'''

def verificarCentroOeste(codigo):
   separarCadaTrincaDoCodigo = cortarCodigo(codigo)
   trincaDoCodigoInformado = separarCadaTrincaDoCodigo[0] 
   #0 = primeira trinca
   if int(trincaDoCodigoInformado) >= 201 and int(trincaDoCodigoInformado) <= 299:
      return True
   return False


def verificaJoia (codigo):
   separarCadaTrincaDoCodigo = cortarCodigo(codigo)
   trincaFinalDoCodigoInformado = separarCadaTrincaDoCodigo[4] 
   #posicao 4 = ultima trinca do codigo
   if trincaFinalDoCodigoInformado == codigosTodosOsProdutos()[0] \
      and verificarCentroOeste(codigo) == True:
         return False
   return True


