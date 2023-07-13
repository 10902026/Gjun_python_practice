class StackNode():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedStack():
    def __init__(self):
        self.top = None

    def push(self,value):
        if self == None:
            new = StackNode(value)
        else :
            new = StackNode(value)
            new.next = self.top
            self.top = new

    def printstack(self):
        pointer = self.top
        while (pointer != None):
            print(pointer.value)
            pointer = pointer.next

if __name__ == '__main__':
    one = LinkedStack()
    one.push(1)
    one.push(4)
    one.push(9)
    one.push(10)
    one.printstack()
