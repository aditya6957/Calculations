def power(a,b): 
     res = 1 
     for i in range(b): 
         res *= a 
     return res

x=int(input("x"))
y=int(input("y"))
print(power(x,y))
 