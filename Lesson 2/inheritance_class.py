# Class Point2D
# Supperclass of Point3D
#  x, y
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def khoangcach(self, other):
        return 0

# Class Point3D
# Point2D subclass
# x, y, z
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def khoangcach(self, other):
        return 0
    
#
p2d = Point2D(1, 2)
p3d = Point3D(1, 2, 3)

print(p2d)