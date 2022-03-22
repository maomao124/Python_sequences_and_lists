"""
 * Project name(项目名称)：Python序列和list列表
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 10:15
 * Version(版本): 1.0
 * Description(描述)： 序列

 序列切片
切片操作是访问序列中元素的另一种方法，它可以访问一定范围内的元素，通过切片操作，可以生成一个新的序列。
sname[start : end : step]

其中，各个参数的含义分别是：
sname：表示序列的名称；
start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进行切片；
end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，
则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略。

函数	    功能
len()	计算序列的长度，即返回序列中包含多少个元素。
max()	找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，
        否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。
min()	找出序列中的最小元素。
list()	将序列转换为列表。
str()	将序列转换为字符串。
sum()	计算元素和。
sorted()	对元素进行排序。
reversed()	反向序列中的元素。
enumerate()	将序列组合为一个索引序列，多用在 for 循环中。
 """

if __name__ == '__main__':
    str1 = "hello world"
    print(str1[0], "==", str1[-11])
    print(str1[10], "==", str1[-1])
    print(str1[:2])
    print(str1[3:])
    print(str1[::2])
    print(str1[:])
    print(str1 * 3)
    list1 = [None] * 10
    print(list1)
    print("h" in str1)
    print("1" in str1)

    print(len(str1))
    print(max(str1))
    print(min(str1))
    print(list(str1))
    print(sorted(str1))
    print(reversed(str1))


