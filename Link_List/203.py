# https://leetcode.com/problems/remove-linked-list-elements/description/
# remove all ocurence of given element in LL

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class SLL:
    def __init__(self):
        self.head = None

    def printSLL(self):
        temp = self.head
        while(temp != None):
            print temp.data
            temp = temp.next

    def insertInFront(self, data):
        n = Node(data);
        if self.head == None:
            self.head = n
            return
        n.next = self.head
        self.head = n

    def removeElementDummy(self, data):
        temp = Node(0)
        temp.next = self.head
        n = temp
        while n.next != None:
            if n.next.data == data:
                n.next = n.next.next
            else:
                n = n.next
        self.head = temp.next

    def removeElement(self, data):
        while self.head != None and self.head.data == data:
            self.head = self.head.next

        if self.head == None:
            return

        temp = self.head
        while temp.next != None:
            if temp.next.data == data:
                temp.next = temp.next.next
            else:
                temp = temp.next

if __name__ == "__main__":
    s = SLL()
    s.insertInFront(10)
    s.insertInFront(10)
    s.insertInFront(10)
    s.insertInFront(10)
    s.insertInFront(10)
    s.insertInFront(10)
    s.insertInFront(20)
    s.insertInFront(20)
    s.insertInFront(20)
    s.insertInFront(20)
    s.insertInFront(20)
    s.insertInFront(20)
    s.insertInFront(30)
    print "ORIGINAL:"
    s.printSLL()
    print "remove 10"
    s.removeElement(10)
    s.printSLL()
    print "remove 20"
    s.removeElement(20)
    s.printSLL()
