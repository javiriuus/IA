import sys

class Bus():
    def __init__(self, parada, nMax, alumnos):
        self.parada=parada
        self.alumnosMax=nMax
        self.alumnosBus=[]
        self.alumnosRestantes=alumnos

class Alumno():
    def __init__(self, parada, colegio):
        self.parada=parada
        self.colegio=colegio


class Parada(): 
    def __init__(self, nombre, adyacentes, colegio, alumnos):
        self.nombre=nombre
        self.adyacentes=[]
        self.colegio=colegio
        self.alumnos=alumnos


class Simulador():
    def initialize():
        flag=0
        fprob=open(sys.argv[1], "r")
        if fprob.mode == 'r':
            problema = fprob.readlines()[1:]
            for line in problema:
                myLine=line.split()
                if myLine[0][:1]=='P' and flag==0:
                    nombre=myLine[0]
                    adyacentes=[]
                    for i in range(len(myLine)):
                        if i!=0:
                            if myLine[i]=='--':
                                adyacentes.append(-1)
                            else:
                                adyacentes.append(int(myLine[i]))
                        print(nombre + ":")
                        print(adyacentes)
                else:
                    flag=1

    initialize()
