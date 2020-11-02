# 先实现一个双向链表好了
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.pre  = None

class List():
    def __init__(self):
        self.head = Node()
        self.len  = 0
    
    # def 