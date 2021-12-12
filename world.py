import numpy as np
import random
from agent import Agent

PSY_COST_OF_POPULATION = 1
PSY_COST_OF_BIRTH = 2
PHY_COST_OF_MOVED = 1
PHY_COST_OF_BIRTH = 4
AMOUNT_OF_FOOD = 10
AMOUNT_GET_FOOD = 2
MINIMAL_NEIGHBOUR = 1
MAXIMAL_NEIGHBOUR = 4

class World:
    def __init__(self, x, y, num_agents, random_seed):
        self.cx = x
        self.cy = y
        self.agents = num_agents
        self.seed = random_seed
        self.map_ag = np.zeros((self.cy, self.cx), dtype= np.bool)
        self.map_food = np.random.randint(0, AMOUNT_OF_FOOD,(self.cy, self.cx), dtype= np.int)
        self.agent_list = []
        random.seed(self.seed)
        for a in range(0, num_agents):
            agent = Agent(random.randint(0, self.cx - 1), random.randint(0, self.cy - 1), self, 1, 0)
            self.agent_list.append(agent)
            self.map_ag[agent.iy, agent.ix] = 1

    def rule(self):
        for item in self.agent_list:
            count = item.logic(self.map_ag)
            if count > MAXIMAL_NEIGHBOUR or count < MINIMAL_NEIGHBOUR:
                item.psi_health -= PSY_COST_OF_POPULATION
            elif 5 > count > 3:
                item.is_parent = 1
            if item.psi_health <= 0 or item.phy_health <= 0:
                item.is_live = 0
            if item.is_moved != 0:
                item.phy_health -= PHY_COST_OF_MOVED

    def point_matrix_scanning(self, x, y):
        if x == 0:
            maximum_x = x + 2
            minimum_x = x
        elif x == (self.cx - 1):
            maximum_x = x
            minimum_x = x - 2
        else:
            maximum_x = x + 1
            minimum_x = x - 1
        if y == 0:
            maximum_y = y + 2
            minimum_y = y
        elif y == (self.cy - 1):
            maximum_y = y
            minimum_y = y - 2
        else:
            maximum_y = y + 1
            minimum_y = y - 1
        return minimum_x, maximum_x, minimum_y, maximum_y

    def get_food(self, x, y):
        value = self.map_food[y, x]
        if value != 0 and value != 1:
            self.map_food[y, x] -= AMOUNT_GET_FOOD
            hand_over = 2
        elif value == 1:
            self.map_food[y, x] -= 1
            hand_over = 1
        else:
            hand_over = 0
        return hand_over

    def update(self):
        for item in self.agent_list:
            if item.is_parent == 1:
                minimum_x, maximum_x, minimum_y, maximum_y = self.point_matrix_scanning(item.ix, item.iy)
                free_cell = False
                for i in range(0, 9):
                    random_x = random.randint(minimum_x, maximum_x)
                    random_y = random.randint(minimum_y, maximum_y)
                    if self.map_ag[random_y][random_x] == 0:
                        free_cell = True
                        break
                if free_cell:
                    item.is_parent = 0
                    item.phy_health -= PHY_COST_OF_BIRTH
                    item.psi_health -= PSY_COST_OF_BIRTH
                    agent = Agent(random_x, random_y, self, 1, 0)
                    self.map_ag[random_y, random_x] = 1
                    self.agent_list.append(agent)
            if item.is_moved:
                if item.direction_of_moved[0] != 0:
                    self.map_ag[item.iy, item.ix] = 0
                    item.ix += item.direction_of_moved[0]
                elif item.direction_of_moved[1] != 0:
                    self.map_ag[item.iy, item.ix] = 0
                    item.iy += item.direction_of_moved[1]
                self.map_ag[item.iy, item.ix] = 1
            if item.is_live:
                continue
            else:
                self.map_ag[item.iy, item.ix] = 0
                self.agent_list.remove(item)

    def get_agents_matrix(self):
        return self.map_ag

    def get_food_matrix(self):
        return self.map_food