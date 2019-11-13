#Importamos la librería
from constraint import *

#Generamos el problema
problem = Problem()

#Clases
problem.addVariable("clase", ["cienciasDeLaNaturaleza", "cienciasSociales", "lenguaCastellanaYLiteratura", "matematicas", "ingles", "educacionFisica"])

#Horarios
problem.addVariable("horario", ["L1", "L2", "L3", "M1", "M2", "M3", "X1", "X2", "X3", "J1", "J2"]])

#Profesores
problem.addVariable("profesor", ["andrea", "juan", "lucia"])

#Solution
problem.getSolutions()
