# area of circle

class AreaOfCircle():
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius


    def area_circle(self):
        print(f"Area of cirle: { self.PI * self.radius**2}")



area = AreaOfCircle(5)
area.area_circle()