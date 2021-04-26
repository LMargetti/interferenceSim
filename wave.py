import math


class Source:
    def __init__(self, x, y, time_period, resolution):
        self.pos = [x, y]
        self.tp = time_period
        self.res = resolution

    def create_points(self, output_velocity, time):
        set_of_points = []
        for i in range(self.res):
            pt = Point(self.pos[0],
                       self.pos[1],
                       output_velocity,
                       time,
                       (math.pi / self.res) * i)  # fires wave points
            set_of_points.append(pt)
        return set_of_points
