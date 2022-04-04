from RESTRICAO_verificaTipoInformado import verificadorDeTipos
from RESTRICAO_verificaJoiaCentroOeste import verificaJoia
from RESTRICAO_verificaInativo import verificaCnpjInativo


def verificarTipo(codigoDeBarra):
   if verificadorDeTipos(codigoDeBarra) == True:
      return True
   else:
      return False

def verificarJoiaCentroOeste(codigoDeBarra):
   if verificaJoia(codigoDeBarra) == True:
      return True
   else:
      return False

def verificarVendedoresInativos(codigoDeBarra):
   if verificaCnpjInativo(codigoDeBarra,'367') == False:
      return True
   else:
      return False

