from simpleai.search import SearchProblem
# from simpleai.search import breadth_first,depth_first,astar,greedy
import simpleai.search

class GameProblem(SearchProblem):
    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None
    SHOPS=None
    CUSTOMERS=None
    MAXBAGS = 0
    MOVES = ('West','North','East','South')
    customer3 = 0
    customer2 = 0
    customer1 = 0
    created = 0

   # --------------- Common functions to a SearchProblem -----------------

    def actions(self, state):
        
        actions=[]

        position = state[0]
        carried = state[1]
        deliver = state[2]
        
        North = (position[0], position[1]-1)
        South = (position[0], position[1]+1)
        West = (position[0]-1, position[1])
        East = (position[0]+1, position[1])
        
        if North in self.POSITIONS['street'] or North in self.SHOPS or North in self.CUSTOMERS or North in self.POSITIONS['start']:
            actions.append('North')
        if South in self.POSITIONS['street'] or South in self.SHOPS or South in self.CUSTOMERS or South in self.POSITIONS['start']:
            actions.append('South')
        if West in self.POSITIONS['street'] or West in self.SHOPS or West in self.CUSTOMERS or West in self.POSITIONS['start']:
            actions.append('West')
        if East in self.POSITIONS['street'] or East in self.SHOPS or East in self.CUSTOMERS or East in self.POSITIONS['start']:
            actions.append('East')
        
        if position in self.POSITIONS['pizza'] :
            actions.append('Load')
            if North in self.POSITIONS['street'] or North in self.SHOPS or North in self.CUSTOMERS or North in self.POSITIONS['start']:
                actions.append('North')
            if South in self.POSITIONS['street'] or South in self.SHOPS or South in self.CUSTOMERS or South in self.POSITIONS['start']:
                actions.append('South')
            if West in self.POSITIONS['street'] or West in self.SHOPS or West in self.CUSTOMERS or West in self.POSITIONS['start']:
                actions.append('West')
            if East in self.POSITIONS['street'] or East in self.SHOPS or East in self.CUSTOMERS or East in self.POSITIONS['start']:
                actions.append('East')

        try:
            self.POSITIONS['customer3']
        except:
            pass
        else:
            if position in self.POSITIONS['customer3']:
                actions.append('Deliver')
        
        try:
            self.POSITIONS['customer2']
        except:
            pass
        else:
            if position in self.POSITIONS['customer2']:
                actions.append('Deliver')
        
        try:
            self.POSITIONS['customer1']
        except:
            pass
        else:
            if position in self.POSITIONS['customer1']:
                actions.append('Deliver')
        
        print state
        print actions
        return actions

    def result(self, state, action):
        #If on a pizzeria pick up bags
        if state[0] in self.POSITIONS['pizza'] and action == 'Load':
            next_state = (state[0], state[1]+2, state[2])
	    print "pillo dos pizza"

        #If on a house deliver and remove customer from tuple
        #We first check that this type of customer exists
        try:
            self.POSITIONS['customer3']
        except:
            pass
        else:
            if state[0] in self.POSITIONS['customer3'] and state[1]>=3 and action == 'Deliver':
                self.POSITIONS['customer3'] = self.POSITIONS['customer3'][1:]
                next_state = (state[0], state[1]-3, state[2]-3)
        
        try:
            self.POSITIONS['customer2']
        except:
            pass
        else:
            if state[0] in self.POSITIONS['customer2'] and state[1]>=2 and action == 'Deliver':
                self.POSITIONS['customer2'] = self.POSITIONS['customer2'][1:]
                next_state = (state[0], state[1]-2, state[2]-2)
		print "dejo las pizzas"
        
        try:
            self.POSITIONS['customer1']
        except:
            pass
        else:
            if state[0] in self.POSITIONS['customer1'] and state[1]>=1 and action == 'Deliver':
                self.POSITIONS['customer1'] = self.POSITIONS['customer1'][1:]
                next_state = (state[0], state[1]-1, state[2]-1)

        if action == 'South' and ((state[0][0], state[0][1]+1) not in self.POSITIONS ['building']) and state[0][1]+1<self.CONFIG['map_size'][1]:
            next_state = ((state[0][0], state[0][1]+1), state[1], state[2])
        elif action == 'North' and ((state[0][0], state[0][1]-1) not in self.POSITIONS ['building']) and state[0][1]-1>=0:
            next_state = ((state[0][0], state[0][1]-1), state[1], state[2])
        elif action == 'East' and ((state[0][0]+1, state[0][1]) not in self.POSITIONS ['building']) and state[0][0]+1<self.CONFIG['map_size'][0]:
            next_state = ((state[0][0]+1, state[0][1]), state[1], state[2])
        elif action == 'West' and ((state[0][0]-1, state[0][1]) not in self.POSITIONS ['building']) and state[0][0]-1>=0:
            next_state = ((state[0][0]-1, state[0][1]) , state[1], state[2])
        else:
            next_state = (state[0], state[1], state[2])

        return next_state

    def is_goal(self, state):
        return state == self.GOAL

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        return 1

    def heuristic(self, state):
        '''Returns the heuristic for `state`
        '''
        return 0


    def setup (self):
        '''This method must create the initial state, final state (if desired) and specify the algorithm to be used.
           This values are later stored as globals that are used when calling the search algorithm.
           final state is optional because it is only used inside the is_goal() method

           It also must set the values of the object attributes that the methods need, as for example, self.SHOPS or self.MAXBAGS
        '''

        print('\nMAP: ', self.MAP, '\n')
        print('POSITIONS: ', self.POSITIONS, '\n')
        print('CONFIG: ', self.CONFIG, '\n')
        
        try:
            self.POSITIONS['customer3']
        except:
            self.customer3 = 0
        else:
            self.customer3 = 1 #Exists
        
        try:
            self.POSITIONS['customer2']
        except:
            self.customer2 = 0
        else:
            self.customer2 = 1 #Exists    
        
        try:
            self.POSITIONS['customer1']
        except:
            self.customer1 = 0
        else:
            self.customer1 = 1 #Exists

        if self.customer3 == 1 and self.created == 0:
            deliver = len(self.POSITIONS['customer3'])*3
            self.CUSTOMERS=self.POSITIONS['customer3']
            self.created = 1
        
        if self.customer2 == 1 and self.created == 0:
            deliver = len(self.POSITIONS['customer2'])*2
            self.CUSTOMERS=self.POSITIONS['customer2']
            self.created = 1
        elif self.customer2 == 1 and self.created == 1:
            deliver += len(self.POSITIONS['customer2'])*2
            self.CUSTOMERS.append(self.POSITIONS['customer2'])

        if self.customer1 == 1 and self.created == 0:
            deliver += len(self.POSITIONS['customer1'])
            self.CUSTOMERS=self.POSITIONS['customer1']
        elif self.customer1 == 1 and self.created == 1:
            deliver = len(self.POSITIONS['customer1'])
            self.CUSTOMERS.append(self.POSITIONS['customer1'])
        
        initial_state = (self.POSITIONS['start'][0], 0, deliver)
        final_state= (self.POSITIONS['start'][0], 0, 0)
        algorithm= simpleai.search.astar
        self.SHOPS=self.POSITIONS['pizza']
        return initial_state,final_state,algorithm

    def printState (self,state):
        '''Return a string to pretty-print the state '''
        pps=''
        return (pps)

    def getPendingRequests (self,state):
        ''' Return the number of pending requests in the given position (0-N). 
            MUST return None if the position is not a customer.
            This information is used to show the proper customer image.
        '''
        return None

    # -------------------------------------------------------------- #
    # --------------- DO NOT EDIT BELOW THIS LINE  ----------------- #
    # -------------------------------------------------------------- #

    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string
           
           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None

    def getStateData (self,state):
        stateData={}
        pendingItems=self.getPendingRequests(state)
        if pendingItems >= 0:
            stateData['newType']='customer{}'.format(pendingItems)
        return stateData
        
    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf
        self.AGENT_START = tuple(conf['agent']['start'])

        initial_state,final_state,algorithm = self.setup()
        if initial_state == False:
            print ('-- INITIALIZATION FAILED')
            return True
      
        self.INITIAL_STATE=initial_state
        self.GOAL=final_state
        self.ALGORITHM=algorithm
        super(GameProblem,self).__init__(self.INITIAL_STATE)
            
        print ('-- INITIALIZATION OK')
        return True
        
    # END initializeProblem 

