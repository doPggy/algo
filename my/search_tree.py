#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 树节点
class TNode():
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

# 任意节点的左子树比
class BSearchTree():
    def __init__(self, value):
        self.root = TNode(value)
    
    def insert(self, value):
        t_ptr         = self.root
        t_parent_ptr  = self.root
        while t_ptr:
            t_parent_ptr = t_ptr
            if t_ptr.value <= value:
                t_ptr = t_ptr.right
            else:
                t_ptr = t_ptr.left
        if value < t_parent_ptr.value:
            t_parent_ptr.left = TNode(value)
        else:
            t_parent_ptr.right = TNode(value)

    """
    搜索
    返回 bst 中所有值为data的节点列表
    因为大于等于的值都会放在右子树，可能不止一个节点
    :param data:
    :return:
    """
    def search(self, value):    
        ret           = []
        t_ptr         = self.root
        while t_ptr:
            # t_parent_ptr = t_ptr
            if t_ptr.value == value:
                ret.append(t_ptr)
            # 遍历
            if t_ptr.value < value:
                t_ptr = t_ptr.right
            else:
                t_ptr = t_ptr.left
        return ret


    def del_(self, value):

if __name__ == "__main__":
    root       = Node(0)
    t_1        = Node(1)
    t_2        = Node(2)
    t_2_1      = Node(3)
    t_2_2      = Node(4)
    t_3        = Node(5)
    t_3_1      = Node(6)
    t_3_2      = Node(7)

    root.left       = t_1 # 1
    root.right      = t_2 # 2 
    t_2.left        = t_2_1 # 3
    t_2.right       = t_2_2 # 4
    t_2_2.left      = t_3 # 5
    t_3.left        = t_3_1 #6
    t_3.right       = t_3_2 # 7

    # list 会触发生成器的 next
    print(list(pre_tra(root)))
    print(list(in_tra(root)))
    print(list(post_tra(root)))