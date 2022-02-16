####=======================  THread ==================
from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)

t1 = hello()
t2 = hi()

# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()

print('Bye....')

###  ================= Working with File =======================================
## Read File
file = open('data/MyData', mode='r')
# print(file.readline(), end='#')
# print(file.readline())

## Write File
file1 = open('data/Mydata2', 'a')
# file1.write(' Hello.....')

for data in file:
    # print(data)
    file1.write(data)

try:
    with open('data/data.txt') as fileObj:
        lines = fileObj.readlines()
        print(lines)
        # for num, line in enumerate(lines):
        #     print(num+1, line.upper())

except Exception as e:
       print("File Error :  ", e)


##=======================================  BINARY DATA ==========================================================

## write a binary data to file
with open('data/binary', 'wb') as binObj:
    binObj.write(b'life is good') # not saving as binary data

##read  a binary file
with open('data/binary', 'rb') as binObj:
    binary_data = binObj.read()
    # encoded_data = binary_data.encode('utf-8')
    print(binary_data)




#### read  write a  imaage file as binary file  #####
imgFile = open('data/Image.jpg', 'rb')
print(imgFile)

imgFile1 = open('data/image2.jpg', 'wb')
for i in imgFile:
    imgFile1.write(i)




### --------------- Bangla writing-------------------
with open('data/bangla.txt', 'a', encoding='UTF-8') as fileObj:
    fileObj.write('আমার সোনার বাংলাদেশ \n')
    fileObj.write('আমি তোমায় ভাল বাসি  \n')


### --------------- redirect ot file -------------------
## it will redirect to file directly instead printing in the consosle
with open('data/print.txt', 'w') as fileObj:
    print('Nothing Goes unpaid:  ', file=fileObj)


##==============Check if fle exist ================
import os
if os.path.exists('data/bangla.txt'):
    print("Yes....exist ")

###=======================temporary file ========================
from tempfile import TemporaryFile
with TemporaryFile('w+') as obj:
     obj.write(" Life is cool . \n")

     obj.seek(5)  ## 0 indicate the posttion of controoll
     data = obj.read()
     print(data)



##===================== Serialize python object to a byte stream=============================
import pickle

dict_data = {'name' : 'Joytun nur', 'Country' : 'Bangladesh'}
with open('data/serialize', 'wb') as obj:
    pickle.dump(dict_data, obj)

with open('data/serialize', 'rb') as obj:
    dict_data = pickle.load(obj)
    print(dict_data)

###================= CSV fle read and write ==================
### read csv
import csv
# with open('data/data.csv','r') as obj:
#     fcsv = csv.reader(obj)
#
#     sum = 0
#     for i, row in enumerate(fcsv):
#         print(i, row[0], row[1])
#         sum += int(row[1]) if i > 0 else 0
#     print("Total Cost: ", sum)


## write csv
list_item = [ ["Name",'Age','Country'],
              ['Bill Gets', 55,'US'],
              ['Mark Zucarbarg', 34,'US'],
              ['Swift',35,'CANADA']
            ]

with open('data/ppl.csv','w') as obj:
    file_csv = csv.writer(obj)
    file_csv.writerows(list_item)


###=========  JSON data ==================
data ={'Name':'Bill Gets', 'age': 55,'Country':'US'},
    # {'Mark Zucarbarg', 34,'US'],
    # {'Swift',35,'CANADA']

import json
with open('data/json_data.json','w') as obj:
    json.dump(data, obj)

with open('data/json_data.json','r') as obj:
  jsondata = json.load(obj)
  print(jsondata)






