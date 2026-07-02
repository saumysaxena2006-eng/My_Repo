class Queue:
    def __init__(self):
        self.rear = -1
        self.front = -1
        self.list = []

    def enqueue(self, number):
        if len(self.list) < 50:
            print(f"{number} is enqueued")
            self.list.append(number)
            self.rear += 1
        else:
            raise Exception("Queue Overflow")

    def dequeue(self):
        if len(self.list) >= 1:
            self.front += 1
            print(f"{self.list[self.front]} got dequeued")
            self.list.pop(0)
        else:
            raise Exception("Queue Underflow")

    def display(self):
        if len(self.list) >= 1:
            print("Elements in the queue are:")
            for i in self.list[::-1]:
                print(i, end=", ")
            print("\n")
        else:
            raise Exception("Queue Underflow")

    def front_element(self):
        if self.front > -1:
            print(self.list[self.front])
        else:
            print("Queue Underflow")

    def rear_element(self):
        if self.rear > -1:
            print(self.list[self.rear])
        else:
            print("Queue Underflow")


q = Queue()
print("1-> Enqueue\n2-> Dequeue\n3-> Display\n4-> Front\n5-> Rear\n6-> Exit")
choice = int(input("Enter your choice:"))
while True:
    match choice:
        case 1:
            x = int(input("Enter the number to be enqueued:"))
            q.enqueue(x)
            continue
        case 2:
            q.dequeue()
            continue
        case 3:
            q.display()
            continue
        case 4:
            q.front_element()
            continue
        case 5:
            q.rear_element()
            continue
        case _:
            break
