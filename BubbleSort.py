from this import d


a = []
n = int(input("Enter number of elements"))
for i in range (0,n):
    I = int(input())
    a.append(I)
print("Unsorted Array is", a)

for i in range (n-1):
    for j in range (0, n-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


for i in range (n):
    ()      
print("Sorted Array is", a)

