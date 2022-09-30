# Execise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of 
# the numbers instead of the average. 

maximo = 0
minimo = 0
primer_numero = True
while True: 
  try:
    input_str = input("Ingrese un número: ")
    if (input_str == 'done'):
      break
    else:
      if (primer_numero):
        maximo = int(input_str)
        minimo = int(input_str)
        primer_numero = False
      else:
        if (int(input_str) > maximo): maximo = int(input_str)
        if (int(input_str) < minimo): minimo = int(input_str)
  except:
    print("Valor no es válido")
    continue
print("Máximo:", maximo)
print("Mínimo:", minimo)