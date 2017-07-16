# -*- coding:utf-8 -*-
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
        return self.stack1
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        if len(self.stack1) == 0:
            del self.stack2[len(self.stack2) - 1]
        else:
            m = len(self.stack1)
            while len(self.stack1):
                x = self.stack1.pop(m-1)
                m = m-1
                self.stack2.append(x)
            del self.stack2[len(self.stack2) - 1]
            return self.stack2
P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())
