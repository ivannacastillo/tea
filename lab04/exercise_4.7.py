# Exercise 7: Rewrite the grade program from the previous chapter using 
# a function called computergrade that takes a score as its parameter and
# returns a grade as a string

def computergrade(grade):
  if (grade ≥ 0.9 and grade ≤ 1.0):
    grade = "A"
  elif (grade ≥ 0.8 and grade < 0.9):
    grade = "B"
  elif (grade ≥ 0.7 and grade < 0.8):
    grade = "C"
  elif (grade ≥ 0.6 and grade < 0.7):
    grade = "D"
  elif (grade ≥ 0 and grade < 0.6):
    grade = "F"
  else:
    grade = "Califiación no válida"
  return grade 

try: 
  score = float(input("Ingrese la calificación (0.01 - 1.00): ")
  grade = computergrade(score)
  print("El grado de su califiación es:", grade)
except:
  print("Erro, calificación solamente acepta números")