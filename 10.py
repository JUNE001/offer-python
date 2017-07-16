# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff #n为负数时，使用补码表示，做加减运算不对，所以与全1相与？？？？不懂！！！！
        while n:
            count += 1
            n = (n-1) & n
        return count
Test = Solution()
print(Test.NumberOf1(-15))