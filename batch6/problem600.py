'''
Given a set of points (x, y) on a 2D cartesian plane,
find the two closest points.
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
'''
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution():
    def __init__(self, points):
        self.points = points
        self.point_map = [Point(p[0],p[1]) for p in self.points]
        self.min_dist = -1

    @staticmethod
    def distance_between_points(point_a, point_b):
        '''
        We use the Pythagoras Theorem to derive a formula for finding the distance between two points in 2- and 3- dimensional space.
        Let P = (x 1, y 1) and Q = (x 2, y 2) be two points on the Cartesian plane (see picture below).
        So the horizontal distance between P and Q is x2 - x1 and the vertical distance between the points is y2 - y1.

        Then from the Pythagoras Theorem we find that the distance between P and Q is
             math.sqrt( ((x1[0]-x2[0])**2)+((y1[1]-y2[1])**2) )
        the square root of the horizontal distance between the points squared plus the vertical distance between the points squared.
        '''
        return math.sqrt( ((point_a.x-point_b.x)**2) + ((point_a.y - point_b.y)**2) )

    def solve(self):
        if len(self.points) < 2:
            return self.min_dist
        temp = 100
        window = [0, 0]
        for index, i in enumerate(self.point_map):
            print(i.x, i.y)
            for j in self.point_map[index+1:]:
                print(j.x, j.y)
                d = self.distance_between_points(i, j)
                if d < temp:
                    window = [i, j]
                    temp = d
        print("The minimum distance is : {} & between [{}, {}] - [{}, {}]".format(temp, window[0].x, window[0].y, window[1].x, window[1].y))
        self.min_dist = temp
        return temp, window

s = Solution(points=[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)])
s.solve()