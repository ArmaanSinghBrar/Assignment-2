a = "Python is a case sensitive language"

#Question 1 (a)
b = len(a)
print(b)

#Question 1 (b)
c = a[::-1]
print(c)

#Question 1 (c)
d = a[slice(10,26)]
print(d)

#Question 1 (d)
e = a.replace("a case sensitive", "object oriented")
print(e)

#Question 1 (e)
f = a.index('a')      #we can also use the function a.find('a') for index of a in sentence
print(f)

#Question 1 (f)
g = a.replace(" ","")
print(g)
