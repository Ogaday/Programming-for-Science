#find the radius of a circle which passes through the vertices of a triangle with edges of length a, b, c
#diamater of the circle is given by d = (abc) / (2(s(s-a)(s-b)(s-c))**0.5)
#s is the semiperimeter and is defined by s= (a + b + c)/2

#set variables
a = 3.0
b = 4.0
c = 6.0

#fine semiperimeter
s = (a + b + c)/2.0

#find diamter
d = (a*b*c)/(2.0*(s*(s-a)*(s-b)*(s-c))**0.5)

#find radius: r
r = d/2

#present result
print 'the radius of the circle which passes through the vertices of the triangle with sides', 'a=', a, 'b=', b, 'c=', c, 'is', r