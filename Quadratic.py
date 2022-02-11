print("Your equation has to be in the format of ax2 + bx + c = 0")
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("enter the value of c"))

d1 = ((b**2)- 4*a*c)
d = (((b**2)-4*a*c)**0.5)

if d1<0:
    print("Roots are imaginary")

if d1==0:
    print("Roots are equal")
    print((-b)/(2*a))
else:
    X1 = (((-b) + d)/2*a)
    X2 = (((-b) - d)/2*a)
print("The roots of equation are", X1, "and", X2)

