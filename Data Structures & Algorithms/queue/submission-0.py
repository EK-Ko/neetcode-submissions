class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = self.right = None


    def isEmpty(self) -> bool:
        if self.left == None and self.right ==None:
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        newNode = Node(value)

        if self.right:
            self.right.next = newNode
            self.right.next.prev = self.right
            self.right = self.right.next

        else:
            self.right = self.left = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)

        if self.left:
            newNode.next = self.left
            self.left.prev = newNode
            self.left = newNode
        else:
            self.right = self.left = newNode
        

    def pop(self) -> int:
        if not self.right:
            return -1
        
        val = self.right.val
        
        self.right = self.right.prev

        if self.right:
            self.right.next = None
        else:
            self.left = None
        
        return val

        

    def popleft(self) -> int:
        if not self.left:
            return -1

        val = self.left.val
        self.left = self.left.next

        if self.left:
            self.left.prev = None
        else:
            self.right = None

        return val