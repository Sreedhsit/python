import os


print(os.getcwd())

cwd = os.getcwd()

print('Cuurent Path :',cwd )

list_directory= os.listdir('/Users/sreekanth/python/DataTyes/')

len = len(list_directory)

print('No of Files', len)

file = open('/Users/sreekanth/python/DataTyes/FileWrite.txt','w')

#for i in len(list_directory):
#    file.write(list_directory[i])
for i in range(0,5):
        file.write(list_directory[i])
        file.write('\n')

file.close()

read_file = open('/Users/sreekanth/python/DataTyes/FileWrite.txt','r')

print(read_file.read())

#readline
#readlines

read_file.close()



