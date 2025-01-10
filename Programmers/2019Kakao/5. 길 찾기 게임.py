# 길 찾기 게임
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀

class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self, idx, x, y):
        if self.root is None:
            self.root = Node(idx, x, y)
            return

        self.cur = self.root
        while True:
            if x < self.cur.x:
                if self.cur.left:
                    self.cur = self.cur.left
                else:
                    self.cur.left = Node(idx, x, y)
                    break
            else:
                if self.cur.right:
                    self.cur = self.cur.right
                else:
                    self.cur.right = Node(idx, x, y)
                    break

    def preorder(self, node):
        if not node:
            return
        self.preorder_arr.append(node.idx)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        self.postorder_arr.append(node.idx)


def solution(nodeinfo):
    answer = []
    bst = BST()

    info = [[i + 1, v[0], v[1]] for i, v in enumerate(nodeinfo)]
    info.sort(key=lambda x: x[2], reverse=True)  # y값 기준으로 정렬(그래야 루트에서부터 아래로 내려감)
    for i, x, y in info:
        bst.insert(i, x, y)

    bst.preorder(bst.root)
    bst.postorder(bst.root)
    answer.append(bst.preorder_arr)
    answer.append(bst.postorder_arr)
    return answer
