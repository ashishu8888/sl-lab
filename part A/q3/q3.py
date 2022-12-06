
class rectangle:

    def __init__(self,height,width):
            self.width = width
            self.height = height

    def getArea(self):
        return self.width*self.height



w = int(input("Enter the width of rectangle\n"))
h = int(input("Enter the height of rectangle\n"))

rec1 = rectangle(w,h)

print("The are of the rectangle is:\n",rec1.getArea())

        