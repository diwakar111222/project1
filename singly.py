class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        temp = Node(data)
        if self.first is None:
            self.first = temp
        else:
            temp.next = self.first
            self.first = temp

    def removeFirst(self):
        if self.first is None:
            print("List is empty")
            return
        cur = self.first
        self.first = self.first.next
        print("The deleted item is", cur.data)

    def display(self):
        if self.first is None:
            print("List is empty")
            return
        current = self.first
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def search(self, item):
        if self.first is None:
            print("List is empty")
            return
        current = self.first
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        if found:
            print("Item is present in linked list")
        else:
            print("Item is not present in the linked list")

# Singly Linked List
sll = SinglyLinkedList()
while True:
    c1 = int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit: "))
    if c1 == 1:
        item = input("Enter the element to insert: ")
        sll.insertFirst(item)
        sll.display()
    elif c1 == 2:
        sll.removeFirst()
        sll.display()
    elif c1 == 3:
        item = input("Enter the element to search: ")
        sll.search(item)
    elif c1 == 4:
        sll.display()
    elif c1 == 5:
        break
