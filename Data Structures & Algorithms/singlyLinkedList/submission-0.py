class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr != None:
            return curr.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index):
            curr = curr.next
        if curr == None or curr.next == None:
            return False
        node_to_remove = curr.next
        curr.next = node_to_remove.next
        if node_to_remove == self.tail:
            self.tail = curr
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
