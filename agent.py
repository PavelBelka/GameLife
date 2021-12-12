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

    def logic(self, matrix):
        cnt_agents = self.calc_neighbour_count(matrix)
        if self.phy_health < 5:
            while self.phy_health != AGENT_PHY_HEATH:
                val = self.world.get_food(self.ix, self.iy)
                if val == 0:
                    break
                self.phy_health += val
            if self.phy_health > AGENT_PHY_HEATH:
                self.phy_health = AGENT_PHY_HEATH
        if cnt_agents == 0:
            pass

