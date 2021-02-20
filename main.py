import math


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = '( {} , {} )'.format(self.x, self.y)
        return s

    def __eq__(self, other):
        '''
        :type other : point
        '''
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def distance(self, other):
        x = self.x - other.x
        y = self.y - other.y
        dist = math.sqrt((x ** 2) + (y ** 2))
        return dist


class line:
    def __init__(self, a=0, b=0, c=0):
        """
        :type a: float
        :type b: float
        :type c: float
        """
        self.a = a
        self.b = b
        self.c = c  # ax + by + c = 0
        self.slope = -(self.a / self.b)

    def __init__(self, p1, p2):
        """
        :type p1: point
        :type p2: point
        """
        if p1 == p2:
            raise Exception("Both points must be different to make a line")
        elif p1.x == p2.x:
            self.slope = math.inf
            self.a = 0
            self.b = 1
            self.c = -p1.x


        else:
            self.slope = m = (p2.y - p1.y) / (p2.x - p1.x)
            self.a = 1
            self.b = -m
            self.c = (m * p1.x) - p1.y

    def __str__(self):
        s = '({})X + ({})Y + ({}) = 0'.format(self.a, self.b, self.c)
        return s

    def isParallel(self, other):
        """
        :type other : line
        """
        if self.slope == other.slope:
            return True
        else:
            return False

    def isPerpendicular(self, other):
        """
        :type other : line
        """

        if self.slope == math.inf and other.slope == 0:
            return True
        if other.slope == math.inf and self.slope == 0:
            return True
        if self.slope * other.slope == -1:
            return True
        else:
            return False

    def angleBetweenLinesInRadians(self, other):
        """
        :type other: line
        """
        if self.isParallel(other):
            return 0
        elif self.isPerpendicular(other):
            return math.pi / 2
        else:
            tanOfAngle = abs((self.slope - other.slope) / (1 + (self.slope * other.slope)))
            angle = math.atan(tanOfAngle)
            return angle

    def angleBetweenLinesInDegrees(self, other):
        """
        :type other: line
        """
        if self.isParallel(other):
            return 0.0
        elif self.isPerpendicular(other):
            return 90.0
        else:
            tanOfAngle = abs((self.slope - other.slope) / (1 + (self.slope * other.slope)))
            angle = math.atan(tanOfAngle)
            angle = math.degrees(angle)
            return angle

     
#Testing 

p1 = point(1, 0)
p2 = point(2, 0)
p3 = point(3, 0)
p4 = point(3, 10)
l0 = line(p3, p4)
l1 = line(p1, p2)
l2 = line(p2, p3)
print(l1.angleBetweenLinesInDegrees(l0))
print(l1.angleBetweenLinesInRadians(l0))

