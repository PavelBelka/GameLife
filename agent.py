import math

AGENT_PHY_HEATH = 10
AGENT_PSY_HEATH = 10

class Agent:
    def __init__(self, x, y, world, is_live, is_parent):
        self.ix = x
        self.iy = y
        self.world = world
        self.is_live = is_live
        self.is_parent = is_parent
        self.is_moved = 0
        self.direction_of_moved = [0, 0]
        self.purpose = 0
        self.purpose_coord = [x, y]
        self.psi_health = AGENT_PSY_HEATH
        self.phy_health = AGENT_PHY_HEATH

    def calc_neighbour_count(self, matrix):
        count = 0
        x_zero, x_max, y_zero, y_max = self.world.point_matrix_scanning(self.ix, self.iy)
        for i in range(y_zero, y_max + 1):
            for j in range(x_zero, x_max + 1):
                if j == self.ix and i == self.iy:
                    continue
                if matrix[i][j] == 1:
                    for p in self.world.agent_list:
                        if p.ix == j and p.iy == i and p.is_live == 1:
                            count += 1
        return count

    def purpose_of_movement(self):
        agents = self.world.agent_list
        sum_dist = []
        self.psi_health -= 2
        for a in agents:
            sum_dist.append(math.sqrt(math.pow(a.ix, 2) + math.pow(a.iy, 2)))
        index = sum_dist.index(min(sum_dist))
        return agents[index].ix, agents[index].iy

    def agent_motion(self):
        axis_x = self.purpose_coord[0] - self.ix
        axis_y = self.purpose_coord[1] - self.iy
        if axis_x > 0:
            self.direction_of_moved[0] = 1
        elif axis_x < 0:
            self.direction_of_moved[0] = -1
        else:
            self.direction_of_moved[0] = 0
            if axis_y > 0:
                self.direction_of_moved[1] = 1
            elif axis_y < 0:
                self.direction_of_moved[1] = -1
            else:
                self.direction_of_moved[1] = 0

    def agent_food_motion(self):
        x_zero, x_max, y_zero, y_max = self.world.point_matrix_scanning(self.ix, self.iy)
        for i in range(y_zero, y_max + 1):
            for j in range(x_zero, x_max + 1):
                if self.world.map_food[i][j] != 0 and self.world.map_ag[i][j] != 1:
                    self.purpose_coord[0] = j
                    self.purpose_coord[1] = i
                    self.agent_motion()
                    self.is_moved = 1

    def logic(self, matrix):
        cnt_agents = self.calc_neighbour_count(matrix)
        if self.phy_health < 5:
            val = self.world.get_food(self.ix, self.iy)
            self.phy_health += val
            if self.phy_health > AGENT_PHY_HEATH:
                self.phy_health = AGENT_PHY_HEATH
        if cnt_agents == 0 and self.purpose == 0:
            self.purpose_coord[0], self.purpose_coord[1] = self.purpose_of_movement()
            self.purpose = 1
        if cnt_agents == 0 and self.purpose == 1:
            self.agent_motion()
            self.is_moved = 1
        if cnt_agents > 0:
            self.is_moved = 0
            self.purpose = 0
            if self.phy_health < 9:
                val = self.world.get_food(self.ix, self.iy)
                if val == 0:
                    self.agent_food_motion()
        return cnt_agents

