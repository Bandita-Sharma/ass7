#Que1-->Calcultae area and circumference of a circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of circle with radius 5 is:",3.14*self.radius*self.radius)
    def getCircumference(self):
        print("Circumference of circle is:",2*3.14*self.radius)
cir=Circle(5)
cir.getArea()
cir.getCircumference()
print()

#Que2-->Make a class student and display its required info
class Student:
    age=19 # Static Variable
    marks=90
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno 
    
    def display(self):
        print('Name: {}, RollNo: {},'.\
              format(self.name, self.rno), end=' ')
        print('Marks:', self.marks)
        #print(self.country)
        
    def setAge(self):
        return self.age

    def setMarks(self,marks):
        self.marks=marks       
    
s1 = Student('abc', 1)
s1.display()
s2 = Student('def',2)
s2.display()
s3=Student('lmn',3)
s3.display()
print("Age of 3rd student is:",s3.setAge())
print()

#Que3-->Convert Temperature
class Temperature:
    def convertFahreheit(self,c):
        """converts celsius into fahreheit"""
        self.c=c
        print("Conversion of Celsius into Fahrenheit:",1.8*self.c+32)
    def convertCelsius(self,f):
        """converts fahrenheit into celsius"""
        self.f=f
        print("Conversion of Fahrenheit into celsius:",(f-32)*(5/9))

t=Temperature()
t.convertFahreheit(40)
t.convertCelsius(40)
print()

#Que4-->Create a class movie details and perform the functionalities
class MovieDetails:
    def __init__(self, artistname, release,ratings):
        self.artistname = artistname
        self.release = release
        self.ratings = ratings
    
    def display(self):
        print('Movie details are :: Artist Name: {}, Year of Release: {}, Ratings: {}'.\
              format(self.artistname, self.release,self.ratings), end=' ')

    def add(self,mname):
        self.mname=mname
        print("Name of Movie is:",self.mname)
    
artistname=input("enter artist name")
release=int(input("enter year of release"))
rating=int(input("enter the ratings of movie"))
mname=input("enter the movie name")
m=MovieDetails(artistname,release,rating)
m.display()
m.add(mname)
print()


#Que5-->Animal inheritance
class Animal:
    def animal_attribute(self):
        print("This is base class")

class Tiger(Animal):
    def tiger_attr(self):
        print("this is child base")

a=Animal()
a.animal_attribute()
b=Tiger()
b.animal_attribute()
print()

#Que6-->Determine the output
#INVALID SYNTAX
print()

#Que7-->Create class Shape.Initialize with length and breadth create method area.create class rect and sqr which inherits shape and access method area.
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def Area(self):
        return self.length*self.breadth
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super(Rectangle,self).__init__(length,breadth)

class Square(Shape):
    def __init__(self,length):
        super(Square,self).__init__(length,length)

a=Shape(3,6)
b=Rectangle(3,6)
c=Square(3)
print("Area of rectangle is:",b.Area())
print("Area of Square is:",c.Area())
print()
