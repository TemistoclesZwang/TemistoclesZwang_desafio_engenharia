from splitCodigoBarra import cortarCodigo

def encontrarTrinca (codigo,PosicaoTrinca):
      separarCadaTrincaDoCodigo = cortarCodigo(codigo)
      trincaDoCodigoInformado = separarCadaTrincaDoCodigo[PosicaoTrinca]
      return trincaDoCodigoInformado