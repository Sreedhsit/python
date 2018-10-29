#!/usr/bin/python

findnames = "This is a example to search the values with start and end"

l1 =['Sreekanth Reddy Kamtam','Havish Reddy Kamtam','Deepika Reddy Kamtam','Deepika Inugla']
l2 = l1
l3=l1+l2
var='this'
print(findnames.startswith(var.capitalize(),0,len(findnames)))

print(findnames.endswith('end',0,len(findnames)))

print(l1)
print(len(l1))

cnt=0

for i in range(0,len(l1)):
    if l1[i].endswith('Kamtam'):
        cnt=cnt+1
print ('Surname Ending with Kamtam found',cnt,'people in Newcastle in a search of', len(l1))
    #print(l1[i].endswith('Kamtam'))
cnt1=0
for i in range(0,len(l3)):
    if l3[i].endswith('Kamtam'):
        cnt1=cnt1+1

print('Surname Ending with Kamtam found',cnt1,'people in Newcastle in a search of', len(l3))
