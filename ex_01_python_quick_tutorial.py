print('Hello Python')

print('Hello Python','!','赵怡慧')

#这是一个注释

'''
这是一个注释
这是一个注释
这是一个注释

'''



name='Allen'
print(name)



int1=10
float1=10.5

print(int1)
print(float1)

#type()   查看数据类型的方法
print(type(int1))
print(type(float1))

# 布尔值
b1=True
b2=False
print(b1,'===',b2)
print(type(b1),'===',type(b2))

#字符串
str1='Silence 汪苏泷'
print(str1)
print(type(str1))

#容器
list1=[10,20,30]
#列表用中括号
tuple1 = (100,200,300)
#元组用小括号
set1 = {101,102,103} 
#集合用大括号
dict1 = {'name','汪苏泷'}
#字典用大括号以及单引号

print(list1)
print(tuple1)
print(set1)
print(dict1)

print(type(list1))
print(type(tuple1))
print(type(set1))
print(type(dict1))





#04_赋值运算符的使用.py

name='汪苏泷'
print(name)

num1,num2,num3=10,20,30
#可以这样写，左右数量相等
print(num1)
print(num2)
print(num3)

a=b=100
print(a)
print(b)

'''
复合运算符+=  -=   *=
'''

a=200
a += 10
#   a += 10    等于   a = a + 10
print(a)

b = 300
b *= 1+2
#   b *= 1+2    等于    b = b*(1 + 2)
print(b)





#05_比较运算符的运用.py


a = 100
b = 200

print(a == b)   #判断a是否等于b
print(a != b)   #判断a是否不等于b
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)





#06_逻辑运算符的使用.py


# and  or  not

a = 1
b = 2
c = 3

print(a > b and b > c)
#两者都符合才会返回一个true
print(a < b and b < c)


print(a > b or b < c)
#有一个表达式是ture 返回的就是true


print(not a > b)  #取反





#07_字符串的创建.py

name1 = '白幼薇'
name2 = '沈墨'

print(name1)
print(name2)
print(type(name1))
print(type(name2))
#结果给出str 表示字符串


#多行字符串infor
infor1 ='''
叮
欢迎来到玩偶游戏
'''

infor2 ='''
我以为我会拯救世界，
结果是世界拯救了我。
'''

print(infor1)
print(infor2)
print(type(infor1))
print(type(infor2))

# 当内容有单引号时的两种解决方式
say1 = "I'm Eva."
say2 = 'I\'m Eva.'

print(say1)
print(say2)






#08_输入操作.py

uname = input()
password = input()
# input()  运行后需要在下方输入   见code程序结束
#但是它没有给用户任何提示，非常不友好

'''
so  我们只需要在input里面 输入一些相应的提示信息
'''

uname = input("请输入用户名：")
password = input("请输入密码：")

print('您输入的用户名是：',uname,'    密码是：',password)
print(type(uname))


'''
输入特点
1、当程序执行到input,等待用户输入，输入完成之后才继续向下执行

2、在Python中，input会把接收到的任意用户输入数据都当作字符串处理

3、在Python中，input接收用户输入后，一般存储到变量，方便使用
'''





name = '汪苏泷'
print(name)

#我们目前知道的多个输出的方法
#不过目前两个还能接受，多了的话，隔开，隔开  就显得过于繁琐
print('我的名字：',name)


#方法二
print('我的名字：{}'.format(name))
#变种1
print('我的名字：{0}'.format(name))  #数字即指定位置，0代表后面的第一个参数
print('我的名字是：{0},{1},{2}' .format(name, '你好' , '你直接告诉他得了呗' ))
#变种2
print('我的名字是：{a},{b},{c}'.format(a = name, b = '故事的发展有很多', c = '意外' ))


#方法三（python3.6之后的写法，之前的版本不支持哦）
#其实是方法二的变种啦
print(f'我最喜欢的人是：{name}',   '逃避过整个世界，也拥抱过世界' )
print('满怀深情的说' , '随便')





#10_字符串下标的使用.py

#从一串字符串中去除一个 （从0开始数哦，宝贝）
info = '随便，汪苏泷.'
print(info[0])    #比较短还行，长了就。。。



#达拉笛当， 长了的解决方式

#一、从后往前数
print(info[-1])
print(info[-2])

#二、取好多个（用：隔开   从哪开始 到哪结束）
print(info[3:6])
'''注意哦，要取到你想要的下一个'''
print(info[3:-1])
'''从最前端或者最末端开始取  可以有省略的'''
print(info[:2])
print(info[-4:])

#倒着写
print(info[::-1])   #  开始：结束：步长   负数就是倒着输出
print(info[::2])    #2 从左往右，每隔一个获取一个






#11_字符串常用的方法.py

#常用的 三种方法:  查找  判断   修改

info = 'hello python and world and allen'


#查找操作   一般有 find  index(指数 指示 索引) count

# find
print('='*10,'find','='*10)   
'''我只是一行平平无奇的分割线'''

print(info.find('and'))
#返回的是13   表明从第一个字符下标开始数到第13个结束
print(info.find('and',15,30))
#返回的是23    表明从第15个字符下标开始数到23找到'and'
print(info.find('ands'))
#返回的是-1    表明没有找到，，（因为我们的字符串info中就没有'ands'这个单词）


#index的使用方式基本同find
'''但是index 没有找到的时候会报错'''
print('='*10,'index','='*10)
'''我只是一条没有感情的分割线'''

print(info.index('and'))
print(info.index('and',15,30))
# print(info.index('ands'))
#  找不到会返回 substring(子字符串) not found
'''中途报错就不能运行下去了，所以知道那意思就行了'''


#count    (用来判断这里面有多少个)
print('='*10,'count','='*10)
'''我是那条分割线，我又来了'''

print(info.count('and'))
print(info.count('and',15,30))
print(info.count('ands'))


#修改操作    （更改大小写之类的玩意）

print('='*10,'修改首字母大小写','='*10)
'''分割分割分割'''
print(info.upper())     #upper  上面的；上部的
print(info.lower())     
print(info.title())      
'''每一个单词的首字母'''
print(info.capitalize())     #capitalize  资本化；首字母大写
'''只有第一个单词的首字母'''


#replace  替换
print('='*10,'replace','='*10)
'''又又又是我——分割线'''

print(info.replace('and','add'))
print(info.replace('and','add',1))   #只替换了一个呢


#split  分裂
print('='*10,'split','='*10)
'''这里是一条来了又来的分割线'''

print(info.split())   #按空格分裂
print(info.split('and'))      # 按and分裂

tmp = info.split()


#拼接   join
print('='*10,'join','='*10)
'''分分分分分割线'''

print(' '.join(tmp))
#''  中填上拼接以后想要的连接方式


#去除空格  strip   (n.条；带；脱光)
print('='*10,'strip','='*10)
'''哈哈哈，分割线我又来了'''

info2 = '      而太空的星星   会不会唱歌很好听    '
print(info2.strip())
print(info2.lstrip())   #只去左边  left
print(info2.rstrip())    #只去右边  right



#判断  startswith   endswith   判断是否为指定字符
print('='*10,'判断是否为此字符','='*10)
'''没错，就是我——分割线'''

print(info.startswith('不适合你的年纪'))
print(info.startswith('hello'))

info3 = '123'
info4 = 'abc'
info5 = 'abc123'
info6 = 'abc_'
print(info3.isdigit())   #digit  n.数字 ；手指  
print(info4.isalpha())
print(info5.isalnum())






#12_列表的使用.py

print("="*10,'append','='*10)
#append (追加  增补)
'''  append  往列表里面增加内容'''
name_list = ['魏应洲','谢聿','明华严','兰残音']
name_list.append('乔银魏谢，万人不破')
print(name_list)

#  name_list.append('而太空的星星','会不会唱歌很好听') 
'''此时会报错 （2 given)  不支持这种写法'''

#so 尝试添加一个列表
name_list.append(['而太空的星星','会不会唱歌很好听'])
print(name_list)
'''然而， 此时打印出来的结果为列表套列表（禁止套娃）'''
#所以append 只能增补单一内容




print('='*10,'extend','='*10)
#extend   追加多个数据（这不就来了吗）
name_list1 =  ['魏应洲','谢聿','明华严','兰残音']
name_list1.extend(['乔银魏谢','万人不破'])
print(name_list1)

'''注意extend 就是一只随便拆家的二哈'''
name_list1.extend('汪苏泷')
print(name_list1)   #它print出来是 '汪’，'苏','泷'



print('='*10,'insert','='*10)
#insert （v.插入，添加    n.插页，广告附加页
#insert  可以在指定位置上进行相应的增加

name_list2 = ['魏应洲','谢聿','明华严','兰残音']
name_list2.insert(1,'你喜欢我吗')
name_list2.insert(3,'喜欢')
name_list2.insert(5,'你回没回家')
name_list2.insert(7,'还没')
print(name_list2)




#  哈哈哈，不能光添加呀，，，让我们删掉它

# del
print('='*10,'del','='*10)
name_list3 = ['魏应洲','谢聿','明华严','兰残音']
del name_list3[1]    #从0开始数哦
print(name_list3)

''' 还可以把整个变量给干掉'''
#  del name_list3
print(name_list3)  #(会报错哦)


#pop
print('='*10,'pop','='*10)
'''你的list会变成拿出来以后剩下的
      不给它输入数据的话，它就自己从最后一个开始取了'''

name_list4 = ['魏应洲','谢聿','明华严','兰残音']
tmp1 = name_list4.pop()
print(tmp1)
print(name_list4)

tmp2 = name_list4.pop(1)
print(tmp2)
print(name_list4)



# remove
print('='*10,'remove','='*10)
#必须要输入参数！！！   要不然就会报错

name_list5 =  ['魏应洲','谢聿','明华严','兰残音']
name_list5.remove('魏应洲')
print(name_list5)



#  clear
print('='*10,'clear','='*10)
'''有一点子类似于pop  
   不过pop 是直接干掉变量     clear则只是清空列表'''

name_list6 = ['魏应洲','谢聿','明华严','兰残音']
print(name_list6)
name_list6.clear()
print(name_list6)




print('='*10,'修改','='*10)
#直接通过索引的方法修改内容
name_list7 = ['魏应洲','谢聿','明华严','兰残音']
name_list7[2] = '人类可以自取灭亡，但不能被奴役致死'
print(name_list7)


#reverse  颠倒顺序
print('='*10,'reverse','='*10)
#reverse  (v.颠倒，彻底转变   adj.相反的)

name_list8 = ['魏应洲','谢聿','明华严','兰残音']
print(name_list8)
name_list8.reverse()
print(name_list8)



#sort   排序操作
print('='*10,'sort', '='*10)

name_list9 = ['魏应洲','谢聿','明华严','兰残音']
print(name_list9)
name_list9.sort()
print(name_list9)

'''我不理解    sort  到底是按啥排序的！！！！  
                    首字母吗    不对呀     我裂开'''


#in  判断
print('='*10,'in','='*10)
name_list0 = ['魏应洲','谢聿','明华严','兰残音']
print('赵怡慧' in name_list0)
print('谢聿' in name_list0)






#13_字典的使用.py

'''
   1、字典的数据以“键值对” 形式存储
   2、字典数据和数据顺序没有关系
   3、字典不支持下标
   4、后期无论数据如何变化，只需要按照对应的键的名字查找数据即可
     '''

#要想使用字典，，首先要创建一个字典
'''创建字典的三种方式'''
dict1 = {}
dict2 = dict()
dict3 = {'name':'普通爱情故事','from':'随便','date':'2021-07-24'}

print(type(dict1))
print(type(dict2))
print(type(dict3))


dict1['name'] = '威廉敏娜'
#[]是一个key
print(dict1)





#14_选择结构的使用.py

# 单分支选择结构
print('='*10,'单分支选择结构','='*10)

year = 2021

if year > 2020:
    print('反复怀念，脑海蒙太奇的碎片')


#  双分支选择结构
print('='*10,'双分支选择结构','='*10)

if year > 2021:
     print('反复怀念，脑海蒙太奇的碎片')
else:
    print('辩证思维理性观点，运气总不站我这边')


#  多分支选择结构
print('='*10,'多分支选择结构','='*10)
level = 0

if level == 0:
    print('拒绝游戏变成玩偶') 
elif level == 1:
    print('游戏失败变成玩偶')
elif level ==2:
    print('游戏成功奖励及玩偶')    
else:
    print('叮，欢迎来到玩偶游戏')
'''一个等号是  '赋值'    两个等号才是  '等于'
'''




#15_多层选择结构的使用.py

year = 2020
if year > 2020:
    level = 0

    if level == 0:             #按中Tab 向右移动
        print('拒绝游戏变成玩偶') 
    elif level == 1:
        print('游戏失败变成玩偶')
    elif level ==2:
        print('游戏成功奖励及玩偶')    
    else:
        print('叮，欢迎来到玩偶游戏')

else:
    print('也看懂了世界，也看不懂世界，满怀深情的说随便')






#16_三目运算符的使用.py

point = 2

if point == 3:
    print('我擦肩而过的爱情，自卑敏感的个性')
else:
    print('逃避过这个世界，也拥抱过世界，嬉皮笑脸的说随便')


#初步简化
print('='*10, '初步简化','='*10)
point = 2

if point == 3:
    rs = '我擦肩而过的爱情，自卑敏感的个性'
else:
    rs = '逃避过这个世界，也拥抱过世界，嬉皮笑脸的说随便'

print(rs)



# 简化进阶
print('='*10, '简化进阶','='*10)

rs = '我擦肩而过的爱情，自卑敏感的个性' if point == 3 else'逃避过这个世界，也拥抱过世界，嬉皮笑脸的说随便'
print(rs)




#17_while的使用.py

#这样重复的东西完全可以优化的
print('但我真的没假装，是你的想象')
print('但我真的没假装，是你的想象')
print('但我真的没假装，是你的想象')
print('但我真的没假装，是你的想象')
print('但我真的没假装，是你的想象')
print('任务结束了')


i = 0
while i < 5 :
    print('但我真的没假装，是你的想象')
    i +=1    # i+1 =1
print('爱过的那些时光，你别觉得多难忘')



#  1 到 100之间的累加和
#  1+2+3+...

i = 0
rs = 0

while i <= 100:
    rs += i # rs = rs+i
    i += 1

print(f'1-100之间的累加和是：{rs}')






#18_for的使用.py

for a in '星星坠落时':
      print(a)
#竖着打印了，每一个汉字都占了一行


#用for 语句来遍历列表
for a in ['一颗一颗流星','划过遥远天际','带着谁的委屈','唱着谁的回忆'] :
    print(a)


#计算1-100的和
#使用一个函数   range(start,end,step)

rs = 0

for i in range(1,101):     #后面这个是不被包含的，所以要写到101
    rs += i

print(f'1-100之间的和是：{rs}') 


for i in range(5):
    print(i)        #默认从0  start






infos = [
    ['在神秘伊甸园','在偷吃苹果前','在爱情没被定义为爱情的那几年','那一首有点甜','永恒经典'],
    ['你总说要有个家','能让我放下挣扎','可用尽所有办法也没能让我好点吧'],
    ['困扰着我的问题','是宇宙和我自己','我拥有所有情绪','没法用语言告诉你',],
    ['都说我有点叛逆','但我不需要同情','我只是还没办法和成熟成为共同体'],
    ['我短暂的拥有过玫瑰和狐狸','我欣赏过四十次日落的风景','我训练过面对你每一副表情','我已经分不清','哪一个是自己'],
]

for info in infos:
    for i in info:
        print(i)          #还没给一个谁是第几段的信息

for info in infos:
    print('='*10,'第一段的内容','='*10)      #现在是一个死的东西，，我们增加一个变量，把它变活
    for i in info:
        print(i)



'''方法一'''
count = 1
#for info in infos:
# count +=1
#    for i in info:
 #       print(i)


'''方法二'''
for i in range(len(infos)):
    print(f'===================第{i+1}段的内容====================')
    for info in infos[i]:
        print(info)


'''方法三'''
for i,info in enumerate(infos):      #  enumerate 是帮助记录，，，内容是索引
    print(i) 





   #20_break_continue的使用.py

print('去612星球，开万有引力演唱会')

i = 1
while True:
    if i ==5: 
        print('随便不错的，爱了爱了~回家')
        break
    print('跑错地方了，重新出发')
    i += 1


for i in range(10):
    print('点赞')
    print('收藏')
    print('投币')




     #21_函数的使用.py

print()    #这就是一个函数



'''无参数'''

def fun1():
    print('而太空的星星，会不会唱歌很好听，风不停，吹乱了我的发型')
    #此时只是定义了一个函数，需要调用它才能发挥它的价值

fun1()     # 我们定义的函数没有设定参数


'''传递一个参数'''

def fun2(info1):
    print(f'不是很聪明，不适合你的年纪，不擅长游戏，不能够{info1}')
fun2('逗你开心')