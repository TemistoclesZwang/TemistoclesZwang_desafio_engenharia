from listaDePacotes import lista_pacotes
from RESTRICAO_verificaTipoInformado import verificadorDeTipos
from RESTRICAO_verificaJoiaCentroOeste import verificaJoia
from RESTRICAO_verificaInativo import verificaCnpjInativo
from encontrarTrinca import encontrarTrinca

codigosDeBarraAprovados = {}
codigosDeBarraReprovados = {}

def encontrarCodigosValidosOuInvalidos(pacotes):

   for chavePacote in pacotes:
      trincaOrigem = int(encontrarTrinca(pacotes[chavePacote],0))
      trincaDestino = int(encontrarTrinca(pacotes[chavePacote],1))

      if trincaOrigem > 499 or trincaDestino < 1:
         codigosDeBarraReprovados[chavePacote] = pacotes[chavePacote]

      elif verificadorDeTipos(pacotes[chavePacote]) and verificaJoia(pacotes[chavePacote]) \
            and verificaCnpjInativo(pacotes[chavePacote],'367') == False:
         codigosDeBarraAprovados[chavePacote] = pacotes[chavePacote]

      elif verificaJoia(pacotes[chavePacote]) == False:
         codigosDeBarraReprovados[chavePacote] = pacotes[chavePacote]

      elif verificadorDeTipos(pacotes[chavePacote]) == False:
         codigosDeBarraReprovados[chavePacote] = pacotes[chavePacote]

      elif verificaCnpjInativo(pacotes[chavePacote],'367') == True:
         codigosDeBarraReprovados[chavePacote] = pacotes[chavePacote]

   # print(codigosDeBarraAprovados)

encontrarCodigosValidosOuInvalidos(lista_pacotes)