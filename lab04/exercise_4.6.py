# Exercise 6: Rewrite your pay cpmputation with time-and-a-half for over-
# time and create a function called computepay which takes two parameters
# (hours and rate)

def computepay(hours, rate): 
 MAX_HOURS = 40
 if (hours > MAX_HOURS): 
   extra_hours = hours - MAX_HOURS
 else:
   extra_hours = 0
 payment = (hours * rate) + (extra_hours * (rate/ 2))
 return payment

try: 
  hours: float(input("Ingrese el número de hora: "))
  rate: float(input("Ingrese tarifa por hora: "))
  payment = computepay(hours, rate)
  print("El pago es:", payment)
  except:
  print("Eror, favor ingresar un valor numérico")