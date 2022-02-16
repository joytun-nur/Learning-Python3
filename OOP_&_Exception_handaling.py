### ===================== Classs =================================
class Restuarant:
     name= ''
     owner = ''

     def details(self):
         print(self.name,self.owner)

     def details_address(self, address):
         print(self.name, self.owner)
         print(address)

res1 =  Restuarant()
res1.name = ' Doi Ghor'
res1.owner = ' Rahim'
res1.details()
res1.details_address('Dhaka')
print(type(res1))


##  ==========================  Constructor  ===============================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep=' | ')


p = Person('Bill', 55)
p.details()
print(p.name, p.age)

## ============= Dynamic object creation ================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self,name):
        self.name = name

    def details(self):
        print(self.name, self.age, sep=' | ')

people_list = []
for i in range(0, 3):
    p = Person("Person" + str(i), 30+i)
    people_list += [p]

for x in people_list:
    x.details()

prson_x = Person("AAA",20)
prson_x.details()
prson_x.name ="bbb"
prson_x.details()

prson_x.change_name('vvvv')
prson_x.details()

###  ====================== Object Lifecycle =======================
class X:
    def __init__(self,name):
        self.name=name
        print(self.name + "  is Created ")
    def __del__(self):
        print(self.name + "  is destroyed")


x=X('a')
y=X('b')
print('hello world')


def hell():
    x = X('g')
    y = X('h')


hell()

##=================== INheritance , multiple inheritance ==========


class Math:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def sum(self):
        return self.x + self.y


class MathExtend (Math):
    def __init__(self, x, y):
        super().__init__(x, y)

    def sum(self):   # Method Overriding
        return self.x + self.y + 100

    def subtract(self):
        return self.x - self.y

    def show_all(self):
        print("show_all Sum: " + str(super().sum()))
        print("show_all Sum: " + str(self.sum()))
        print("show_all subtract:" + str(self.subtract()))


class mathDivision:
    def dividion(self, x, y):
        return x / y

class Mathextend2(MathExtend,mathDivision):
    def __init__(self, x, y):
        super().__init__(x,y)

    def multiplication(self):
        return self.x  * self.y


math_obj = Math(3, 7)
print(math_obj.sum())

math_obj2 = MathExtend(10, 2)
print(math_obj2.sum())
print(math_obj2.subtract())
print(math_obj2.show_all())

math_ext2 = Mathextend2(10,2)
print("sum = " + str(math_ext2.sum()))
print("subtract = " + str(math_ext2.subtract()))
print("multiplication = " + str(math_ext2.multiplication()))
print("Division = " + str(math_ext2.dividion(math_ext2.x, math_ext2.y)))


##======================== class variable vs instance variable========
class Alien:
    legs = 5  # Class variable

    def __init__(self, name):
        self.nam = name    # nam ia a instance variable

alien1 = Alien('Maven')
alien2 = Alien('Oven')
print(alien1.nam, alien2.nam)
print(alien1.legs, alien2.legs)

Alien.legs = 10  ## changed by using the name of class or by class variable
print(alien1.legs, alien2.legs)

alien1.legs = 11 ## changerd the value of one object variable only. classs variable will not effect
print(alien1.legs, alien2.legs)

alien2.__class__.legs = 22  ## now the class variable will be changed bi object / instance variable
print(alien1.legs, alien2.legs)  #

##================================  Exception  =====================


def div(x, y):
    try:
        result = x / y
    # except ZeroDivisionError:
    #     print(' Divide by zero')
    #     return None
    # except TypeError:
    #     print(' String can not be  Divide')
    #     return None
    except Exception as e:
        print(' error occure ', e)
        return None

    return result


print(div(4, 2))
print(div('4', '2'))
print(div('asa', '2'))
print(div(4, 0))


##   finally
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print(' Error division by zero')
    else:
        print("result is :", result)
    finally:
        print("==== Execute Finally Clause===")

div(100,5)
div(100,0)
# div('100',0)
##==================================  PASS ===============

try:
    div_result = div(4,1)
except:
    pass # dont show anything to used
else:
    print("Result is : " + str(div_result))

##======== Multiple exception ===========
## ====== As Touple or chain==============
try:
    file = open('filename')
except(FileNotFoundError, PermissionError):
    print("Can not open the file")


try:
    file = open('filename')
except FileNotFoundError:
    print(" File doesn't exist")
except PermissionError:
    print("Permission Denied to open ")


##===========   Create  custom exception =====
class VouleNOtExcepted(Exception):
    def __init__(self,message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

def check_chrs(words):
    for char in words:
        if char.lower() in ['a','e','i','o','u']:
            raise VouleNOtExcepted(" Voule is not accepted", 1001)

    return words


try:
    print(check_chrs('Love'))
    print(check_chrs('My'))
except Exception    as e:
    print("Error Reason: " + e.message)
