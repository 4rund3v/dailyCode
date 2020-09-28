"""
 Suppose you are given two lists of n points,
  one list p1, p2, ..., pn on the line y = 0
   and
  the other list q1, q2, ..., qn on the line y = 1.
  Imagine a set of n line segments connecting each point pi to qi.
  Write an algorithm to determine how many pairs of the line segments intersect.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Given three colinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'


def on_segment(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
        (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False

def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Colinear orientation
        return 0


def do_intersect(p1, q1, p2, q2):
    '''
      The main function that returns true if
      the line segment 'p1q1' and 'p2q2' intersect.
    '''
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if ((o1 == 0) and on_segment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if ((o2 == 0) and on_segment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if ((o3 == 0) and on_segment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if ((o4 == 0) and on_segment(p2, q1, q2)):
        return True
    # If none of the cases
    return False


# Driver program to test above functions:
p1 = Point(1, 1)
q1 = Point(10, 1)
p2 = Point(1, 2)
q2 = Point(10, 2)

if do_intersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")

p1 = Point(10, 0)
q1 = Point(0, 10)
p2 = Point(0, 0)
q2 = Point(10, 10)

if do_intersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")

p1 = Point(-5, -5)
q1 = Point(0, 0)
p2 = Point(1, 1)
q2 = Point(10, 10)

if do_intersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")


class Solution():
    def __init__(self, p, q):
        self.intersecting_pairs = 0
        self.y0_points = []
        for x in p:
            temp = Point(x, 0)
            self.y0_points.append(temp)

        self.y1_points = []
        for x in q:
            temp = Point(x, 1)
            self.y1_points.append(temp)

    def solve(self):
        for i1, i2 in range(0, len(self.y0_points), 2):
            p1 = self.y0_points[i1]
            p2 = self.y0_points[i2]
            for j1, j2 in range(0, len(self.y1_points), 2):
                q1 = self.y0_points[i1]
                q2 = self.y0_points[i2]
                if do_intersect(p1, q1, p2, q2):
                    self.intersecting_pairs += 1
        print("Total number of intersecting pairs are: {} ".format(self.intersecting_pairs))
        return self.intersecting_pairs
