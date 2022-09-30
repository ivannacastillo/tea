cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1
final = len(cadena)
numero = float(cadena[inicio:final])
print(inicio, final)
print(numero)
print(type(numero))
