# --------------------------------------------
#                Regular Expression
# --------------------------------------------
import re
date_data = '13/Feb/2019 I will go to canada'
if re.match(r'\d+/[a-zA-Z]+/\d{4}', date_data):
    print ('Match')
else:
    print ('not Match')

#=----------------- use regx repeatdly ----------------
##  without r we can use double \\ in the starting of regx
date_data = '13/Feb/2019 I will go to canada'
date_pattern = re.compile('\\d+/[a-zA-Z]+/\d{4}')

print(' Without r ')
if date_pattern.match(date_data):
    print('Matched...')
else:
    print('not Match')

#=----------------- use regx repeatdly ----------------
date_data = '13/Feb/2019 I will go to canada  10/Jan/2019 kdfdg 13/Feb/2020'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

result = date_pattern.findall(date_data)
print(result)

#=----------------- use regx repeatdly ----------------
date_data = '25/June/2019 I will go to canada  10/Jan/2019 kdfdg 13/Feb/2020'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
result = date_pattern.match(date_data)
print(" group res = ", result.group(0) )

for x in range(0, 4):
    print(result.group(x))

print(result.groups())
day, month, year = result.groups()
print('Today is : ', day)
print('Month is : ', month)
print('Year is : ', year)


#=----------------- use regx repeatdly ----------------
##  without r we can use double \\ in the starting of regx
date_data = '25/June/2019 I will go to canada  10/Jan/2019 kdfdg 13/Feb/2020'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
# result = date_pattern.match(date_data)
print("before date_data  = ", date_data)

date_data_modify=date_pattern.sub(r'\3-\2-\1', date_data)
print("After modify date_data  = ", date_data_modify)


#=----------------- use regx repeatdly ----------------
##  without r we can use double \\ in the starting of regx
date_data = '25/June/2019 I will go to canada  10/Jan/2019 kdfdg 13/Feb/2020'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

def to_upper(m):
    return '{} {} {}'.format(m.group(3), m.group(2).upper(), m.group(1))

date_modified =  date_pattern.sub(to_upper,date_data)
print("After...  date_data  = ", date_modified)


#============= Case insensetive sarch ===
text = " I am GOOD, but I am not very good"
list = re.findall('good',text,flags = re.IGNORECASE)
print(list)

text = " I am GOOD, but I am not very good"
list = re.sub('gOOd', 'bad', text, flags = re.IGNORECASE)
print(list)

#------- Unicode Character -----
num = re.compile(r'\d+')
list = num.findall('৪৫৬৭ আমার দেশের নাম বাংলাদেশ')
print(list)

#------------- stripe unwanted space  -------
text ='Life               is           good '
texre = re.compile(r'\s+')
text = texre.sub('_', text)
print(text)

