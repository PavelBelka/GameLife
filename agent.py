
class Agent:
    def __init__(self, x, y, is_live, is_parent):
        self.ix = x
        self.iy = y
        self.is_live = is_live
        self.is_parent = is_parent

    def calc_neighbour_count(self, matrix):
        count = 0
        if self.ix > 0:
            x_zero = self.ix - 1
            x_max = self.ix + 1
        else:
            x_zero = 0
            x_max = self.ix + 2
        if self.iy > 0:
            y_zero = self.iy - 1
            y_max = self.iy + 1
        else:
            y_zero = 0
            y_max = self.iy + 2
        for i in range(y_zero, y_max):
            for j in range(x_zero, x_max):
                if i == self.ix and j == self.iy:
                    continue
                if matrix[i][j] == 1:
                    count += 1
        return count

