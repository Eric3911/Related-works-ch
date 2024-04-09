'''
    动态语言：
    解释型语言：
'''

'''
    静态变量类型：数字、字符串、元组
    动态变量类型：列表、字典、集合
'''

number1 = 1 #int
number2 = 1.0 #float
number3 = 10012345678987654323456787654334567  #long
number4 = 1000 + 1j #complex

type1 = type(number1)
type2 = type(number2)
type3 = type(number3)
type4 = type(number4)
print(type1, type2, type3, type4)


# string
str1 = "abcdefghijklmno1234567890.,/;'[]"
print(type(str1), str1)
print(str1[0]) #输出字符串的第一个字符
print(str1[2:6]) #输出第二个到第七个（不包含第七个）字符
print(str1[2:]) #输出从第三个开始的所有字符
print(str1 * 2) #输出字符串2次
print(str1 + "TEST") #拼接字符串


# tuple = 只读列表
tuple1 = ('a', "abcde", 123, 1.23)
print(type(tuple1), tuple1)
print(type(tuple1[0]), tuple1[0])
print(tuple1[1:3])
print(tuple1[1:])
print(tuple1 * 2)
tuple2 = ('b', 5)
print(tuple1 + tuple2) #tuple2不能只有一个元素，否则系统不把它当作元组


# list查找
list1 = ['a', "abcdefg", 123, 1.23]
list2 = ['b']
print(type(list1), list1)
print(list1 + list2) # list的拼接，list2可以只有一个元素
value1 = list1[0]
print(value1, type(value1))
print(list1[1:3])
print(list1[:], list1[1:], list1[:2]) # 如何进行倒叙访问
# list增删改
list3 = []
list3.append("google") # 在list3尾部添加元素
list3.append("baidu")
list3.append('a')
list3.append(123)
print(list3)
list3.insert(2, 2024) # 在指定位置添加元素
print(list3)
#修改list中的元素
print(list3)
list3[2] = 2025
print(list3)
#list元素的删除
print(list3)
del list3[0] # 按照位序删除
print(list3)
list3.remove(2025) # 按照值删除
print(list3)


#dictionary
dict1 = {'a': 1, "abc": 2, "abcd": 3}
print(dict1["abc"])
print(dict1, type(dict1))
print(dict1.keys()) # 打印所有键的值
print(dict1.keys) # 打印key的内存地址
print(dict1.values())
print(dict1.values)
#字典增加元素
dict1["abcedf"] = 12223
print(dict1)
# 字典属于无序结构，在指定位置插入需要先将它转化为有序字典
dict1["abc"] = 'a' # 对指定key的value修改
print(dict1)
del dict1["abc"] # 删除这个键对应的条目
print(dict1)
dict1.clear() # 清空字典
print(dict1)
#
dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
print('zzz',dict2)
dict3 = dict2.copy()
dict3['a'] = 10
dict3['b'].append(4)

print('xxx',dict2)
print(dict3)

original_dict = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}

# 使用copy()方法创建一个浅拷贝
new_dict = original_dict.copy()

# 修改新字典中的一个不可变元素（数字）
new_dict['a'] = 100

# 修改新字典中的一个可变元素（列表）
new_dict['b'].append(4)

print('Original Dictionary:', original_dict)
print('New Dictionary:', new_dict)

import copy

# 创建原始字典
original_dict = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}

# 使用deepcopy()创建一个深拷贝
new_dict = copy.deepcopy(original_dict)

# 修改新字典中的可变元素
new_dict['b'].append(4)
new_dict['c']['d'] = 5

print('Original Dictionary:', original_dict)
print('New Dictionary:', new_dict)




dict5 = {"abc": [1, 2]}
dict5['abc'] = [1.2,3,4]
print(dict5)


