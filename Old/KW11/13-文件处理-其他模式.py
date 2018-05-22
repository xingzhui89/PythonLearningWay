# f=open('xxx','r+',encoding='gbk')
# # data=f.read()
# # print(data)
# # f.write('123sb')

# f.write('sb')


#文件修改
# src_f=open('xxx','r',encoding='gbk')
# data=src_f.readlines()
# src_f.close()
#
# # for i in data:
# #     print(i)
# print(data)
# dst_f=open('xxx','w',encoding='gbk')
# # dst_f.writelines(data)
# dst_f.write(data[0])
# dst_f.close()

# with open('a.txt','w') as f:
#     f.write('1111\n')


# src_f=open('xxx','r',encoding='gbk')
# dst_f=open('xxx','w',encoding='gbk')
# with open('xxx','r',encoding='gbk') as src_f,\
#         open('xxx_new','w',encoding='gbk') as dst_f:
#     data=src_f.read()
#     dst_f.write(data)

f=open('a.txt')
print(f.encoding) #查看文件编码



# f=open('test11.py','rb',encoding='utf-8') #b的方式不能指定编码
# f=open('test11.py','rb') #b的方式不能指定编码
# data=f.read()
# #'字符串'---------encode---------》bytes
# #bytes---------decode---------》'字符串'
# print(data)
# print(data.decode('utf-8'))
# f.close()


# f=open('test22.py','wb') #b的方式不能指定编码
# f.write(bytes('1111\n',encoding='utf-8'))
# f.write('杨件'.encode('utf-8'))

f=open('test22.py','ab') #b的方式不能指定编码
# f.write('杨件'.encode('utf-8'))

# open('a;ltxt','wt')


# f=open('日志文件','rb')
# data=f.readlines()
# print(data[-1].decode('utf-8'))

f=open('日志文件','rb')

# for i in f.readlines():
#     print(i)

#循环文件的推荐方式
# for i in f:
#     print(i)

for i in f:
    offs=-10
    while True:
        f.seek(offs,2)
        data=f.readlines()
        if len(data) > 1:
            print('文件的最后一行是%s' %(data[-1].decode('utf-8')))#因为data是个列表，所以读取最后一行只要指定-1
            break
        offs*=2