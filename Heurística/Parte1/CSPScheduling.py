#Importamos la librería
from constraint import *

#Generamos el problema
problem = Problem()

###################################################Variables###################################################

#Clase en cada hora
problem.addVariables(["cienciasDeLaNaturaleza1", "cienciasDeLaNaturaleza2", "cienciasSociales1", "cienciasSociales2", "lenguaCastellanaYLiteratura1", "lenguaCastellanaYLiteratura2", "matematicas1", "matematicas2", "ingles1", "ingles2", "educacionFisica1"], ["L1", "L2", "L3", "M1", "M2", "M3", "X1", "X2", "X3", "J1", "J2"])

#Profesor en cada asignatura
problem.addVariables(["andrea1", "andrea2", "juan1", "juan2", "lucia1", "lucia2"], ["cienciasDeLaNaturaleza", "cienciasSociales", "lenguaCastellanaYLiteratura", "matematicas", "ingles", "educacionFisica"])

###################################################Restricciones###################################################

#Horas consecutivas:
problem.addConstraint(naturalesConsecutivas, (("clase", "profesor", "horario"), ("clase", "profesor", "horario")))

#Cada asignatura se imparte dos veces (Menos E.F.)
problem.addConstraint(AllEqualConstraint(), )

#Solution
print(problem.getSolution())

###################################################Funciones###################################################

def naturalesConsecutivas(x, y, horario1, a, b, horario2):
    if(x==a and x=="cienciasDeLaNaturaleza" and abs(int(horario1[1:])-int(horario2[1:]))==1):
        return True
