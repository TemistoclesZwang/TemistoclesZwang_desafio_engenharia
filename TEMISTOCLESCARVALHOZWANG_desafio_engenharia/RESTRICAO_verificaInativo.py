from splitCodigoBarra import cortarCodigo

'''
O vendedor 367 está com seu CNPJ inativo e, portanto, não pode mais
enviar pacotes pela Loggi, os códigos de barra que estiverem relacionados
a este vendedor devem ser considerados inválidos
'''

def verificaCnpjInativo (codigo,codigoVendedor):
      separarCadaTrincaDoCodigo = cortarCodigo(codigo)
      trincaDoCodigoInformado = separarCadaTrincaDoCodigo[3] 
      if trincaDoCodigoInformado == codigoVendedor: 
            return True
      return False
