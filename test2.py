"""
 * Project name(项目名称)：Python序列和list列表
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 10:26
 * Version(版本): 1.0
 * Description(描述)： list列表
 """
# 使用 [ ] 直接创建列表


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7]
    emptyList = []
    # 将字符串转换成列表
    list1 = list("hello")
    print(list1)
    # 将元组转换成列表
    tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
    list2 = list(tuple1)
    print(list2)
    # 将字典转换成列表
    dict1 = {'a': 100, 'b': 42, 'c': 9}
    list3 = list(dict1)
    print(list3)
    # 将区间转换成列表
    range1 = range(1, 6)
    list4 = list(range1)
    print(list4)
    # 创建空列表
    print(list())

    print(list4[1])
    print(list4[2])
    print(list4[3])
    print(list4[-2])
    print(list4[-3])
    print(list4[1:3])

    list5 = [5, 7, 8]
    print(list5)
    del list5
    # print(list5)
