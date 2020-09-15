#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 树节点
class Node():
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

# 前序遍历
def pre_tra(root):
    if root:
        yield root.value
        yield from pre_tra(root.left)
        yield from pre_tra(root.right)

# 中序遍历
def in_tra(root):
    if root:
        yield from in_tra(root.left)
        yield root.value
        yield from in_tra(root.right)

# 非递归莫里斯
# 遍历空间复杂度是 O(1) ,但是为了方便查看用了一个 list。
def in_tra_morris(root):
    r = []
    while root:
        if not root.left:
            r.append(root.value)
            root = root.right
        else:
            tmp = root.left
            while tmp.right and tmp.right != root:
                tmp = tmp.right
            # 说明左子树已经遍历完成
            if tmp.right == root:
                tmp.right = None
                r.append(root.value)
                root = root.right
            else:
                tmp.right = root
                root = root.left
    return r

# 层序遍历
#! 利用一个队列，弹出第一个节点，并将其子节点入队
def level_tra(root):
    ret   = []
    queue = [ root, ]
    while len(queue) != 0:
        ptr = queue.pop(0)
        if ptr.left:
            queue.append(ptr.left)
        if ptr.right:
            queue.append(ptr.right)
        ret.append(ptr.value)
    return ret

# 后序遍历
def post_tra(root):
    if root:
        yield from post_tra(root.left)
        yield from post_tra(root.right)
        yield root.value

def fetch_height(root):
    if not root:
        return 0
    return max(fetch_height(root.left), fetch_height(root.right)) + 1

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

    print(level_tra(root))
    print(fetch_height(root))


    print(in_tra_morris(root))