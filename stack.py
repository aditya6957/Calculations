class stack(object):

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)
        
    def pop(self, item):
        self.item.pop(item)

    def peak(self):
        if self.item:
            return self.item[-1]
        else:
            return None

    def view(self):
        if self.item:
            return self.item[::]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

if __name__ == "__main__":
    stack = stack()

    stack.push("1")
    stack.push('2')
    print(stack.size())
    print(stack.peak())
    print(stack.view())