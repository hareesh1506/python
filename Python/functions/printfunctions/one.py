print(10)
a=5
print(a,10,15)


for i in [1,2,3,4,5]:
    print(i,end= ' ')

for i in [1,2,3,4,5]:
    print(i)

# default \n
print('hello')
print('hareesh')

# adding \n
print('hello',end=' ')
print('hello',end='->')
print('hareesh')

# unpacking
print(*[1,2,3,4,5,6])
print(*[1,2,3,4,5],sep=',')


# seperate paremeter
print('hello','world')
print('hello','world',sep=' , ')

# adding data to file using print
file = open('sample.txt','w')
print('hello all',file=file)
file.close()