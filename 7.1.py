# -*- coding:utf-8 -*-
'''
用两个队列来实现一个栈，完成栈的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, node):
        self.queue1.append(node)
    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return
        if len(self.queue1) == 0:
            return self.queue2.pop()
        else:
            while len(self.queue1):
                x = self.queue1.pop()
                self.queue2.append(x)
            return self.queue2.pop()
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