s1 = 'asdf'
s2 = 'asdffas'

test = 'aLex'
v = test.capitalize()  # 将字符的首字母大写，其他都是小写
print(v)

v1 = test.casefold()  # 这个更牛逼，把所有字符变小写
print(v1)

v2 = test.lower()
print(v2)

v = test.center(20, '*')
print(v)

test = 'aLexalexr'
v = test.count('ex')  # 统计字符中出现某个字符的次数
print(v)

v = test.endswith('ex')
print(v)
v = test.startswith('ex')
print(v)
v = test.__contains__('ex')
print(v)

test = '12345678\t9'
print(len(test))
v = test.expandtabs(6)  # 将字符串中的tab延长
print(v, len(v))

test = 'alexalex'
v = test.find('ex')  # 从前往后找指定字符的位置，只是第一个
print(v)
v = test.rfind('ex')  ##从前往后找指定字符的位置，找最后一个
print(v)
v = test.index('ex')  # index找不到，报错,尽量不用
print(v)

# 格式化，将一个字符串中的占位符替换为指定的值
test = 'i am {name}, age {a}'
print(test)
v = test.format(name='alex', a=19)
print(v)

# 格式化，传入的值 {"name": 'alex', "a": 19}
test = 'i am {name}, age {a}'
v1 = test.format(name='df',a=10)
v2 = test.format_map({"name": 'alex', "a": 19})

# 字符串中是否只包含 字母和数字
test = "123"
v = test.isalnum()#如果都是数字，返回true
print(v)

# 是否是字母或者汉子
test='as2df'
v=test.isalpha()
print(v)
v=test.isalnum()
print(v)

# 13 当前输入是否是数字
test = "二" # 1，②
v1 = test.isdecimal()
v2 = test.isdigit()
v3 = test.isnumeric()
print(v1,v2,v3)

# 16 判断是否是标题
test = "Return True if all cased characters in S are uppercase and there is"
v1 = test.istitle()
print(v1)
v2 = test.title()
print(v2)
v3 = v2.istitle()
print(v3)

# 17 ***** 将字符串中的每一个元素按照指定分隔符进行拼接
test = "你是风儿我是沙"
print(test)
# t = ' '
v = "_".join(test)
print(v)

# 18 判断是否全部是大小写 和 转换为大小写
test = "Alex"
v1 = test.islower()
v2 = test.lower()
print(v1, v2)

v1 = test.isupper()
v2 = test.upper()
print(v1,v2)

# 20 对应关系替换
test =  "aeiou"
test1 = "12345"

v = "asidufkasd;fiuadkf;adfkjalsdjf"
m = str.maketrans("aeiou", "12345")
new_v = v.translate(m)
print(new_v)

