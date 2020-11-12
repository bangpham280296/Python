f = '%d' %(5.77)
print(f)

name = 'Phạm Thanh Bằng'
address = 'Sài Gòn'
phone = '0923354253'

result = f' Họ và tên: {name}\n Địa chỉ: {address}\n Điện thoại:{phone}'
print(result)

demo = '1 là :{one} \n2 là: {two}'.format(one = 111, two = 222)
print(demo)

r = '{:*^10}'.format('Bằng')
print(r)


r1 = '+{:=<5} + {:=^20} + {:=>5}+'.format('','','')
r2 = '|{:<5} | {:^20} | {:>5}|'.format('name','Địa chỉ','Sđt')
r3 = '|{:<5} | {:^20} | {:>5}|'.format('name','Địa chỉ','Sđt')
r4 = '|{:<5} | {:^20} | {:>5}|'.format('name','Địa chỉ','Sđt')
r5 = '|{:<5} | {:^20} | {:>5}|'.format('name','Địa chỉ','Sđt')
r6 = '+{:=<5} + {:=^20} + {:=>5}+'.format('','','')
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)


a = 'pham thanh bang'
b = a.find ('p')
print(a)
print(b)


'Trinh Thang bang'.replace('trinh thang', 'Pham Thanh').title()


