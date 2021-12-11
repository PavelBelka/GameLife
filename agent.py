
class Agent:
    def __init__(self, x, y, world, is_live, is_parent):
        self.ix = x
        self.iy = y
        self.world = world
        self.is_live = is_live
        self.is_parent = is_parent
        self.psi_health = 10
        self.phy_health = 10

    def calc_neighbour_count(self, matrix):
        count = 0
        if self.ix == 0:
            x_zero = self.ix
            x_max = self.ix + 2
        elif self.ix == (self.world.cx - 1):
            x_zero = self.ix - 2
            x_max = self.ix
        else:
            x_zero = self.ix - 1
            x_max = self.ix + 1
        if self.iy == 0:
            y_zero = self.iy
            y_max = self.iy + 2
        elif self.iy == (self.world.cy - 1):
            y_zero = self.iy - 2
            y_max = self.iy
        else:
            y_zero = self.iy - 1
            y_max = self.iy + 1
        for i in range(y_zero, y_max + 1):
            for j in range(x_zero, x_max + 1):
                if j == self.ix and i == self.iy:
                    continue
                if matrix[i][j] == 1:
                    for p in self.world.agent_list:
                        if p.ix == j and p.iy == i and p.is_live == 1:
                            count += 1
        return count

