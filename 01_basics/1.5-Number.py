# In python number are -->> integer, float, complex number, set, decimal number,fraction, boolean
# operater are +, -, *, /, //, **->power

print(40+23.2)  # it works but not good practice
print(float(40) + 23.2)

print('moni'+ 'chaurasiya')

x=2
y=4
z=6
print(x,y,z) # tuple -> if we try to print multiple value together
print(x+y,x*z)

print(2**100)
print(2**1000)  # In python even this can be calculated

result= 1/3.0
print(result)

print(repr('moni'))
print(str('moni'))
print('chai')
print(1<2)
print(5.0 == 5.0)
print(4.0 != 5.0)
print(x<y<z),   print(x<y and y<z)
print(1==2 and 2<3), print(1==2<3)  # false

import math
# floor will always print lower value 
print(math.floor(4.5))  # 4 
print(math.floor(-4.5))  # -5

# trunc will go towards zero
print(math.trunc(2.6)) # 2
print(math.trunc(-2.6)) # 2

print(9999999999999999999999 + 1) 
print(999999999999999 * 2.1)

print(2+3j)  # imaginary number
print((2+1j)*5)   # (10+5j)


print(0o20) # octal
print(0xff)  # hexadecimal
print(0b10001) # binary

print(oct(64))
print(hex(64))
print(bin(64))

# other way to calculate
print(int('64',8)) #octal
print(int('64',16)) #binary
print(int('10000',2)) # hexadecimal

print(x<<2)  # left sift -> 8 for when x is 2
print(x | 2)

import random
# In python we can get random value between any integer
li=[1,2,3,4,5,6,7]
print(random.randint(1,100))
print(random.choice(li))
random.shuffle(li)
print(li)

print(1.1 + 2.4 + 3.7-0.5)

from decimal import Decimal
print(Decimal('0.1')+Decimal('4.7'))

from fractions import Fraction
print(Fraction(2,7))

setone={1,3,4,5}
settwo={1,2,5,7}

print(setone & settwo)  # intersection
print(setone | settwo)  # union

print(setone-{1,3,4,5})  # it will print set() instead of {} -> empty
print(type({}))

print(True is 1)  # false
print(True + 5) # 6
