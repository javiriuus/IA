#Importamos la librería
from constraint import *

#Generamos el problema
problem = Problem()

################################################### Variables ###################################################

#Clase en cada hora
problem.addVariables(["cienciasSociales1", "cienciasSociales2", "lenguaCastellanaYLiteratura1", "lenguaCastellanaYLiteratura2", "cienciasDeLaNaturaleza1", "cienciasDeLaNaturaleza2", "matematicas1", "matematicas2", "ingles1", "ingles2", "educacionFisica1"], ["L1", "L2", "L3", "M1", "M2", "M3", "X1", "X2", "X3", "J1", "J2"])

#Profesor en cada asignatura, añado sólo andrea para facilitar las restricciones
problem.addVariables(["andrea1", "andrea2", "lucia1", "lucia2", "juan1", "juan2"], ["cienciasDeLaNaturaleza", "cienciasSociales", "lenguaCastellanaYLiteratura", "matematicas", "ingles", "educacionFisica"])

################################################### Funciones ###################################################

def naturalesConsecutivas(naturales1, naturales2):
    if(naturales1[:1]==naturales2[:1] and abs(int(naturales1[1:])-int(naturales2[1:]))==1):
        return True

def matesPrimera(mates1, mates2):
    if(int(mates1[1:])==1 and int(mates2[1:])==1):
        return True

def socialesUltima(sociales1, sociales2):
    if(sociales1 in ["L3", "M3", "X3", "J2"] and sociales2 in ["L3", "M3", "X3", "J2"]):
        return True

def coincidenciaMates(mates1, mates2, naturales1, naturales2, ingles1, ingles2):
    if(mates1[:1] not in [naturales1[:1], naturales2[:1], ingles1[:1], ingles2[:1]] and mates2[:1] not in [naturales1[:1], naturales2[:1], ingles1[:1], ingles2[:1]]):
        return True

def luciaAndrea(andrea1, andrea2, lucia1, lucia2):
    if((andrea1 == "educacionFisica" or andrea2 == "educacionFisica") and (lucia1 == "cienciasSociales" or lucia2 == "cienciasSociales")):
        return True
    elif((andrea1 != "educacionFisica" and andrea2 != "educacionFisica") and (lucia1 != "cienciasSociales" and lucia2 != "cienciasSociales")):
        return True

def juan(juan1, juan2, naturales1, naturales2, sociales1, sociales2):
    if((juan1 == "cienciasDeLaNaturaleza" or juan2 == "cienciasDeLaNaturaleza") and (naturales1 not in ["L1", "J1"] and naturales2 not in ["L1", "J1"])):
        return True
    if((juan1 == "cienciasSociales" or juan2 == "cienciasSociales") and (sociales1 not in ["L1", "J1"] and sociales2 not in ["L1", "J1"])):
        return True

################################################### Restricciones ###################################################

#Mates primera
problem.addConstraint(matesPrimera, ("matematicas1", "matematicas2"))

#Sociales última
problem.addConstraint(socialesUltima, ("cienciasSociales1", "cienciasSociales2"))

#Mates no con naturales e inglés
problem.addConstraint(coincidenciaMates, ("cienciasSociales1", "cienciasSociales2", "cienciasDeLaNaturaleza1", "cienciasDeLaNaturaleza2", "ingles1", "ingles2"))

#Horas consecutivas
problem.addConstraint(naturalesConsecutivas, ("cienciasDeLaNaturaleza1", "cienciasDeLaNaturaleza2"))

#Lucia sociales <==> Andrea E.Física
problem.addConstraint(luciaAndrea, ("andrea1", "andrea2", "lucia1", "lucia2"))

#Juan no da naturales ni sociales si se dan a primera lunes o jueves
problem.addConstraint(juan, ("juan1", "juan2", "cienciasDeLaNaturaleza1", "cienciasDeLaNaturaleza2", "cienciasSociales1", "cienciasSociales2"))

#Cada asignatura se imparte en horarios diferentes y cada profesor da clases diferentes
problem.addConstraint(AllDifferentConstraint())

#Solución
print(problem.getSolution())
