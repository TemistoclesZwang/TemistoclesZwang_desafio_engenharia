# Nome: Temitocles Carvalho Zwang
# Universidade: Instituto Federal do Piaui
# Curso: Análise e Desenvolvimento de Sistemas
# 5° Semestre
# Previsão conclusão: 6/2024 (devido a pandemia)

#LEIA O README.PNG PARA ACESSAR O RELATÓRIO E OUTROS DETALHES

from validadorDeCodigoDebarras import encontrarCodigosValidosOuInvalidos
from listaDePacotes import lista_pacotes
from codCidadeRegiao import codCidadeRegiao
from validadorDeCodigoDebarras import codigosDeBarraAprovados
from encontrarTrinca import encontrarTrinca
from validadorDeCodigoDebarras import codigosDeBarraAprovados
from validadorDeCodigoDebarras import codigosDeBarraReprovados
from tipoProduto import codProdutos

#separar o resultado de cada questão
def questao(numeroQuestao):
   print('='*30, 'questao: ',numeroQuestao)

# 1. Identificar a região de destino de cada pacote, com totalização de
# pacotes (soma região);
def identificarRegiaoDescarga(regiaoParaPegarCodigos):
   total = 0
   print(regiaoParaPegarCodigos)
   for numeroDoPacote in lista_pacotes:
      trincaDaRegiao = (encontrarTrinca (lista_pacotes[numeroDoPacote],1))
      regiao = codCidadeRegiao(int(trincaDaRegiao))
      if regiao == regiaoParaPegarCodigos:
         print(numeroDoPacote, lista_pacotes[numeroDoPacote])
         total+=1
   print(f'Soma região: {total}')
   codigosDeBarraAprovados.clear()


# 2. Saber quais pacotes possuem códigos de barras válidos e/ou
# inválidos;
def mostrarCodigosValidosOuInvalidos():
   codigosDeBarraReprovados.clear()
   codigosDeBarraAprovados.clear()
   encontrarCodigosValidosOuInvalidos(lista_pacotes)
   print('CÓDIGOS VÁLIDOS:')
   for pacote in codigosDeBarraAprovados:
      print(pacote,codigosDeBarraAprovados[pacote])
   print('\n')
   print('CÓDIGOS INVÁLIDOS:')
   for pacote in codigosDeBarraReprovados:
      print(pacote,codigosDeBarraReprovados[pacote])


# 3. Identificar os pacotes que têm como origem a região Sul e
# Brinquedos em seu conteúdo;
def identificarRegiaoCadaPacote():
   # encontrarCodigosValidosOuInvalidos(lista_pacotes)
   print('PACOTES COM ORIGEM NO SUL CONTENDO BRINQUEDOS:\n')
   for numeroDoPacote in lista_pacotes:
      trincaDaRegiao = (encontrarTrinca (lista_pacotes[numeroDoPacote],0))
      trincaDoProduto = (encontrarTrinca (lista_pacotes[numeroDoPacote],4))
      regiao = codCidadeRegiao(int(trincaDaRegiao))
      if regiao == 'sul' and trincaDoProduto == '888':
         print(numeroDoPacote, lista_pacotes[numeroDoPacote])


# 4. Listar os pacotes agrupados por região de destino (Considere apenas
# pacotes válidos);
def listarPacotesRegiaoDestino(regiaoParaPegarCodigos):
   codigosDeBarraAprovados.clear()
   encontrarCodigosValidosOuInvalidos(lista_pacotes) 
   print(regiaoParaPegarCodigos)
   print(f'Pacotes: ')
   for numeroDoPacote in codigosDeBarraAprovados:
      trincaDaRegiao = (encontrarTrinca (codigosDeBarraAprovados [numeroDoPacote],1))
      regiao = codCidadeRegiao(int(trincaDaRegiao))
      if regiao == regiaoParaPegarCodigos:
         print(numeroDoPacote, codigosDeBarraAprovados [numeroDoPacote])


# 5. Listar o número de pacotes enviados por cada vendedor (Considere
# apenas pacotes válidos);
def listarNumeroPacotesCadaVendedor():
   listaVendedores = []
   for codigo in codigosDeBarraAprovados:
      trincaVendedor = (encontrarTrinca (codigosDeBarraAprovados[codigo],3))
      nomeVendedor = '\nCodigo do vendedor: '
      codigoDoVendedor = 'pacotes enviados:'
      totalTexto = 'Total:'
      totalValor = 0

      if trincaVendedor not in listaVendedores:
         listaVendedores.append(nomeVendedor)
         listaVendedores.append(trincaVendedor)
         listaVendedores.append(codigoDoVendedor)
         listaVendedores.append(totalTexto)
         listaVendedores.append(totalValor)

         posicaoVendedor = listaVendedores.index(trincaVendedor)
         listaVendedores[posicaoVendedor+1] = listaVendedores\
            [posicaoVendedor+1]+'\n'+codigo + '\nCódigo: '+ \
               codigosDeBarraAprovados[codigo]
         listaVendedores[posicaoVendedor+3] += 1

      elif trincaVendedor in listaVendedores:
         posicaoVendedor = listaVendedores.index(trincaVendedor)
         listaVendedores[posicaoVendedor+1] = listaVendedores\
            [posicaoVendedor+1]+'\n'+codigo + '\nCódigo: '+ \
               codigosDeBarraAprovados[codigo]
         listaVendedores[posicaoVendedor+3] +=1
   return listaVendedores


# 6. Gerar o relatório/lista de pacotes por destino e por tipo (Considere
# apenas pacotes válidos);
def pacotesPorDestinoETipo():
   listaDestinos = []
   for codigo in codigosDeBarraAprovados:
      trincaDestino = (encontrarTrinca (codigosDeBarraAprovados[codigo],1))
      trincaProduto = (encontrarTrinca (codigosDeBarraAprovados[codigo],4))
      codDestino = codCidadeRegiao(int(trincaDestino))
      tipoProduto = codProdutos(trincaProduto)
      destino = '\nDestino: '
      codigoProduto = 'produtos:'

      if codDestino not in listaDestinos:
         listaDestinos.append(destino)
         listaDestinos.append(codDestino)
         listaDestinos.append(codigoProduto)
         listaDestinos.append(tipoProduto +'\n'+ \
            codigo+'\nCódigo: '+ codigosDeBarraAprovados[codigo])

      elif codDestino in listaDestinos:
         posicaoDestino = listaDestinos.index(codDestino)
         listaDestinos[posicaoDestino+2] = listaDestinos[posicaoDestino+2]\
            +'\n'+tipoProduto +'\n'+ codigo +'\nCódigo: '+ \
               codigosDeBarraAprovados[codigo]
   return listaDestinos


# 7. Se o transporte dos pacotes para o Norte passa pela Região
# Centro-Oeste, quais são os pacotes que devem ser despachados no
# mesmo caminhão?
def pacotesParaDespacharNoCaminho():
   codigosDeBarraAprovados.clear()
   encontrarCodigosValidosOuInvalidos(lista_pacotes)
   print('ENTRE A REGIÃO CENTRO OESTE E NORTE, \
      O CAMINHÃO PASSARÁ PELO\nNORDESTE, POR ISSO DEVE LEVAR OS SEGUINTES PACOTES: ')
   listarPacotesRegiaoDestino('centroOeste')
   listarPacotesRegiaoDestino('nordeste')
   listarPacotesRegiaoDestino('norte')


# 8. Se todos os pacotes fossem uma fila qual seria a ordem de carga
# para o Norte no caminhão para descarregar os pacotes da Região
# Centro Oeste primeiro;
def gerarOrdemFila():
   codigosDeBarraAprovados.clear()
   print('SEGUIRIA A SEGUINTE ORDEM: ')
   listarPacotesRegiaoDestino('norte')
   listarPacotesRegiaoDestino('nordeste')
   listarPacotesRegiaoDestino('centroOeste')


# 9. No item acima considerar que as jóias fossem sempre as primeiras a
# serem descarregadas;
def considerarJoias(regiaoParaPegarCodigos):
   codigosDeBarraAprovados.clear()
   encontrarCodigosValidosOuInvalidos(lista_pacotes)
   naoJoias = {}
   print(regiaoParaPegarCodigos)
   for numeroDoPacote in codigosDeBarraAprovados:
      trincaDaRegiao = (encontrarTrinca (codigosDeBarraAprovados[numeroDoPacote],1))
      regiao = codCidadeRegiao(int(trincaDaRegiao))

      if regiao == regiaoParaPegarCodigos:
         naoJoias[numeroDoPacote] = codigosDeBarraAprovados[numeroDoPacote]

   for codigo in naoJoias:
      if naoJoias[codigo][12:] != '001':
         print(codigo)
         print(naoJoias[codigo])

   for codigo in naoJoias:
      if naoJoias[codigo][12:] == '001':
         print(codigo)
         print(naoJoias[codigo])


# 10. Listar os pacotes inválidos.
def mostrarPacotesInvalidos():
   print('CÓDIGOS INVÁLIDOS:')
   encontrarCodigosValidosOuInvalidos(lista_pacotes)
   for pacote in codigosDeBarraReprovados:
      print(pacote)
      print('Código: '+codigosDeBarraReprovados[pacote])
   

def main():
#1
   questao(1)
   identificarRegiaoDescarga('centroOeste')
   identificarRegiaoDescarga('nordeste')
   identificarRegiaoDescarga('norte')
   identificarRegiaoDescarga('sudeste')
   identificarRegiaoDescarga('sul')


# #2 
   questao(2)
   mostrarCodigosValidosOuInvalidos()

# #3
   questao(3)
   identificarRegiaoCadaPacote()


# #4

   questao(4)
   listarPacotesRegiaoDestino('centroOeste')
   listarPacotesRegiaoDestino('nordeste')
   listarPacotesRegiaoDestino('norte')
   listarPacotesRegiaoDestino('sudeste')
   listarPacotesRegiaoDestino('sul')


# #5
   questao(5)
   for i in listarNumeroPacotesCadaVendedor():
      print(i)

# #6 
   questao(6)
   for i in pacotesPorDestinoETipo():
      print(i)
   

# #7
   questao(7)
   pacotesParaDespacharNoCaminho()

# #8
   questao(8)
   gerarOrdemFila()

# #9
   questao(9)
   considerarJoias('norte')
   considerarJoias('nordeste')
   considerarJoias('centroOeste') 

# #10
   questao(10)
   mostrarPacotesInvalidos()


main()