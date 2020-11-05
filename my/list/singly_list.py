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

    def delete_node(self, index):
        target, pre = self.find_node_and_pre_by_index(index)
        if not target:
            return
        pre.next    = target.next
        target.next = None
        target.data = None
        self.len    -= 1
    
    def reversed_self(self):
        # 考虑空链表情况
        if not self.head or not self.head.next:
            return
        q   = self.head.next
        pre = self.head
        while q:
            _next = q.next
            q.next = pre
            pre    = q
            q      = _next
        # head 还指向头结点
        self.head.next.next = None
        self.head.next      = pre


    def __repr__(self):
        t = []
        # q = self.head.next
        # while q:
        #     t.append(str(q.data))
        #     q = q.next
        q = self.head
        while q.next:
            q = q.next
            t.append(str(q.data))
        return '->'.join(t)

    # 利用快慢指针，快指针一次走两步
    def has_ring(self):
        # 空链表情况
        fast = self.head
        slow = self.head
        # fast.next 要保证不为 None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def back_insert_by_node(self, node, new_node):
        new_node.next = node.next
        node.next     = new_node


    # 升序:w
    def ascend_order_insert(self, data):
        if not self.head.next:
            return self.back_insert_by_node(self.head, Node(data))
        q   = self.head
        pre = self.head
        while q.next:
            pre = q
            q   = q.next
            if data < q.data:
                return self.back_insert_by_node(pre, Node(data))
        # 尾插 注意是 q 之后插入
        return self.back_insert_by_node(q, Node(data))
        

    def order_list_merge(l1 = None, l2 = None):
        if not l1 or not l2:
            return l1 or l2
        q1        = l1.head.next
        q2        = l2.head.next
        q_new     = SList()
        q_new_ptr = q_new.head
        # 不构造完全的新链表, 不用新节点，用已有节点合并
        while q1 and q2:
            if q1.data < q2.data:
                q_new_ptr.next = q1
                q1 = q1.next
            else:
                q_new_ptr.next = q2
                q2 = q2.next
            q_new_ptr = q_new_ptr.next
        q_new_ptr.next = q1 if q1 else q2
        return q_new
    

def test_head_insert():
    sl = SList()
    sl.head_insert(1)
    sl.head_insert(2)
    sl.head_insert(3)
    sl.head_insert(4)
    print(sl)

def test_forward_insert():
    sl = SList()
    # 空链表情况
    sl.forward_insert(1, 0)
    # sl.head_insert(3)
    # sl.head_insert(4)
    print(sl)
    sl.head_insert(1)
    print(sl)
    sl.forward_insert(2, 1)
    print(sl)

def test_reversed_self():
    # 空链表情况
    sl1 = SList()
    print(sl1)
    sl1.reversed_self()
    print(sl1)
    # 一个节点
    sl1.head_insert(1)
    print(sl1)
    sl1.reversed_self()
    print(sl1)
    # 两个节点
    sl1.head_insert(2)
    print(sl1)
    sl1.reversed_self()
    print(sl1)

def test_has_ring():
    sl = SList()
    # 空链表
    print(sl.has_ring())

    # 一个节点
    sl.head_insert(11)
    print(sl.has_ring())
    # 两个节点
    sl.head_insert(21)
    print(sl.has_ring())


def test_merge():
    sl1 = SList()
    sl1.ascend_order_insert(4)
    sl1.ascend_order_insert(3)
    sl1.ascend_order_insert(5)
    print(sl1)

    sl2 = SList()
    sl2.ascend_order_insert(8)
    sl2.ascend_order_insert(18)
    sl2.ascend_order_insert(1)
    print(sl2)
    print(SList.order_list_merge(sl1, sl2))

if __name__ == "__main__":
    print('test_head_insert-------------')
    test_head_insert()
    print('test_forward_insert-------------')
    test_forward_insert()
    print('test_reversed_self-------------')
    test_reversed_self()
    print('test_has_ring-------------')
    test_has_ring()
    print('test_merge-------------')
    test_merge()
    # sl = SList()
    # sl.head_insert(1)
    # sl.head_insert(2)
    # sl.head_insert(3)
    # sl.head_insert(4)
    # print(sl)

    # sl.forward_insert(1111, 0)
    # print(sl)
    # sl.forward_insert(1111, 1)
    # print(sl)
    # sl.back_insert(1112, 2)
    # print(sl)


    # sl.reversed_self()
    # print(sl)
