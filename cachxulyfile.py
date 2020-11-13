file_object = open('home.txt',mode='r')

data = file_object.read()
file_object.seek(0)
data2 = file_object.read()

file_object.close()
print(data)
print(data2)







