
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem
# from simpleai.search import breadth_first,depth_first,astar,greedy
import simpleai.search

class GameProblem(SearchProblem):

    # Object attributes, can be accessed in the methods below
    
    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None
    SHOPS=None
    CUSTOMERS=None
    MAXBAGS = 0
    num_pizzas = 0
    MOVES = ('West','North','East','South')

   # --------------- Common functions to a SearchProblem -----------------

    def actions(self, state):
        '''Returns a LIST of the actions that may be executed in this state
        '''
        action = ['South', 'North', 'East', 'West','Load','Deliver']
        
        return action
    def move(self,state,action):
        if action == 'South' and ((state[0], state[1]+1) not in self.POSITIONS ['building']):
            next_state = (state[0], state[1]+1)
        elif action == 'North' and ((state[0], state[1]-1) not in self.POSITIONS ['building']):
            next_state = (state[0], state[1]-1)
        elif action == 'East' and ((state[0]+1, state[1]) not in self.POSITIONS ['building']):
            next_state = (state[0]+1, state[1])
        elif action == 'West' and ((state[0]-1, state[1]) not in self.POSITIONS ['building']):
            next_state = (state[0]-1, state[1])
        else:
            next_state = (state[0], state[1])

        return next_state

    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed
        '''
        if state in self.POSITIONS['street']:
            next_state = move(state,action)
        elif state in self.POSITIONS['pizza']:
            if num_pizzas<MAXBAGS:
                num_pizzas = MAXBAGS
            next_state = move(state,['North','South','East','West'])
        else:
            next_state = (state[0],state[1])
        return next_state


    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
        return state in self.GOAL and num_pizzas == MAXBAGS

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

        print '\nMAP: ', self.MAP, '\n'
	print 'POSITIONS: ', self.POSITIONS, '\n'
	print 'CONFIG: ', self.CONFIG, '\n'

        initial_state = self.POSITIONS['start'][0]
        final_state= self.POSITIONS['pizza'][0]
        algorithm= simpleai.search.astar

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

