class Stack:
    def __init__(self):
        self.list = []

    def push(self, number):
        if len(self.list) < 50:
            print(f"{number} is pushed into the stack")
            self.list.append(number)
        else:
            raise Exception("Stack Overflow")

    def pop(self):
        if len(self.list) > 1:
            print(f"{self.list[-1]} got popped from the stack")
            self.list.pop()
        else:
            raise Exception("Stack Underflow")

    def display(self):
        if len(self.list) >= 1:
            print("Elements in the stack are:")
            for i in self.list[::-1]:
                print(i, end=", ")
            print("\n")
        else:
            raise Exception("Stack Underflow")

    def peek(self):
        if len(self.list) > 1:
            print(f"The peek value of stack is {self.list[-1]}")
        else:
            raise Exception("Stack Underflow")


s = Stack()
print("1-> Push\n2-> Pop\n3-> Display\n4-> Peek\n5-> Exit")
choice = int(input("Enter your choice:"))
while True:
    match choice:
        case 1:
            x = int(input("Enter the data to be pushed"))
            s.push(x)
            continue
        case 2:
            s.pop()
            continue
        case 3:
            s.display()
            continue
        case 4:
            s.peek()
            continue
        case _:
            break
