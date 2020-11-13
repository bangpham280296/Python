dic = {'name' : 'Howkteam' , 'number' : 69}
print(dic)
print(type(dic))

d = {'Team' : 'Kteam', (1,2):69}
print(d)

d2 = d.copy()
print(d2)

# value = d.get('Team')
value = d.get('hhh', 'olaolaoal')#nếu giá trị k có thì trả ra cái sau
value = d.keys()
print(value)

g = {'name':'bang', 'old':24}
get = g.get('sdt','mothaiba')
print(get)