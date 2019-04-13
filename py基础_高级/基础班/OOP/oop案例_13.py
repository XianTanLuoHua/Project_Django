''
'''
        定义一个工具类这个工具类的作用就是对传入的数据以定义的方法进行转换字符编码
'''
class code_tools():

    @staticmethod
    def data_encoding(data,code):
        print('{0}使用了{1}编码格式进行了编码'.format(data,code))

    @staticmethod
    def data_decoding(data,code):
        print('{0}使用了{1}编码格式进行了解码'.format(data,code))




if __name__ == '__main__':
    s1 = 'hollo word'
    s2 = '你好世界'

    code_tools.data_encoding(s1,'UTF-8')
    code_tools.data_encoding(s2,"UTF-8")
