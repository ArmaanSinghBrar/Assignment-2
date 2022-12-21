a = 56
b = 10

#Question 3 (a)
c = a&b                #& operator acts as an AND gate
print("a&b =",c)

#Question 3 (b)
d = a|b                #| operator acts as an OR gate
print("a|b =",d)

#Question 3 (c)
e = a^b                #^ operator acts as an XOR gate
print("a^b =",e)

#Question 3 (d)
f = a<<2               # << shifts the bits to the left
g = b<<2
print("Shifting a left by 2 bits =", f , "\nSifting b left by 2 bits =",g)

#Question 3 (e)
h = a>>2               # >> shifts the bits to the right
i = b>>4
print("Shifting a right by 2 bits =",h,"\nShifting b right by 4 bits =",i)
