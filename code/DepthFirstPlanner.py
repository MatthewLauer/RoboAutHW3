
import DiscreteEnvironment as DE
import numpy as np
class DepthFirstPlanner(object):

    
    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        self.nodes = dict()



    def Plan(self, start_config, goal_config):
        plan =[]
	Lowerlimits = self.planning_env.lower_limits;
	Upperlimits = self.planning_env.upper_limits;
	obj = DE.DiscreteEnvironment(.2, Lowerlimits, Upperlimits)
	
	a = obj.ConfigurationToGridCoord(goal_config)
	b = obj.ConfigurationToGridCoord(start_config)
	targetnodeid = obj.GridCoordToNodeId(a)
	currentnodeid = obj.GridCoordToNodeId(b)

	
	plannodeid = []
	while (targetnodeid != currentnodeid):
		plannodeid.append(currentnodeid)
		
		

		temp = self.planning_env.GetSuccessors(currentnodeid)
		count = 0
		for index in range(0,2):
			if temp[count] in plannodeid:
				count = count+1
		currentnodeid = temp[count]
		print temp
		
	plannodeid.append(targetnodeid)

	
	
	import IPython
	IPython.embed()



	
	

	
        
        # TODO: Here you will implement the depth first planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space

        #plan.append(start_config)
	for i in range(0,len(plannodeid)):
		plan.append(obj.NodeIdToGridCoord(plannodeid[i]))



        #plan.append(goal_config)
        return plan
