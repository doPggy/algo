# 先实现一个双向链表好了
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre  = None