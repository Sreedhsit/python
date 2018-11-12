#!/usr/bin/python

a =10
b=20
if a>b:
    print(a)
else:
    print(b)

even_num=0
odd_num=0

l1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,9):
    if l1[i]%2==0:
        print(l1[i], 'is even number')
        even_num=even_num+1
    else:
        print(l1[i],'is odd number')
        odd_num=odd_num+1


print('No of even number in the Integer list 1 is',even_num)
print('No of odd number in the Integer list 1 is ',odd_num)

age =int(input('Enter your age :'))

if age<10:
    print('Your school going child')
elif age>10 and age<=19:
    print('your are a teenager')
elif age>20 and age<=25:
    print('your are in early 20s')
else:
    print('Your are above 25')



Name = input('Enter the Word   :')
l11 = len(Name)
print(l1)
l2 = int(l11/2)
print(l2)

First_Half = Name[0:l2]
second_half = Name[l2:l11]
print('First of your name ',First_Half)
print('Second of your name ',second_half)
print('Reverse of your name ',Name[::-1])


