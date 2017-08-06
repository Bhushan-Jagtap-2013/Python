class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
        print "None"

    def addAtFront(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def addAfter(self, data, new_data):
        temp = self.head
        while (temp != None and temp.data != data):
            temp = temp.next
        if temp == Node :
            return

        node = Node(new_data)
        node.next = temp.next
        temp.next = node

    def addAtEnd(self, data):
        if self.head == None :
            self.head = Node(data)
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def removeFront(self):
        if (self.head == None):
            return
        self.head = self.head.next

    def removeElement(self, data):
        prev = None
        temp = self.head
        while(temp != None):
            if temp.data == data:
                if prev == None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return
            prev = temp
            temp = temp.next

if __name__ == "__main__":
    print "\nadd at front"
    sll = SinglyLinkList()
    sll.addAtFront(10)
    sll.addAtFront(20)
    sll.addAtFront(30)
    sll.addAfter(30, 40)
    sll.printList()

    print "\nadd at end"
    sll = SinglyLinkList()
    sll.addAtEnd(10)
    sll.addAtEnd(20)
    sll.addAtEnd(30)
    sll.printList()

    print "\nDeletion"
    sll.printList()
    sll.removeFront()
    sll.printList()
    sll.removeElement(20)
    sll.printList()
    sll.removeElement(30)
    sll.printList()
    sll.removeElement(40)
    sll.printList()
