
i=0
while i<=10:
    print(i)
    i=i+1

l1 = [10,20,30,60,5,6]
a =0
b=9999999999
for i in range(0,len(l1)):
    if l1[i]>a:
        a=l1[i]
    elif l1[i]<b:
        b=l1[i]




print('Greater number in the list is ', a)
print('Smallest number in the list is',b)