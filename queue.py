a = []
#n = int(input("Enter number of elements"))

def enqueue():
    #for i in range(0,n):
    I = input("Enter element: ")
    a.append(I)

def dequeue():
    if not a:
        print("Can not dequeue from an empty list")
    else:
        a.pop()

def display():
    print(a)


#b = int(input("Select action: 1 -> Enqueue, 2 -> Dequeue, 3 -> Display, 4 -> Quit"))

while True:
    b = int(input("Select action: 1 -> Enqueue, 2 -> Dequeue, 3 -> Display, 4 -> Quit"))
    if b == 1:
        enqueue()
        print("The queue is: ", a)

    elif b == 2:
        if a.pop():
            print("Queue is", a)

    elif b == 3:
        print(a)
    
    elif b == 4:
        print("Thank you")
        break
    else:
        print("Enter correct input")




