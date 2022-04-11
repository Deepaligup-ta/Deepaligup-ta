#code 2
class CIRCLE():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self,peri):
       
        self.perimeter=2*radius*(CIRCLE.pi)
        print("perimeter of circle is:",perimeter)
    def Area(self,area):
        
        self.area=(CIRCLE.pi)*radius*radius
        print("area of circle is:",area)

A=CIRCLE(10)
A.perimeter
A.Area
