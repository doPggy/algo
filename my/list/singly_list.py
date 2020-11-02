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
        return None, None

    def find_node_and_pre_by_index(self, index):
        if index == 0 or index > self.len:
            print("not find_node_and_pre_by_index")
            return None, None
        q   = self.head
        pre = self.head
        cur = 0
        # 到下一个节点
        while cur < index:
            pre = q
            q   = q.next
            cur += 1
        return q, pre

    # 后插
    def back_insert(self, data, index):
        target, _ = self.find_node_and_pre_by_index(index)
        if not target:
            return
        new_node        = Node(data)
        new_node.next   = target.next
        target.next     = new_node
        self.len        += 1
    # 前插
    def forward_insert(self, data, index):
        target, pre = self.find_node_and_pre_by_index(index)
        if not target:
            print("not")
            return
        new_node        = Node(data)
        new_node.next   = target
        pre.next        = new_node
        self.len        += 1
    
    # 头插法
    def head_insert(self, data):
        new_node        = Node(data)
        new_node.next   = self.head.next   
        self.head.next  = new_node
        self.len        += 1
    
    # 尾插法
    def tail_insert(self):
        pass

    def delete_node(self, data, index):
        target, pre = self.find_node_and_pre_by_index(index)
        if not target:
            return
        pre.next    = target.next
        target.next = None
        target.data = None
        self.len    -= 1

    def __repr__(self):
        t = []
        q = self.head.next
        while q:
            t.append(str(q.data))
            q = q.next
        return '->'.join(t)
            

if __name__ == "__main__":
    sl = SList()
    sl.head_insert(1)
    sl.head_insert(2)
    sl.head_insert(3)
    sl.head_insert(4)
    print(sl)

    sl.forward_insert(1111, 0)
    print(sl)
    sl.forward_insert(1111, 1)
    print(sl)
    sl.back_insert(1112, 2)
    print(sl)