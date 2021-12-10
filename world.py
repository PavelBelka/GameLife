import numpy as np
import random
from agent import Agent

class World:
    def __init__(self, x, y, num_agents, random_seed):
        self.cx = x
        self.cy = y
        self.agents = num_agents
        self.seed = random_seed
        self.map_ag = np.zeros((self.cy, self.cx), dtype= np.int)
        self.agent_list = []
        random.seed(self.seed)
        for a in range(0, num_agents):
            agent = Agent(random.randint(0, self.cx - 1), random.randint(0, self.cy - 1), 1, 0)
            self.agent_list.append(agent)
            self.map_ag[agent.iy, agent.ix] = 1

    def check_impossibility(self, x, y):
        check_x = check_y = False
        if 0 < x < self.cx:
            check_x = True
        if 0 < y < self.cy:
            check_y = True
        return check_x, check_y

    def rule(self):
        for item in self.agent_list:
            count = item.calc_neighbour_count(self.map_ag)
            if count > 3 or count < 2:
                item.is_live = 0
            elif count == 3:
                item.is_live = 1
                item.is_parent = 1
            elif count == 2:
                item.is_live = 1

    @staticmethod
    def f_x(item):
        return item.ix

    def update(self):
        for item in self.agent_list:
            if item.is_parent == 1:
                if item.ix == 0:
                    maximum_x = item.ix + 2
                    minimum_x = item.ix
                elif item.ix == (self.cx - 1):
                    maximum_x = item.ix
                    minimum_x = item.ix - 2
                else:
                    maximum_x = item.ix + 1
                    minimum_x = item.ix - 1
                if item.iy == 0:
                    maximum_y = item.iy + 2
                    minimum_y = item.iy
                elif item.iy == (self.cy - 1):
                    maximum_y = item.iy
                    minimum_y = item.iy - 2
                else:
                    maximum_y = item.iy + 1
                    minimum_y = item.iy - 1
                free_cell = False
                for i in range(0, 9):
                    random_x = random.randint(minimum_x, maximum_x)
                    random_y = random.randint(minimum_y, maximum_y)
                    if self.map_ag[random_y][random_x] == 0:
                        free_cell = True
                        break
                if free_cell:
                    item.is_parent = 0
                    agent = Agent(random_x, random_y, 1, 0)
                    self.map_ag[random_y, random_x] = 1
                    self.agent_list.append(agent)
            if item.is_live:
                continue
            else:
                self.map_ag[item.iy, item.ix] = 0
                self.agent_list.remove(item)

    def get_agents_matrix(self):
        return self.map_ag