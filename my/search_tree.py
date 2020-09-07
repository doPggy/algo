#!/usr/bin/python
# -*- coding: UTF-8 -*-

from queue import Queue
# 树节点
class TNode():
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.parent = None

# 任意节点的左子树比
class BSearchTree():
    def __init__(self, val_list = []):
        # self.root = TNode(value)
        self.root = None
        for val in val_list:
            self.insert(val)
    
    def insert(self, value):
        # 无根节点
        if not self.root:
            self.root = TNode(value)
            return
        # 有根节点
        t_ptr         = self.root
        t_parent_ptr  = self.root
        while t_ptr:
            t_parent_ptr = t_ptr
            if t_ptr.value <= value:
                t_ptr = t_ptr.right
            else:
                t_ptr = t_ptr.left
        new_node        = TNode(value)
        new_node.parent = t_parent_ptr
        if value < t_parent_ptr.value:
            t_parent_ptr.left = new_node
        else:
            t_parent_ptr.right = new_node

    """
    搜索
    返回 bst 中所有值为data的节点列表
    因为大于等于的值都会放在右子树，可能不止一个节点
    :param data:
    :return:
    """
    def search(self, value):    
        if not self.root:
            return
        ret           = []
        t_ptr         = self.root
        while t_ptr:
            # t_parent_ptr = t_ptr
            if t_ptr.value == value:
                ret.append(t_ptr)
            # 遍历
            if t_ptr.value <= value:
                t_ptr = t_ptr.right
            else:
                t_ptr = t_ptr.left
        return ret
    
    # 不应该只删除一个节点，删除节点可能是有多个的
    def delete(self, value):
        need_del_ptrs = self.search(value)
        for ptr in need_del_ptrs:
            self._delete(ptr)

    def _delete(self, node):
        min_ptr   = node
        # 有两个子节点
        if min_ptr.left and min_ptr.right:
            min_ptr = min_ptr.right
            while min_ptr.left:
                min_ptr = min_ptr.left
            node.value = min_ptr.value
        # 一个子节点或者没有子节点
        need_remain = min_ptr.left or min_ptr.right
        parent      = min_ptr.parent
        # 直接要删除只有一个子节点的根节点
        if not parent:
            self.root = need_remain
        else:
            if need_remain:
                need_remain.parent = parent
            if parent.left == node:
                parent.left = need_remain
            elif parent.right == node:
                parent.right = need_remain
            




    # def delete(self, value):
    #     # 3 种情况，一种解决对策
    #     t_ptr   = self.root
    #     p_t_ptr = None
    #     while t_ptr:
    #         if t_ptr.value == value:
    #             break
    #         p_t_ptr = t_ptr
    #         if value < t_ptr.value:
    #             t_ptr = t_ptr.left
    #         else:
    #             t_ptr = t_ptr.right
    #     #! 没有找到
    #     if not t_ptr:
    #         return
    #     # 已经找到
    #     # 两个子节点，找替代, 最接近自己的数，所以是右子树的最小值或者左子树的最大值
    #     min_p_ptr = None
    #     min_ptr   = None
    #     if t_ptr.left and t_ptr.right:
    #         min_ptr     = t_ptr.right
    #         min_p_ptr   = t_ptr.right
    #         while min_ptr.left:
    #             min_p_ptr = min_ptr
    #             min_ptr   = min_ptr.left
    #         # 右子树最小节点，替换要删除节点
    #         t_ptr.value = min_p_ptr.value
    #         # 这样方便后头删除一个节点的情况
    #         t_ptr       = min_ptr
    #         p_t_ptr     = min_p_ptr

    #     # 开始处理只有一个子节点的情况
    #     need_del    = t_ptr
    #     # 需要删除的节点的子节点 可能为 None，这样直接包括了删除没有子节点的节点，这类情况
    #     need_remain = t_ptr.left or t_ptr.right
    #     if not p_t_ptr: # 删除的是根节点 能走到这，说明这个树本来就只有两个节点，且要删除根节点
    #         self.root = need_remain
    #     elif t_ptr == p_t_ptr.left:
    #         p_t_ptr.left = need_remain
    #     elif t_ptr == p_t_ptr.right:
    #         p_t_ptr.right = need_remain

    # 中序遍历就是有序序列
    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, ptr):
        if not ptr:
            return []
        ret = []
        ret.extend(self._in_order(ptr.left))
        ret.append(ptr.value)
        ret.extend(self._in_order(ptr.right))
        return ret
    
    def __repr__(self):
        # return (str(self.in_order()))
        return self._draw_tree()

    def fetch_height(self):
        return self._fetch_height(self.root)

    def _fetch_height(self, node):
        if not node:
            return 0
        return max(self._fetch_height(node.left), self._fetch_height(node.right)) + 1

    def _draw_tree(self):
        # self.root = 
        queue = [ self.root ]
        _draw = ""
        p     = None
        while len(queue) > 0:
            p     = queue.pop()
            _draw += str(p.value) + '\t'
            _draw += '\n'
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return _draw
    
    def bfs(self):
        return self._bfs(self.root)
    # 广度优先遍历
    # 层序遍历
    def _bfs(self, node):


if __name__ == "__main__":
    nums = [4, 6, 5, 4, 1, 7, 3]
    '''
          4
      1       6
        3   5     7 
         4
    '''
    bst  = BSearchTree(nums)
    print(bst)

    print(bst.fetch_height())
    print(bst.in_order())

    # bst.insert(8)
    # # bst.insert(4)
    # print(bst)

    # bst.delete(4)
    # print(bst)

    # bst._draw_tree()
