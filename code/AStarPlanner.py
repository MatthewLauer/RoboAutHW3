
class AStarPlanner(object):
    
    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        self.nodes = dict()


    def Plan(self, start_config, goal_config):

        plan = []
        
        plan.append(start_config)
        curr_conf = start_config
        # TODO: Here you will implement the AStar planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space
        while (curr_conf != goalconfig):




                
        plan.append(goal_config)

        return plan


class Node:
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth

    def __str__(self):
        #Spits out a full list the node's state/operator and states/operators leading to it
        result = "State: " +  str(self.state)
        result += " Depth: " + str(self.depth)
        if self.parent != None:
            result += " Parent: " + str(self.parent.state)
            result += " Operator: " + self.operator
        return result

        class Closelist:

    def __init__(self):
        #God is dead
        self.close = [[[100000000 for i in range(1)] for j in range(1000)] for k in range(1000)]

    def addNode(self, node):
        self.close[node.state.startpos[0]][node.state.startpos[1]].append(node.state.time)

    def isDuplicate(self, State):
        #print "State"
        #State.stateInfo()
        '''for i in range(0,len(self.close)):
            #self.close[i].state.stateInfo()
            if (self.close[i].state.equals(State)):
                #print "True"
                return True
        #print "False"
        '''
        timelist = self.close[State.startpos[0]][State.startpos[1]]
        for i in range(0, len(timelist)):
            if (timelist[i] == State.time):
                return True
        return False


class Openlist:
    """
    """
    def __init__(self):
        self.open = []
    def __str__(self):
        result = "Open List contains " + str(len(self.open)) + " items\n"
        for item in self.open:
            result += str(item) + "\n"
        return result
    def addNode(self, node):

        lowest = 0
        greatest = len(self.open)
        oldmid = -1
        midpoint = 0

        while(lowest < greatest):
            midpoint = (lowest + greatest)/2
            if(self.open[midpoint].state.getF() == node.state.getF() or oldmid == midpoint):
                lowest = midpoint
                break;
            else:
                if (node.state.getF() < self.open[midpoint].state.getF()):
                    greatest = midpoint
                else:
                    lowest = midpoint+1
            oldmid = midpoint
        self.open.insert(lowest, node)

    def getlowest(self):
        if not self.empty():
            return self.open.pop(0)
        else:
            raise RunTimeError

    def empty(self):
        return len(self.open) == 0