# creating file and insert data
"""
f = open('file1.txt','w')
f.write('name   :  hareesh')
print('done add..')
f.close()
"""

# adding data
"""
f = open('file1.txt','a')
f.write('\n'+'age   :  23')
print('done add..')
f.close()
"""

# read data in file
"""
f=open('file1.txt','r')
content=f.read()
print(content)
f.close()
"""

# Iterating Over File Lines
"""
f=open('file1.txt','r')
for i in f:
    print(i)
f.close()
"""