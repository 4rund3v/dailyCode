"""
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""
class Solution():
    def __init__(self, triplet):
        self.triplet = triplet

    @staticmethod
    def check_pythogorea_triplet(triplet):
        status = False
        trip_squares = (i*i for i in triplet)
        hyp = max(triplet)
        if 2*(hyp*hyp) == sum(trip_squares):
            status = True
        return status

    def solve(self):
        if len(self.triplet) != 3:
            print("Given triplet invalid length. {}, {} ".format(self.triplet, len(self.triplet)))
            return False
        status = self.check_pythogorea_triplet(self.triplet)
        if status:
            print("The given Triplet : {} is a valid Triplet".format(self.triplet))
        else:
            print("The given Triplet : {} is  NOT a valid Triplet".format(self.triplet))
        return status

trip = (3, 4, 5)
s = Solution(triplet=trip)
s.solve()
