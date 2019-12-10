import sys

class Bus():
    def __init__(self, parada, nMax, alumnos):
        self.parada=parada
        self.alumnosMax=nMax
        self.alumnosBus=[]
        self.alumnosRestantes=alumnos

    def mover(destino):
        self.parada=destino
        return 0

class Parada():
    def __init__(self, nombre, adyacentes, colegio):
        self.nombre=nombre
        self.adyacentes=adyacentes
        self.colegio=colegio

class Simulador():
    def initialize():

        flag=0
        flag2=0

        adjacents={}
        schools={}
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
                        adjacents[nombre]=adyacentes

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
                        elif myLine[item][0]=='C':
                            Clist=[] #Lista con todos los alumnos de un mismo colegio en una parada
                            #Añadimos colegios a una lista temporal hasta que no queden (por si hubiera más de uno)
                            while int(myLine[item-1])>0:
                                Clist.append(myLine[item])
                                myLine[item-1]=str(int(myLine[item-1])-1)
                            for i in Clist:
                                kidsList.append((i, currentStop))
                elif myLine[0][0]=='B':
                    currentStop=myLine[1]
                    nMax=myLine[2]

        Bus(currentStop, nMax, kidsList)

        keys=adjacents.keys()
        for stop in keys:
            Parada(stop, adjacents[stop], schools[stop] if stop in schools.keys() else 0)

    initialize()
