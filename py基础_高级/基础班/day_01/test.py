''
'''
        小技巧
        通过yield 只能向下取值  来取出无限层的列表并生成可迭代对象
                                    列表中的列表嵌套次数来决定递归的次数
                上方代码有个bug 如果碰到字符串 会把字符拆开  不ok
'''


def list_str_yield(lst):
    for i in lst:
        try:
            try:
                i + ''
            except:
                pass
            else:
                raise Exception
            for d in list_str_yield(i):
                yield d
        except:
            yield i


c = [1, 2, 123, 1, [123, 4, 51, [123, 'abc', 3, [1, 7], 45, 35, ], 1235, 123, [1234, ], 123]]
a = list_yield(c)
print(list(a))
