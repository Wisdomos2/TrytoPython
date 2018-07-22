#-*-coding:utf-8-*-

myname = 'junseo'

#print("my name is " + myname)

fomatstring1 = "fomatting sample1 %s " % "---test"

#print((fomatstring1+'\n')*5)

arr = ['1', '2', '3', '4', '5', '6']
arr2 = ['7', '8', '9', '10', '11', '12']
arr3 = [arr, arr2]

"""
arr2.insert(0, 13)
print(arr2)
arr2.remove('12')
print(arr2)
arr2.sort()
print("sort", arr2)
arr2.reverse()
print(arr2)
"""


# 리스트와 튜플의 차이점 : 리스트 - 가변 / 튜플 - 불변


# key / value
weeks_diction = {'1': 'monday', '2' : 'tuResday', '3': 'Wednesday', '4' : 'thursday',
                 '5': 'friday'}
"""
print(weeks_diction['1'])

del weeks_diction['5']

print(weeks_diction)

print(weeks_diction.keys())
print(weeks_diction.values())
print(weeks_diction.get('3'))
print(len(weeks_diction))
"""


#조건문
"""
age = -1

if (age <= 16) and (age >= 1):
    print("ok")
elif (age <= 32) and (age >= 17):
    print("no")
elif not (age == -1):
    print("0보다 큼 ")
else:
    print("ㅎㅎ")
"""

#반복문
"""
for i in range(0, 10):
    print(i),
"""

i = 0
while i <= 10:
    if i == 9:
        i = i+10
        print(i),
        break
    print(i),
    i = i+1

i = 0
while i <= 10:
    i = i + 1
    if (i % 2) == 1:
        continue
    print(i),

print('\n')

arr_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for y in arr_list:
    print(y),
