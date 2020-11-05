# 先实现一个双向链表好了
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.pre  = None

class List():
    def __init__(self):
        self.head = Node()
        # self.tail = self.head
        # self.head.pre = self.head
        self.len  = 0
    
    def find_node_by_index(self, index):
        q   = self.head
        cur = 0
        while q.next and cur != index:
            cur += 1
            q   = q.next
            # print(q.data)
        return q

    def insert_2_head(self, data):
        new_node      = Node(data)
        new_node.next = self.head.next
        new_node.pre  = self.head
        if self.head.next:
            self.head.next.pre = new_node
        self.head.next     = new_node
        self.len           += 1


    def __repr__(self):
        t = []
        q = self.head
        while q.next:
            q = q.next
            t.append(str(q.data))
        return '<->'.join(t)


if __name__ == '__main__':
    l = List()
    l.insert_2_head(1)
    l.insert_2_head(2)
    l.insert_2_head(3)
    l.insert_2_head(4)
    print(l)

