class Rectangle:
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth
    def __lt__(self,other):
        area1 = self.__breadth * self.__length
        area2 = other.__breadth * other.__length
        return area1 < area2
    

dimension1 = (input("Enter dimension of first rectangle: ").split(" "));
dimension2 = (input("Enter dimension of second rectangle: ").split(" "));

rectangle1 = Rectangle(int(dimension1[0]),int(dimension1[1]))
rectangle2 = Rectangle(int(dimension2[0]),int(dimension2[1]))



if(rectangle1 > rectangle2):
    print("reactangle 1 is bigger")
else:
    print("reactangle 2 is bigger")
    
    

    