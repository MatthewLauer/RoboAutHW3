import time
import bisect
class AStarPlanner(object):
    
    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        self.nodes = dict()
        self.open = Openlist(planning_env)
        self.close = Closelist(planning_env)


    def Plan(self, start_config, goal_config):
        start_time = time.time()

        plan = []
        
        start_node = Node(0,None,0,self.planning_env.discrete_env.ConfigurationToNodeId(start_config))
        self.open.addNode(start_node)
        # TODO: Here you will implement the AStar planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space
        goal_id = self.planning_env.discrete_env.ConfigurationToNodeId(goal_config)
        self.open.setGoal(goal_id)
        suc_node = start_node
        while (self.open.isEmpty() == False):
            #import IPython
            #IPython.embed()
            curr = self.open.getlowest()
            self.close.addNode(curr.id)
            if curr.id == goal_id:
                suc_node = curr
                break
            successors = self.planning_env.GetSuccessors(curr.id)
            for i in range(0, len(successors)):
                if (self.close.isDuplicate(successors[i]) == False):
                    newnode = Node(curr.cost+1,curr,curr.depth+1, successors[i])
                    self.open.addNode(newnode)

        while (suc_node.id != start_node.id):
            plan.insert(0,self.planning_env.discrete_env.NodeIdToConfiguration(suc_node.id))
            suc_node = suc_node.parent
        plan.insert(0,start_config)
        print("--- %s seconds ---" % (time.time() - start_time))
        import IPython
        IPython.embed()
        return plan


class Node:
    def __init__(self, cost, parent, depth, id):
        self.cost = cost
        self.parent = parent
        self.depth = depth
        self.id = id

    def __str__(self):
        #Spits out a full list the node's state/operator and states/operators leading to it
        result = "Cost: " +  str(self.cost)
        result += " Depth: " + str(self.depth)
        result += " ID: " + str(self.id)
        if self.parent != None:
            result += " Parent: " + str(self.parent.id)
        return result


class Closelist:

    def __init__(self, env):
        #import IPython
        #IPython.embed()
        self.close = []

    def addNode(self, id):
        bisect.insort(self.close,id)

    def isDuplicate(self, id):
        #import IPython
        #IPython.embed()
        if(bisect.bisect_left(self.close,id) == len(self.close)):
            return False
        if (self.close[bisect.bisect_left(self.close,id)] == id):
            return True
        return False


class Openlist:
    def __init__(self, env):
        self.env = env
        self.open = []
        self.goal_id = None
    def __str__(self):
        result = "Open List contains " + str(len(self.open)) + " items\n"
        for item in self.open:
            result += str(item) + "\n"
        return result
    def setGoal(self, goal_id):
        self.goal_id = goal_id

    def addNode(self, node):
        lowest = 0
        greatest = len(self.open)
        oldmid = -1
        midpoint = 0

        while(lowest < greatest):
            midpoint = (lowest + greatest)/2
            if(self.open[midpoint].cost+self.env.ComputeHeuristicCost(self.open[midpoint].id, self.goal_id) == node.cost+self.env.ComputeHeuristicCost(node.id, self.goal_id) or oldmid == midpoint):
                lowest = midpoint
                break;
            else:
                if (node.cost+self.env.ComputeHeuristicCost(node.id, self.goal_id) < self.open[midpoint].cost+self.env.ComputeHeuristicCost(self.open[midpoint].id, self.goal_id)):
                    greatest = midpoint
                else:
                    lowest = midpoint+1
            oldmid = midpoint
        self.open.insert(lowest, node)

    def getlowest(self):
        if not self.isEmpty():
            return self.open.pop(0)
        else:
            raise RunTimeError

    def isEmpty(self):
        return len(self.open) == 0