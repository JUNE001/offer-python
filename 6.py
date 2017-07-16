# -*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if not pre:
			return None
		else:
			node = TreeNode(pre[0])

		def handle(node, pre, tin):
			pos = tin.index(pre.pop(0))
			if pos > 0:
				node.left = TreeNode(pre[0])
				handle(node.left, pre[:pos], tin[:pos])
			if pos < len(tin) - 1:
				node.right = TreeNode(pre[pos])
				handle(node.right, pre[pos:], tin[pos + 1:])
			return

		handle(node, pre, tin)
		return node
pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
tree_new = test.reConstructBinaryTree(pre,tin)
print(tree_new.val)


