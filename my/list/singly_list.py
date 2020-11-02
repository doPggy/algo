# 先实现一个单向链表好了
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SList():
    def __init__(self):
        self.head = Node()
        self.len  = 0
    
    def find_node_and_pre_by_value(self, data):
        q   = self.head
        pre = self.head
        while q:
            if q.data == data:
                return q, pre
            else:
                pre = q
                q   = q.next

    def find_node_and_pre_by_index(self, index):
        if index > self.len:
            return
        q   = self.head
        pre = self.head
        while q:
            if q.data == data:
                return q, pre
            else:
                pre = q
                q   = q.next
    # 后插
    def back_insert(self, data, index):
        target, pre = self.find_by_index(index)
        if not target:
            return
        new_node        = Node(data)
        new_node.next   = target.next
        target.next     = new_node
    # 前插
    def forward_insert(self, data, index):
        target, pre = self.find_by_index(index)
        if not target:
            return
        new_node        = Node(data)
        new_node.next   = target
        target.next     = new_node
    
    # 头插法
    def head_insert(self, data):
        new_node        = Node(data)
        new_node.next   = self.head.next   
        self.head.next  = new_node
    
    # 尾插法
    def tail_insert():
        pass

    def delete_node(self, data, index):
        target, pre = self.find_by_index(index)
        if not target:
            return
        pre.next    = target.next
        target.next = None
        target.data = None

if __name__ == 'main':
    pass
