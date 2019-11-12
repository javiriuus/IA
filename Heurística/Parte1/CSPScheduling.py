#Import library
from constraint import *

#Generate problem
problem = Problem()

#Declare variables

    #Ciencias de la Naturaleza -> 1
    #Ciencias Sociales -> 2
    #Lengua castellana y literatura -> 3
    #Matematicas -> 4
    #Ingles -> 5
    #Educacion Fisica -> 6
    #Andrea -> 11
    #Juan -> 12
    #Lucia -> 13

#Lectures with its possible teachers
problem.addVariable("cienciasDeLaNaturaleza", range(11, 14))
problem.addVariable("cienciasSociales", range(11, 14))
problem.addVariable("lenguaCastellanaYLiteratura", range(11, 14))
problem.addVariable("matematicas", range(11, 14))
problem.addVariable("ingles", range(11, 14))
problem.addVariable("educacionFisica", range(11, 14))
#Schedules with its possible lectures
problem.addVariable("l1", range(1, 7))
problem.addVariable("l2", range(1, 7))
problem.addVariable("l3", range(1, 7))
problem.addVariable("m1", range(1, 7))
problem.addVariable("m2", range(1, 7))
problem.addVariable("m3", range(1, 7))
problem.addVariable("x1", range(1, 7))
problem.addVariable("x2", range(1, 7))
problem.addVariable("x3", range(1, 7))
problem.addVariable("j1", range(1, 7))
problem.addVariable("j2", range(1, 7))

#Solution
problem.getSolutions()
