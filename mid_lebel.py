

""" ================================================ LIST ======================================  """
cars = ['honda', 'toyota', 'audi']
print(cars[0])
print(cars[2])

"""  MIX LIST   """
mix_list = [ 'honda', 23, 2.5, False ]
print(mix_list[-1])

"""   Matrix   """
matrix = [
          [12,3,4,5],
          [5,6,4,2],
          [5,6,9,3],
          [6,7,1,3]
         ]

for x in matrix:
   for y in x:
      print(y, end=' ')
   print()

list = [3, 4, 't0', 7, 20]
print(list[2:-2])

cars = ['honda', 'toyota', 'audi']
for car in cars:
   print(car)


sum = 0
list_number = [2, 4, 6, 7, 9, 9]
for num in list_number:
   sum += num
print("sum = {sm}".format(sm=sum))


sum = 0
list_number = [2, 4, 6,'aaa', 7, 9.9]
for num in list_number:
   if type(num) == int:
       sum += num
print("sum = {sm}".format(sm=sum))



"""   LIST mmodification   """
mix_list = [2, 4, 6,'aaa', 7, 9.9]
print(mix_list)
mix_list[3] = 'bbb'
print(mix_list)

mix_list.append('aaa')
print(mix_list)

mix_list += ['ccc']
print(mix_list)

mix_list.insert(2,'xxx')
print(mix_list)

"""  Delete item in list """
del mix_list[2]
print(mix_list)

del mix_list[2:5]
print(mix_list)

cars = ['honda', 'toyota', 'audi']
last_car = cars.pop()
print(last_car)
print(cars)

cars = ['honda', 'toyota', 'audi']
last_car = cars.pop(1)
print(last_car)
print(cars)


numbers = [2, 4, 6, 7, 8, 9,23,45]
print(numbers)
numbers.remove(4)
print(numbers)


"""  String to list """
import re
cars = 'honda, prado, toyota , audi'
car_list = re.split(',', cars)
print(car_list)


"""         list  to  string      """
cars = ['honda', ' prado', ' toyota ', ' audi']
str = ' '.join(cars)
print(str)

"""    Sorting """
cars = ['honda', ' prado', ' toyota ', ' audi']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

"""   NUmber reverse  """
numbers = [1,2,3,4]
numbers.reverse()
print(numbers)
print(len(numbers))


if 2 in numbers:
   print('yes')

if 20 not in numbers:
   print('yes...')



""" ============================================  TOUPLE  ========================================================= """

tp = 1,2,3,'aa', False
print(tp, type(tp))
print(tp[0], tp[2], tp[-2], tp[-1], sep=' | ')

# iteration
for t in tp:
   print(t)


# compare
t1 = 1,2,3
t2 = 1,3,4
if t1==t2:
   print(" equal")
else:
   print("not")

###  Immeutable

tp = 1,3,5,'bill'
print(tp)
#tp[1] = 'aaa'  #will not ork
#print(tp)

## unpacking or multiple assignment
tp = 3, 5, 7
x, y, _ = tp
print(x, y, sep=' | ')

""" =========================DICTIONARY  ======================="""
#   dict = {key : value}
dict = {}
dict['name'] = "Swift"
dict['age'] = 44
dict[5] = 1111
print(dict['name'], ' | ', dict['age'],' | ', dict[5])


dict= {'name':'aaa','father':'ddddd'}
print(dict['name'])
print(dict)
print(len(dict))

dict['mother'] = 'ccc'
print(dict)

del dict['father']
print(dict)


num_dict = {
    'a': 34,
    'b': 57,
    'c': 26
 }
for key, value in num_dict.items():
    print(key, value, sep=' -> ')
for key in num_dict:
    print(key)
for value in num_dict.values():
    print(value)

for key in sorted(num_dict.keys()):
    print(num_dict[key])

"""================FUNCTION ====================="""

def welcome(name):
    print('hello {name}'.format(name=name))
    for a in range(1, 11):
        print("HI..", a)

welcome('joytun')



def person_details(name, age, country="Bangladesh"):
    print(name, age, country, sep=' | ')

person_details('JOhn',20,'AUS')
person_details('Mona',20,'USA')
person_details(name= 'Mona', age=20, country = 'USA')
person_details('Bill',20)


## REturning values
def square(num):
    return num * num
print (square(2), square(2.2), sep=' | ')

#optional argument
def getname(first,last,middle=''):
    full_name = first
    if middle:
        full_name += middle
    full_name += last
    return full_name

print(getname('Bill ','Gets '))
print(getname('Muhammad ','Sm '))
print(getname('Hazrat ','Sm ','Muhammad '))


##   value type parameter
num = 100
def change_num(num):
    num += 100
    print('Inner num = {num}'.format(num=num))

change_num(num)
print('Outer num = ',num)

## Reference type paameter
num_list = [1,2,3,4,5]
num_dict = {'one':1, 'two':2, 'three':3}

def change_num_list(num_list, num_dict):
    del num_list[0]
    num_list[-1] = 50

    del num_dict['one']
    num_dict['three'] = 44
    print('Inner list : ', num_list)
    print('Inner Dict', num_dict)

print('--- Befour call-----')
print(' list : ', num_list)
print(' Dict', num_dict)

change_num_list(num_list, num_dict)

print('--- After call-----')
print(' list : ', num_list)
print(' Dict', num_dict)
## So list and dictionary are reference type parameters
## when te passed in a function as arguments

""" ================================== Arbitrary number of arguments ================="""
def students(captain , *student_name):
    print(captain, type(captain))
    print(student_name, type(student_name))
    for student in student_name:
        print(student)

students('Bill', 'Steve', 'Jack')
#students()
students('Millar')


## put ** to receive arbitrary data as dictionary
def students(captain, **other_students):
    print(captain, type(captain))
    print(other_students, type(other_students))

students(captain ="Mahmud", Second_captain ='FUAD', third_captain='emon')

 ##  ==============================  Lambda  ========================

add_number = lambda x, y: x+y
print(add_number(2, 3))

bd_public = lambda name: " bd ppl " + name
print(bd_public('Joy'))

