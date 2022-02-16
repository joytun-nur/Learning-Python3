class X:
  def show(self):
      print("hello Joytun. Welcome to python World.")

x =X()
x.show()

"""   Variables  """

name = " Item List"
detail = "Buy from supershop "
number_of_items = 2
budgets = 2000
amount_of_rice = 5.5
buy_today = True

print(name, type(name))
print(detail, type(detail))
print(number_of_items, type(number_of_items))
print(budgets, type(budgets))
print(amount_of_rice, type(amount_of_rice))
print(buy_today, type(buy_today))
print("================================")

"""==================String  Operation ================"""
title = "Those is python basic"
print(title[0], title[1], title[2], title[-2], title[-1])

"""  Immetuable  """
# not alowed to re assign any character of string . you can just access it .
#title[0] = "A" ## Error

"""   Build in finction """
name = " helen killer"
print(name.title())
print(name.upper())
print(name.lower())
print(name.upper().lower().title())

"""  String Concatanation  """
first = "aaa"
second = "bbb"
print(first +" "+second)
print(first + "\n" + second)

"""   STRIPE   """
name = "     myName     "
print('*' + name + '*')
print('*' + name.lstrip().rstrip() + '*')


shop = "Rahim's shop"
print(shop)
shop = 'Rahim"s shop'
print(shop)
shop = 'Rahim\'s shop'
print(shop)

#find text
sentence = "A Quick brown fox jump over the laizy dog "
print(sentence.find('fox'))
print(sentence.find('foxs'))

# Replace text
sentence = sentence.replace('dog','fox')
print(sentence)
sentence = sentence.replace('fox','tiger')
print(sentence)


"""   Separator     """
x="aaa"
y="bbb"
z= "ccc"
print(x+" | "+y+" | "+z)
print(x,y,z, sep='|')


"""      String interpolation      """
person = "BIll's age is 77"
print(person)
person = "{name}'s age is {age}"
print(person.format(name='Bill', age=77))

person = "%s's age is %d"
print(person % ('Bill',88))


name = " taylor swift"
part = name[7:-1]
print(part)

"""     Condition     """
#num = input(" Please enter a number")
num=88
num = int(num)
if num == 50:
    print("half")
elif num == 100:
    print("full ")
elif num > 100:
    print(" grater  ")
else:
    print("unknown ")

"""    Logical operator   """
num = 5
if num >= 3 or num < 10:
    print(" 3 to 10")

num = 11
if num >= 3 and num < 10:
    print(" 3 to 10")
else:
    print(" not 3 to 10")


"""   Compare  string  """
name1 = "Shifa"
name2 =  "shifa"

if name1.lower() == name2.lower():
    print("same name")
else:
    print("  different name  ")


"""   Loop   """
sum = 0
for n in range(1, 11):
    print(n)
    sum += n
print("sum is {sm}".format(sm=sum))

name = "Apple"
for char in name:
    print(char)





