# Biến (variable)
a = 28021996
b = 28022020
c = a + b
print(c)
print(type(a))

#float --> là số thực
# vd_float = 1.123456789101112131415

#lấy toàn bộ nội dung của thư viện decimal
from decimal import*

# lấy tối đa 30 chữ số phần nguyên và phần thập phần Decimal
getcontext().prec = 30

print(Decimal(10)/Decimal(3))

#phân số
from fractions import*
frac1  = Fraction(6,9)
frac2  = Fraction(5,10)
frac3  = frac1 + frac2
print(frac3)

#số phức (Complex): gốm phần thực và phần ảo
comp = complex(2,5)
print(comp.real)
print(comp.imag)





