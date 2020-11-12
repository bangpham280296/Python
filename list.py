# giới hạn bởi cặp ngoặc vuông []
#các phần tử của list đc cách nhau bởi dấu phẩy
#List có khả năng chứa mỗi giá trị đối tượng và chính nó

aa = [i for i in range(30)]
print(aa)

bb = [[n,n*1,n*2] for n in range(1,4)]
print(bb)

a = [1,2,'a','b','c',[3,4]]
a[5] = 'kteam'
b = a[5]
print(b)
print(a)

matran = [[1,2,3],[4,5,6],[7,8,9]]
print(matran[0])
print(matran[1])
print(matran[2])

aaa = [1,2,3,4,7,8,9]
c = aaa.copy()
c[0] = 'team'
print(c)
print(aaa)

d = aaa.sort()
print(d)

