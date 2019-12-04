import sys

class Bus():
    def __init__(self, parada, nMax, alumnos):
        self.parada=parada
        print(self.parada)
        self.alumnosMax=nMax
        print(self.alumnosMax)
        self.alumnosBus=[]
        print(self.alumnosBus)
        self.alumnosRestantes=alumnos
        print(self.alumnosRestantes)
        print()

class Alumno():
    def __init__(self, parada, colegio):
        self.parada=parada
        self.colegio=colegio


class Parada():
    def __init__(self, nombre, adyacentes, colegio, alumnos):
        self.nombre=nombre
        print(self.nombre)
        self.adyacentes=[]
        print(self.adyacentes)
        self.colegio=colegio
        print(self.colegio)
        self.alumnos=alumnos
        print(self.alumnos)
        print()


class Simulador():
    def initialize():

        flag=0
        flag2=0

        stops={}
        schools={}
        kids={}
        currentStop=0

        fprob=open(sys.argv[1], "r")
        if fprob.mode == 'r':
            problema = fprob.readlines()[1:] #Eliminamos la primera fila
            for line in problema:
                myLine=line.split()

                #Parsea las paradas y sus adyacencias
                if myLine[0][0]=='P' and flag==0:
                    nombre=myLine[0]
                    adyacentes=[]
                    for i in range(len(myLine)):
                        if i!=0:
                            if myLine[i]=='--':
                                adyacentes.append(-1)
                            else:
                                adyacentes.append(int(myLine[i]))
                        stops[nombre]=adyacentes

                #Parsea los colegios y sus paradas
                elif myLine[0][0]=='C' and flag2==0:
                    flag=1
                    for item in range(len(myLine)):
                        myLine[item]=myLine[item].replace(':', '')
                        myLine[item]=myLine[item].replace(';', '')
                    for i in range(1, len(myLine), 2):
                        schools[myLine[i]]=myLine[i-1]

                #Parsea los niños en cada parada
                elif myLine[0][0]=='P':
                    flag2=1
                    for item in range(len(myLine)):
                        myLine[item]=myLine[item].replace(':', '')
                        myLine[item]=myLine[item].replace(';', '')
                        myLine[item]=myLine[item].replace(',', '')

                    kidsList=[] #Lista con todos los alumnos
                    for item in range(len(myLine)):
                        if myLine[item][0]=='P':
                            currentStop=myLine[item]
                            list=[] #Lista con todos los alumnos de una parada
                        elif myLine[item][0]=='C':
                            Clist=[] #Lista con todos los alumnos de un mismo colegio en una parada
                            #Añadimos colegios a una lista temporal hasta que no queden (por si hubiera más de uno)
                            while int(myLine[item-1])>0:
                                Clist.append(myLine[item])
                                myLine[item-1]=str(int(myLine[item-1])-1)
                            for i in Clist:
                                list.append(i)
                                kidsList.append(i)
                            kids[currentStop]=list
                elif myLine[0][0]=='B':
                    currentStop=myLine[1]
                    nMax=myLine[2]

        #Generamos los elementos del problema
        print('---BUS---')
        Bus(currentStop, nMax, kidsList)

        print('---PARADAS---')
        keys=stops.keys()
        for stop in keys:
            Parada(stop, stops[stop], schools[stop] if stop in schools.keys() else 0, kids[stop] if stop in kids.keys() else 0)

    initialize()
