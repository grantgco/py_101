# class Circle:
#   pi = 3.14
#   def area(self, radius):
#     return (self.pi * radius ** 2)

# circle = Circle()

# pizza_area = circle.area(12/2)
# teaching_table_area = circle.area(36/2)
# round_room_area = circle.area(11460/2)

# print(pizza_area)
# -------------------------------------------------

# class Circle:
#     pi = 3.14
  
#     def __init__(self, diameter):
#         print("New circle with diameter " + str(diameter))
          
# new = Circle(34)

# -------------------------------------------------


can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in can_we_count_it:
  if hasattr(i, "count"):
    print(str(type(i)) + " has the count attribute!")
  else:
    print(str(type(i)) + " does not have the count attribute :(")

# -------------------------------------------------

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle (11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(dir(5))

# -------------------------------------------------

def this_function_is_an_object():
  pass

print(dir(this_function_is_an_object))

# -------------------------------------------------

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):  #iitialize method - fires when the class/object is created
    self.radius = diameter / 2
  
  def __repr__(self): # must only have a self argument and must return a string to define what the object/class is
    return "Circle with radius " + str(self.radius)

  def area(self): 
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# -------------------------------------------------
# PROJECT
# -------------------------------------------------

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self, score):
    if score >= minimum_passing:
      return TRUE

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
