# coding=utf-8
#通过计算，返回子串T的next数组

def get_next(T):
    i = 1#后缀
    j = 0#前缀
    a = []
    a.append(0)
    while i < len(T):#T[0]表示T的长度
        print(i)
        if j == 0 or T[i-1] == T[j-1]:
            i += 1
            j += 1
            a.append(j)
        else:
            j = a[j-1]
    return a
T = 'ababaaaba'
next1 = get_next(T)
print(next1)
