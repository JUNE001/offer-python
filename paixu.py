# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array[0]) - 1
        n = 0
        flag = 0
        while m >= 0 and n < len(array):
            if target == array[n][m]:
                return True
            elif target < array[n][m]:
                m -= 1
                flag = 1
            else:
                n += 1
                flag = 1
        if flag == 1:
            return False