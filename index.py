import os
movices = ['author',123,'activeor', {
}]
for item in movices:
	print(item)

names = ['jhon',['china','japanse'],'xyz']
print(names, True, 4)

data = open('test.txt')
for item in data:
    print(item)
data.close()


if os.path.exists('test.txt'):
    list = open('test.txt')

    for l in list:
        print('l', l)
    list.close()
else:
    print('the datafile is missing')
