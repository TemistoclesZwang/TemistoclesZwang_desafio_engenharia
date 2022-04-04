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
