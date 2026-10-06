'''
oop --> object oriented programming
it is a principle or paradigm which revolves objects


it has two main concepts
Attributes(data)--> Attributes of an object
Methods(Behaviour)--> it performs the actions for the object

An object is a real wordld entity, whereas class is a blueprint of an object



Syntax--> class is the keyword

class Classname:
    """ "Doc-string" """
    #attributes(characteristics)
    """ """""" """'
    """ """""" """'

    #methods(behaviour)
    def method(self):

    """ """
    Statements.....
    """ """
a = ClassName()
b = ClassName()

(or)


ClassName:
""" "docstring" """''
def __init__(self,attrs):
.........................
.........................
........................





class Students:
    """Students class with basic details"""

    # Attributes
    name = "Bhanu"
    age = 23
    location = "vizag"

    # Behaviour(Actions)
    def details(self):
        print(f"{self.name} is {self.age} years old and is from {self.location}")


s1 = Students()
print(dir(s1))
print(s1.age, s1.name, s1.location)
s1.details()
print(s1.__class__)
print(s1.__doc__)
print(s1.__dict__)


s2 = Students()
s2.name = "Nani"
s2.age = 25
s2.location = "vjy"
s2.details()



class students:
    """Students class with Actions"""

    def Profile(self, name, age, email_id, mobile):
        self.name = name
        self.age = age
        self.email = email_id
        self.phone = mobile

    def display(self):
        print(f"Student name is {self.name}")
        print(f"Student email id is {self.email} and age is {self.age}")


s1 = students()
s1.Profile('Bhanu', 23, 'bhanu@123@gmail.com', 78945463210)

s1.display()
print(s1.__dict__)
s2 = students()
s2.Profile("Sampath", 16, "sampath@gmail.com", 9874563210)
print(s2.__dict__)
'''


#task --> Create a Cars class which has attributes as brand,colour,price
'''
class Cars:
    def specifications(self,brand,colour,price):
        self.brand = brand
        self.colour = colour
        self.price = price

    def display(self):
        print(f"Brand of Car is {self.brand}")
        print(f"Car Colour is {self.colour} and price is {self.price}")
Car = Cars("BMW M4",)        

'''



#Encapsulation --> it is one of the key features of oop, it bindsthe data and methods around a 
#the data


'''

class Users:
    def __init__(self,name):
        self.name = name  #public attribute
    def details(self):
        print(f'User name is {self.name}')


u1 = Users('Bhanu')
u1.details()
print(u1.name)
u1.name = "Nani" #modifying public attribute
u1.details()


'''


#Protected attributes : This is generally preferred in Developer point of view
# as 

'''
class users:
    def __init__(self,name,_otp):
        self.name = name
        self._otp = _otp
    def details(self):
        print(f'User name is {self.name}')
u1 = users("Bhanu",8520)
print(u1._otp)
u1._otp = 2580
print(u1._otp)
'''
#private attribute -->


#python breaches it by name mangling,but we prefer usage of setters and getters those are termed as 
#accessors or modifiers

'''
class users:
    def __init__(self,name,_otp,__password):
        self.name = name#public attribute
        self._otp = _otp#protected
        self.__password = __password # private attribute

    def details(self):
        print(f'User name is {self.name}')
u1 = users("Bhanu",8520,"Reddy2569")
u1.details()
print(u1.name)
#print(u1.__password) it raises error as we made it private
print(u1._otp)
u1.__password = "tamati"
print(u1._users__password)


class users:
    def __init__(self,name,_otp,__password):
        self.name = name#public attribute
        self._otp = _otp#protected
        self.__password = __password # private attribute
    def get_password(self):
        return "***"
        #return self.__password
    def set_password(self,new_password):
        if len (new_password) >= 6:
            self.__password = new_password
            print("Password is Updated")
        else:
            print("Your password length must be grater than 6 Characters")
    def details(self):
        print(f'User name is {self.name}')
u1 = users("Bhanu",8520,"admin")
print(u1.get_password())
u1.set_password("Admin2")
print(u1.get_password())
print(u1.__dict__)
u2 = users("nani",6541,"asdfghjkl")
print(u2.get_password())
u2.set_password("tam")
print(u2.get_password())
print(u2.__dict__)

#Task : Use Getter and Setter methods for both Protected 
class users:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        def full_name(self):
            return self.fname + self.lname

u1 = users("Bhanu","Reddy")        

print(u1.full_name())

class users_v2(users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.lname.title().strip()
u1 = users_v2("Bhanu","Reddy")
print(u1.full_name())
print(u1.update_name())



class RBI:
    """"Base Class"""
    cash = 10000000 #Class variable
    #classmethod
    @classmethod
    def available_cash(cls):
        print(f'Available cash with RBI is {cls.cash}')

u1 = RBI()
print(u1.cash)
u1.available_cash()
print(RBI.cash)
RBI.available_cash()


class SBI(RBI):
    """Derived class"""
    pass


u1 = SBI()
u1.available_cash()

class HDFC(RBI):
    """Derived class-2"""
    cash = 5000000 #class variable
    @classmethod
    def hdfc_cash(cls):
        print(f"HDFC Cash is {cls.cash}")
        print(f'Total Cash is {cls.cash + RBI.cash}')
u1 = HDFC()
print(u1.cash)
u1.available_cash()
u1.hdfc_cash


#Task 1 
# Convert same into heirarchy also use public,private,along with class methods,class variables usage

#Kid-Father Property Scenario -->Constructor Overriding,method Overriding
class Father:
    """Father Property only in-terms of cash"""
    def __init__(self):
        self.property = 5000000
    def father_prop(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
#    pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self):
        self.property = 250000
    def kid_prop(self):
        print(f'Kid property is {self.property}')
        print(f'Total property is {self.property + self.property}')
#obj = Kid()
#obj.father_prop()
obj = Kid()
print(obj.property)
obj.father_prop()
obj.kid_prop()

class Father:
    """Father Property only in-terms of cash"""
    def __init__(self):
        self.fproperty = 5000000
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
#class Kid(Father):
#    pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.kproperty = 250000
    def kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total property is {self.kproperty + self.fproperty}')

obj1 = Kid()
obj1.father_prop()
obj1.kid_prop()


class Father:
    """Father Property only in-terms of cash"""
    def __init__(self,prop1):
        self.fproperty = prop1
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
#class Kid(Father):
#    pass
class Kid(Father):
    """Kid has started earning"""
    def __init__(self,prop2,prop1):
        super().__init__(prop1)#calling superclass constructor
        self.kproperty = prop2
    def kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total property is {self.kproperty + self.fproperty}')

u1 = Kid(450000,2500000)
u1.father_prop()
u1.kid_prop()

'''

#Method overriding --> when we define same method name in same parent class and also child class
class Square:
    def __init__(self,x):
        self.x = x
    def area(self):
        return f'Area of Square is {self.x**2}'
class Rectangle(Square):
    def __init__(self,y,x):
        super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print(f'Area of Rectangle is {self.x*self.y}')
x,y = map(int,input("Enter th values: ").split(','))        
obj1 = Rectangle(y,x)
obj1.area()

#Method Overriding will only happen with only inheritance usage

#Task-2: bring out a real time scenario for multiple inheritance