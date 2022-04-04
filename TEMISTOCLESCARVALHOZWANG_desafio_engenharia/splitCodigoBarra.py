def cortarCodigo (codigo):
   listaCodigoCortado = []
   numero = 0
   for numero in range (numero, len(codigo)):
      cortar = codigo[numero:numero+3]
      listaCodigoCortado.append(cortar)
      numero=numero+3
   temp = listaCodigoCortado
   codigoCortado=temp[::3]
   return codigoCortado

#;refatorar
#!não precisa disso tudo, basta usar string[posicaoDaTrinca]

# def teste (codigo,posicaoTrinca):
#    # trincas = 0,1,2,3,4
#    for numero in codigo:
#       # print(numero[:3])
#    # return codigo[posicaoTrinca:1:2]

# # print(teste ('123 456',1))