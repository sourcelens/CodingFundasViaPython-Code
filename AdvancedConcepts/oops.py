# #oops
# #https://johnfoster.pge.utexas.edu/numerical-methods-book/PythonIntro_ObjectOrientedProgramming.html

# class Anything():
#      pass

# s = Anything()
# print(s)





# class Shape():    
#     def __init__(self):
#         self.shape = 'shape'
        
#     def __str__(self):
#         return "I am a {}.".format(self.shape)
    
# s = Shape()
# print(s)


# class Polygon(Shape):
    
#     def __init__(self):
#         self.shape = 'polygon'
#         self.side_lengths = None
        
#     def compute_perimeter(self):
#         return sum(self.side_lengths)
    
#     def get_number_of_edges(self):
#         return len(self.side_lengths)

# p = Polygon()
# print(p)
# print(p.shape)

# #p.compute_perimeter()
# #p.get_number_of_edges()



# class Rectangle(Polygon):
    
#     def __init__(self):
#         self.shape = 'rectangle'
#         self.side_lengths = [1, 1, 1, 1]

# obj = Rectangle()
# print(obj)
# print( obj.get_number_of_edges() )
# print( obj.compute_perimeter())


# class Triangle(Polygon):
    
#     def __init__(self):
#         self.shape = 'triangle'
#         self.side_lengths = [2, 2, 2] 



# obj = Triangle()
# print(obj)
# print( obj.get_number_of_edges() )
# print( obj.compute_perimeter())


# class SourceLensTriangle(Triangle):
    
#     def __init__(self, shapename, input_side_lens):
#         self.shape = shapename
#         self.side_lengths = input_side_lens 

# obj = SourceLensTriangle("Special sourcelens triangle",[3,4,5])
# print(obj)
# print( obj.get_number_of_edges() )
# print( obj.compute_perimeter())


class Car():
    whells = 4

    def __init__( self, name, enginetype ):
        self.name = name
        self.__enginetype = enginetype
    
    def run(self):
        print ( "Running car with engine type " + self.__enginetype)

myCar = Car("Slcar", "turbo")
myCar.run()
#public access
print ( "Num of wheel of myCar ",  myCar.whells ) #static
print ( "Name of myCar is " +  myCar.name ) 

#private not accessable
#print ( "Enginetype of myCar is " +  myCar.__enginetype )

myGreenCar = Car("Tesla", "ElonMusk")
myGreenCar.run()
#public access
print ( "Num of wheel of myGreenCar ",  myGreenCar.whells ) #static
print ( "Name of myGreenCar is " +  myGreenCar.name ) 
print ( "Name of myCar is " +  myCar.name ) 
myGreenCar.run()
myCar.run()





class Animal:
	def speak(self):
		raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "Baaw"

class Cat(Animal):
	def speak(self):
		return "Meeow"

# Create a list of Animal objects
animals = [Dog(), Cat(), Animal()]

# Call the speak method on each object
for animal in animals:
	print(animal.speak())




