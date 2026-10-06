class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while (i != index and curr is not self.tail):
            curr = curr.next
            i += 1
        return curr.val if curr is not self.tail else -1
        
        # head <-> [1] <-> [2]
        # insert [1]
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    # [1] -> [2] <-> tail
    # insert [2]
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        temp.next = node
        node.prev = temp  

    def addAtIndex(self, index: int, val: int) -> None:
        # need to know index before
        i = -1
        curr = self.head
        while(i != index-1 and curr is not self.tail):
            curr = curr.next
            i += 1
        if curr is self.tail:
            return None
        else:
            node = Node(val)
            temp = curr.next
            curr.next = node
            node.prev = curr
            node.next = temp
            temp.prev = node
        

    def deleteAtIndex(self, index: int) -> None:
        i = -1
        curr = self.head
        while(i != index-1 and curr is not self.tail):
            curr = curr.next
            i += 1
        if curr is self.tail or curr.next is self.tail:
            return None
        else:
            curr.next = curr.next.next
            curr.next.prev = curr


class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)