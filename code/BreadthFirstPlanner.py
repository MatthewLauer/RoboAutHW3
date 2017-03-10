import numpy
import matplotlib.pyplot as pl
class BreadthFirstPlanner(object):
    
    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        
    def Plan(self, start_config, goal_config):
        
        plan = []
        if self.visualize and hasattr(self.planning_env, 'InitializePlot'):
            self.planning_env.InitializePlot(goal_config)
        # TODO: Here you will implement the breadth first planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space
        queue_id = []
        plan_id = []
        #print self.planning_env.discrete_env.ConfigurationToNodeId(start_config), self.planning_env.discrete_env.ConfigurationToNodeId(goal_config)
        queue_id.append(int(self.planning_env.discrete_env.ConfigurationToNodeId(start_config)))
        #print queue_id[0] - self.planning_env.discrete_env.ConfigurationToNodeId(goal_config) 
        count = 0;
        while(len(queue_id) >0):
            current = queue_id.pop(0)
            plan_id.append(current)
            if ((current - int(self.planning_env.discrete_env.ConfigurationToNodeId(goal_config))) == 0):
                break
            successors = self.planning_env.GetSuccessors(current)
            
            for i in successors:
                if (int(i) not in queue_id) and (int(i) not in plan_id) :
                    queue_id.append(int(i))
            
            if count > 0:
                #print plan_id[count], count
                print self.planning_env.discrete_env.NodeIdToConfiguration(plan_id[count-1]),self.planning_env.discrete_env.NodeIdToConfiguration(current)
                pl.plot(self.planning_env.discrete_env.NodeIdToConfiguration(plan_id[count-1]),self.planning_env.discrete_env.NodeIdToConfiguration(current),'r.-', linewidth=2.5)
                pl.draw()
            count = count + 1;
            
        print plan_id[14], len(plan_id)

        for i in plan_id:
            plan.append(self.planning_env.discrete_env.NodeIdToConfiguration(i))
        
        #plan.append(start_config)
        #plan.append(goal_config)
   
        return plan
