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

class LRUCache():
    def __init__(self, capacity:int):
        self.capacity  = capacity
        self.head      = Node()
        self.tail      = self.head
        self.key_2_val = {}
    
    def back_insert_by_node(self, node, new_node):
        if not node or not new_node:
            return
        new_node.pre  = node
        new_node.next = node.next
    
    def delete_node_by_node(self, node):
        if not node:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        return node


    def put(self, key, val):
        _val = self.key_2_val.get(key)
        q    = self.head
        # 更新缓存，且放到最开头
        if _val:
            while q.next:
                if q.key == key:
                    self.delete_node_by_node(q)
                    self.back_insert_by_node(self.head, q)
                    break
        else:
            pass

        

    def get(self, key):
        val = self.key_2_val.get(key)
        return val if val else -1 