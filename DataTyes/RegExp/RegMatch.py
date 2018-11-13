import re

NamedString = 'Sreekanth lear ning Python'

_a = re.match('Sree',NamedString,re.I|re.M)

#print(_a)
print(_a.group())

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""

print(re.split('\s+', text)) # split the text around 1 or more space characters

ragex =re.compile(('\s+'))

print(ragex.split(text)) # split the text around 1 or more space characters


print('# find all numbers within the text')

#_anum = re.split('\d+',text)
#print(_anum)

ragex_num = re.compile('\d+')
print(ragex_num.split(text))
print(ragex_num.findall(text))

"""
regex.match() also returns a match object. But the difference is, it requires the pattern to be present at the beginning of the text itself.
"""

"""
regex.search() returns a particular match object that contains the starting and ending positions of the first occurrence of the pattern.
"""

