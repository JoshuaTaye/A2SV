# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key=-1,value=-1, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.val = value
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail 
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.pointers:
            node = self.pointers[key]
            self.remove(node)
            self.insertAtTail(node)
            return node.val
        return -1



    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            new_node = self.pointers[key]
            new_node.val = value
            self.remove(new_node)
        else:
            new_node = ListNode(key, value)
            if len(self.pointers) == self.capacity:
                tbr = self.head.next
                self.remove(tbr)
        self.insertAtTail(new_node) 

    def remove(self, node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        key = node.key
        self.pointers.pop(key)

    def insertAtTail(self, node) -> None:
        key = node.key
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        self.pointers[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)