class ListNode:
    # initiatlize listnode class
    # assume next node is not in parameters, set to none 
    # by default
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    # initialize new linked list with dummy node at head
    # allowing removal from head easier
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

# -1 4, 5, 6, 7, -1
#    ^
# self.head.next = first number after dummy
    def insertHead(self, val: int) -> None:
        # create node for new val
        new_node = ListNode(val)
        # connect new node to first node
        new_node.next = self.head.next
        # connect dummy head node to new node
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

# note: there is NO dummy node at the TAIL
# therefore: replace tail by adding node next to it
# then move tail to that new node 
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # traverse thru list to node BEFORE target node
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        
        # if prev node and TARGET node exist:
        if curr and curr.next:
            # check if TARGET node is tail node
            if curr.next == self.tail:
                # MOVE TAIL MARKER BACK TO PREV NODE
                self.tail = curr
            # connect TARGET node to whatevers next to it
            # performs soft delete
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res