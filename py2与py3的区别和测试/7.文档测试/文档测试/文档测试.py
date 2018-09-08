import doctest
#doctest 模块可以提取注释中的代码执行 >>>后面的代码块
#严格按照交互式格式一致
def mySum(x,y):

    '''
    求两个数的和
    get The Sum from x and y
    :param x: firstNum
    :param y: SecondNum
    :return: sum

    example:
    >>> print(mySum(1,2))
    3

    '''

    return x+y


print(mySum(1,2))


#进行文档测试
doctest.testmod()


