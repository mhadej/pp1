class C():

    def __init__(self, plane):
        self.plane = plane

    def m1(self, n):
        counter = 0
        for i in self.plane:
            if i[0] > 0 and i[1] > 0:
                counter += 1
        if counter >= n:
            return True
        else:
            return False
        
c = C([[2,3],[1,8],[-6,4],[3,-7]])
print(c.m1(2))
print(c.m1(3))