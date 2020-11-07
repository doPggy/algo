'''
leet code: 146
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
    它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
        当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间

哈希表+双向链表
哈希表: 查询 O(1)
双向链表: 有序, 增删操作 O(1)
'''
class Node():
    def __init__(self, key = None, val = None):
        self.key  = key
        self.val  = val
        self.pre  = None
        self.next = None

# 1. 查询已有缓存，说明最近用过，要放到链表首部，表示最近最频繁使用
# 2. 查询未有缓存，返回 -1
# 3. 插入新缓存，未超过上限，插入头部
# 4. 插入新缓存，超过上限，插入头部，将尾部缓存删除
class LRUCache():
    def __init__(self, capacity:int):
        self.capacity  = capacity
        self.head      = Node()
        self.tail      = self.head
        self.key_2_node = {}
        self.len       = 0
    
    def back_insert_by_node(self, node, new_node):
        if not node or not new_node:
            return
        new_node.pre      = node
        new_node.next     = node.next
        node.next         = new_node
        self.len          += 1
        # 用于尾指针
        if self.tail == self.head or node == self.tail:
            self.tail = new_node
        else:
            new_node.next.pre = new_node
    
    def delete_node_by_node(self, node):
        if not node:
            return
        node.pre.next = node.next
        # 这里就很不好
        if node == self.tail:
            self.tail = node.pre
        else:
            node.next.pre = node.pre
        self.len      -= 1
        return node


    def put(self, key, val):
        ptr = self.key_2_node.get(key)
        # 更新缓存，且放到最开头
        if ptr:
            self.delete_node_by_node(ptr)
            ptr.val = val
            self.back_insert_by_node(self.head, ptr)
        # 新增，若超过上限要去掉尾结点
        else:
            new_node             = Node(key, val)
            self.key_2_node[key] = new_node
            self.back_insert_by_node(self.head, new_node)
            # print(self)
            if self.len > self.capacity:
                # print('tailval is {}'.format(self.tail.val))
                # print('tailval pre is {}'.format(self.tail.pre.val))
                self.key_2_node.pop(self.tail.key)
                self.delete_node_by_node(self.tail)
                # print('tailval is {}'.format(self.tail.val))



    def get(self, key):
        node = self.key_2_node.get(key)
        if not node:
            return -1
        self.delete_node_by_node(node)
        self.back_insert_by_node(self.head, node)
        return node.val
    
    def __repr__(self):
        q = self.head
        t = []
        while q.next:
            q = q.next
            t.append(str(q.val))
        return '<->'.join(t)

if __name__ == "__main__":
    lru = LRUCache(2)    
    print(lru)
    print(lru.get(1))
    lru.put(1, 1)
    print(lru)
    lru.put(2, 2)
    print(lru)
    lru.put(3, 3)
    print(lru)

    print(lru.get(2))
    print(lru)