#! /usr/bin/python
# ! coding=utf-8

#  id(object)  查看每个对象的内存的地址
#   type(object) 返回对象的类型

# 对普通的除法来说,例如 5/2==2  为解决数据类型带来的问题，可以导入模块解决这个问题
# from __future__ import division

# 取余数方法  divmod(5,2)  返回商和余数的元祖
# 四舍五入     round(1,2437,2) 返回1.24

# 导入match函数
import math

# 函数帮助
help(math.pow)

# 几个常用的函数
# 求绝对值  abs()

# 字符串
"""
    python中的字符串是一种对象类型，这种类型使用str表示 ，通常使用‘’或""包裹起来
   在字符串连接中，用+连接起来的对象必须是同一种类型. 对于 12+"wfef"会报错
   下面是几种问题的解决方案
   1.使用反引号   a=353; b+`a` (这里是反引号)
   2.使用str函数  a=345; b+str(a)
   3.使用repr函数 a=345; b+repr(a)   同第一种一样 
   
   
   对于转义字符的解决方案
   
   doc="c:\news" 这时会被转义为c:换行ews,解决这个问题有两种解决方案
   1.   doc='c:\\news'  添加\进行转义
   2.   doc=r'c\news'   在字符串前面添加r，代表的是原字符串，不会进行转义操作
   
   
   索引和切片
   使用  lang="sdhrshwr"   c=lang[:]  不写代表的是复制一份  等同于c=lang，将指针引用指向lang指向的地址
   
   字符串的基本操作
   1.len()  求序列长度
   2.连接多个字符串序列
   3.in 判断元素是否在序列中
   4.max()  返回最大值
   5.min()   返回最小值
   7.cmp(str1,str2):比较两个序列是否相同
   
   order()函数可以返回单个字符的ascll码
   chr()函数 可以返回ascll码对应的字符
   
   
   字符串格式化输出
   “i like %s” % "python"
   "i like %d" % 12
   "i like %c" % 'e'
   上面的操作同c语言的相关操作相同
   
   多个占位
   "ni hao %s i am %s " %("a","fang")
    
   python中如何避免中文乱码
   1.在开头申明  coding=utf-8
   2.遇到字符(节)串，立即转换为unicode编码，不要直接使用str()，直接使用unicode()
   unicode_str=unicode('中文',encoding='utf-8')
   print unicode_str.encode('utf-8')
   
   3,如果对文件操作，打开文件的时候，最好用 codecs.open替代open
   import codecs
   codecs.open("filename",encoding="utf-8")
   
   4.申明字符串加u ，声明的字符串就是unicode编码的字符串
        
"""

# 列表
"""
    bool()是一个布尔函数，作用是用来判断一个对象是'真'还是’空‘(假)
    索引和切片(同上面的str一样)
    反转
    alert=[1,23,5,5]
    alert[::-1]  (反转里面的数据)(对于字符串同样适用)
    下面是推荐的list反转的写法
    list(reversed(alert))   
    reversed(object)返回一个可以迭代的对象
    
    对list的基本操作
    1.len()
    2.+ 连接两个序列  li=['asf','sdf']; as=[1,2,3]; li+as==['asf','sdf',1,2,3]
    3.*,重复元素     li=['asf']   li*3==['asf','asf','asf']
    4.in操作 查看元素是否在集合中
    5.max(),min()  查看最小和最大的元素
    6.cmp(li,as) 比较两个集合的大小
    7.追加 append()   li.append("sg")== li[len(li):]="sg"
    8.entend(iterable)  附加一个可以迭代的对象的数据 等同与   la+=lb(la,lb为list)
    
    
    如何判断一个对象是迭代对象
    astr="python"
    hasattr(astr,"__iter__")  (也就是判断这个对象有没有__iter__属性)   查找的时候我们通过 dir(object)也可以直接看出对象是不是有__iter__属性
    
    列表是可以修改的，这种修改不是复制一个新的，而是在原地进行修改
    list.count(object) 对象在list中出现的次数
    list.reversed() 把列表的数据反过来  但是没有返回值，所以不能实现list的反向迭代
    list.sort() 从小到大进行排序 
    
    sorted()内置的排序的函数
    
    list与str的异同
    相同点
    1.都属于序列类型的数据，都可以通过编号进行元素的访问
    区别
    list是可以更改的，但是str是不可以更改的
    
    多维list
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    
    list和str的转换
    str转list
    str.split()
    name=['afagfa',"sherh"]
    "".join(name)

"""

# 元祖
"""
    t=123,"abc",["come","here"]
    t==(123,"abc",["come","here"])
    我们知道部分的函数传递的是*argc代表的就是一个元祖，所以我们可以按照这个方式直接传递过去    
    def demo(*argc):
        print(argc)
        pass
    demo("534634","afg","sgwe",2,3,53,["sgwet","sgw"],{"sgwe","wser","sgwegw"})
    所以可以按照这个方式直接调用
    
    索引和切片
    和list以及str一样都是支持这样的操作的
    
    提醒:如果一个元祖只有一个元素，需要在该元素后面添加逗号，避免解析出错
    
    所有在list可以修改的list的方法，在tuple中都失效
    
    tuple的用途
    1.速度快，用在作为常量的集合
    2.对不需要修改的数据进行写保护
    3.tuple可以作为dict的key,dict的key是不变的，tuple满足这一特性
    4.可以用在字符串的格式化操作
"""

# 字典

"""
    mydict={}
    mydict={"name":"fang","sex":"男"}
    添加
    mydict["phone"]=13077995907
    
    根据dict()函数构造下面给出几个构建dict的例子
    
    利用list构造
    dic=dict([("name","fang"),("age",22)])
    利用元祖构造
    dict((("name", "fang"), ("value", "sgsg")))
    利用set构造
    dict({("name", "fang"), ("value", "sgsg")})
    利用元祖list构造
    dict((["name","fang"],["value","afweg"]))    
    利用元祖和set构造
    dict(({"name", "fang"}, {"value", "sgwerw"})) 
    利用关键字构建 
    dict(name="fang",age=23)
    利用自身函数构建
    {}.fromkeys(["fanga", "sghw"], "agwegwg")
    
    dict存放的数据是键值对隐射的，所以就没有索引以及切片的功能
    
    基本操作
    1.len(d)返回字典键值对的数量
    2.d[key]返回字典d的key
    3.d[key]==value赋值操作
    4.del d[key]  删除key以及value
    5 key in d 检查指定的key是否在d中
    
    
    方法操作
    1.copy()实现的是浅拷贝，拷贝了基本类等，但是对于list等，还是一个引用，copy的对象的list引用指向被拷贝对象的list
    在python中实现深copy需要导入copy模块
    import copy
    z=copy.deepcopy(x)
    
    2.clear()清除字典
    
    3.setdefault(key,value) 在字典中如果没有找到指定的key,就返回设置的默认的key
    
    4.items()返回一个存放tuple的list,tuple的前者为key，后者为值
    
    5.iteritems()  返回一个可以迭代的类型
    
    6.has_key()判断是否存在某个key
    
"""

# 集合
"""
    可以用{}花括号定义，其中的元素没有序列，也就是非序列类型的数据，不能通过索引和切片进行访问，而且set中的元素不可以重复，类似dict的key
    使用list和set可以实现两个类型的转换 利用set()建立的set是可变的集合
    set1=set(("sgws","sgw","shgwerhg"))
    set1=set({"sgw","sg","sgsd"})
    
    
    冻结的集合(可哈希)
    frozenset()
    
    issubset(set) 是不是set的子集
    
"""
# 语句
"""
    zip(c) zip是一个内置的函数，它的参数必须是某种序列数据类型，如果是字典，那么键视为序列
    
    enumerate()函数 可以获得迭代对象的索引以及元素
    
    for i in range(len(week)):
        print(week[i]+' is '+str(i))
    
    改为下面的操作
    for (i ,day) in enumerate(week):
        print(day+" is "+str(i))
        
    list解析
    squares=[x**2 for x in range(1,10)]
    
    
    while...else
    例子
    count=0
    while count<5:
        count=count+1
    else:
        print("is not less than 5")
        
    
    同样 
    for....else
    for n in range(99)
    
     
"""

# 文件
"""
    文件读取的操作
    while True:
    line=file.readline()
        if not line:
            break
        print(line)
    
    file.seek()移动文件指针
       
    
"""

# 迭代
"""
    iter()是一个内置函数，返回一个可以迭代的对象，参数是一个复合迭代条件的对象或者是一个序列
    1.通过dir()函数查看对象是否存在__iter__属性就可以知道对象是否可以进行迭代，如果存在就代表可以迭代
    2.可以迭代的对象都是可以使用list解析的，因为都是可以迭代的对象，下面给出例子
    suples=(2,4,64,7,7)
    suples=[value*2 for value in suples]
    
    suples=[isinstance(value,int) for value in suples ]
    
    上面的两个都是可以进行操作的
    
    
"""

# 自省
"""
    检查某些事物以确定他是什么，他知道什么以及它能做什么。一旦你使用了支持自省的编程语言，就会产生“未经检查的对象不值得实例化”
    
    dir()的用法
    在不指定object,则返回当前作用域的名称，以及变量
    dir()函数用于所有的对象类型，包括字符串，整数，列表，元组，字典 函数 定制类 类实例  类方法
    
"""

# 函数
"""
    python中为是对象编写接口，而不是为数据类型，所以编写的函数灭偶遇具体的类型。具体的操作一句具体的操作
    这个也可以理解为python中的多态机制
    
    对于*argc和**args
    def demo2(*argc,**args):
        print(argc)
        print(args)
    
    
    1.直接传递值  demo2("454",{3,4,64,4},"46346")   这些参数都会被收集到tuple中，也就是第一个形参收集
    2.使用名称传递 demo2(argc={2,3,53,654},args=[34634,4,64,54,3])   本以为argc会赋值给tuple，但是实际都给了dict,其实这部分的内容在前面已经说了，如果使用key:value,dict就会将key
    作为key,dict作为value
    3.使用元组加名称
    demo2(35,26,54,64,464,value=(("fang","demo"),("value","demo")))
    (35, 26, 54, 64, 464)
    {'value': (('fang', 'demo'), ('value', 'demo'))}
    我们发现只要加名称就会被dict解析，同时作为key
    4.使用元组
    demo2(2,3,43,64,6,(("fang","demo"),("value","demo")))
    (2, 3, 43, 64, 6, (('fang', 'demo'), ('value', 'demo')))
    {}
    我们发现一个现象，不管你怎么赋值，就算你赋值的操作符合dict()的赋值标准，都不会被dict接收，只能通过关键字
    
    下面是例子
    value = {"23523", 346, 2, 643, 734}
    print(*value, "\n", "...")
    2 643 23523 346 734  依旧会被收集，尽管参数一已经使用了参数收集
    ...
    print(*value, sep="\n", end="...")
    这个就是实现了参数的匹配，但是需要记住的是，参数的option不能写错了
    dict = {"values": {3, 2, 4, 46}, "sep": "\n", "end": "..."}
    print(**dict)   会出错，原因是value不能匹配，我猜这是由于value是一个tuple的原因
    

    使用元祖或字典进行传值
    def demo4(name,age,sex,address):
        print(name,age,sex,address)
    
    元组调用
    value=("fang",23,"男","anhui")
    demo4(*value)
    
    字典调用
    value={"name":"fang","age":23,"sex":"男","address":"anhui"} 其中的key要和参数的对应
    demo4(**value)
    
    
    几个特殊的函数
    
    lambda
    对于这个函数可以使用lambda这样实现
    list=[1,2,3,4,5]
    squrance=[x*x for x in list ]
    下面是lambda的实现
    lam=lambda x:x+x
    list2=[]
    for i in list1:
        list2.append(lam(i))
    感觉没有上面的语法简化
    
    
    map(func,iterables)函数  func是一个函数，seq是一个序列对象，在执行的时候，将序列对象的元素取出进行func的操作，然后再次存放到序列对象中
    例子
    def demo5(x):
        retrun x+x
    map1=map(demo5,"fagdga")
    
    
    总结，实现迭代对象的自身值的操作，通过上面的技术，就可以有三种实现
    1.lambda
    2.list解析
    3.map函数实现
    
    reduce()函数 实现的可迭代对象的值内部迭代的和
    reduce(lambda x,y:x+y,[1,2,3,4,5])   ==    ((((1+2)+3)+4)+5 实现的是求和的运算
    
    
    简意的实现list的和的计算
    sum(x*y for x,y in [(2,2),(3,3),(43,5),(5,5),(36,734),(3,46)])   这里需要注意的是list里面是一个tuple，迭代的实现不仅对外边的list实现了迭代，同时也实现了
    对内部的tuple的迭代,这种的结构可以通过zip()实现,重点是x,y代表的就是每一项都有两个元素 ，所以可以通过很多都能实现  set，tuple，list都行，但要满足参数的个数
    sum(x * y * z for x, y, z in [(1, 23, 4), (2, 3, 54), (346, 23, 4)])  一个例子
    
    
    filter()过滤的功能   
    filter(lambda x:x>0,range(-5,6))
    同样的代码实现
    [x for x in range(-5,6) if x>0]
    
    
    zip()函数补充
    x,y,z,a=zip([235,4,53,3],[46,4,3,53,53]) 这个是将zip生成的四个元组分别赋值给x,y,z,a
    
"""

# 类
"""
    类相关的属性以及操作等都在笔记中有记载，不在说明
"""
# 迭代器
"""
    可以迭代的对象都具有__iter__属性，当然我们也是可以自己编写一个迭代器的
    class MyRange(object):

    this is my consume iterable this class function only as for test
    dont as system function use
    
        def __init__(self, n):
            self.n = n
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.n > self.i:
                self.i += 1
                return self.i
            else:
                raise StopIteration()


    for v in MyRange(12):
        print(v)
    
"""

# 生成器
"""
    有点像列表解析
    value=(x for x in range(-234,35) if x%2==0)
    sum(x**2 for x in range(1,10))  我们没有加外边的括号 
    列表解析和生成器在编写上面 区别是 一个是[]包含，一个是()包含，但是如果只是用来实现迭代，可以不用加() sum求和就有体现
    
    定义和执行过程
    def g()
        yield 0
        yield 1
        yield 2
        
    我们将含有yield语句的函数称为生成器。生成器是一种用普通函数语法定义的迭代器
    
    yield与return的区别
    return 语句后面的语句根本不会执行
    yield会将函数运行挂起
    例子:
    def demo6(max):
        n=0
        while max>n:
            yield n
            n+=1
        else:
            StopIteration()

"""

# 上下文管理器
"""
    python中的上下文管理器必须包含__enter__()和__exit__()方法
    也就是说判断一个对象师傅可以使用上下文管理器，可以使用dir()判断函数内部是否具有上面的两种属性    
    例子
    with open("demo1.txt", "w") as f:
        f.write("sgsdhsg")
        
    自己实现的上下文管理
    class ContextManagerOpenDemo(object):
        def __init__(self, fileName, model):
            self.fileName = fileName
            self.model = model

        def __enter__(self):
            print("start execute")
            self.openfile = open(self.fileName, self.model)
            return self.openfile

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("end manager")
            self.openfile.close()


    with ContextManagerOpenDemo("file.txt", "r") as f:  # 这个as后面的就是__enter__()返回的类型
        for vale in f:
            print(vale)
        
"""

# 错误和异常
"""
    try:
    
    except Exception as e:
        pass
    finally:
        pass
    
    处理多个异常
    try:
        pass
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
        
    当然也可以这样编写
    except (ZeroDivisionError,ValueError):
        pass
    
    常常在python3.x中这样编写
    except (ZeroDivisionError,ValueError) as e:
        
    对于更多的异常
    except: 或者 except: Exception,e
    
    else子句
    try:
        pass
    except:
        pass
    else:
        print("没有发生异常")
    在没有发生异常时执行else子句，反之不执行
    
    finally:当执行发生异常过后，一定会执行的操作代码
    
    assert关键字的使用
    assert 1==1 如果当程序运行到当前代码，判断条件，如果True就会正常执行，反之抛出异常
    
    断言的应用
    1.防御性的编程
    2.运行时对程序逻辑的检测
    3.合约性检测
    4.程序中的常量
    5.检查文档
             
"""

# 模块
"""
    编写模块
    将py导入
    sys.path.append("/home/fang/python/学习python笔记/index.py") 参数是文件的路径 可以是文件亦可以是目录
    
    模块的位置
    为了使我们编写的模块能够被python解释器知道，需要通过上面的语句导入，在python中，所有的模块都被加入到了sys.path
    里面
    print(sys.path)  查看所有的模块路径
    
    PYTHONPATH环境变量
    sys.path.append()这种方式比较麻烦，通用方法是设置PYTHONPATH环境变量
    vim /etc/profile     添加下面代码   export PYTHONPATH="$PYTHONPATH:/home/fang/python"  其中/home/fang/python是我们编写python的文件夹
    source /etc/profile   立即生效
    
    "all"在模块中的作用
    对于上面的两种方式导入模块后，但是对于python中的私有变量，私有函数，等不能访问 __all__就能解决这个问题
    在我们编写的模块中添加下面代码
    __all__=['函数或变量名','函数或变量名']  这个作用是告诉本模块的解释器，这两个东西是有权被访问的,这种方法不好处是只引用了all里面的属性，方法等，其他并没有被添加 与之对应的导入方法为
    from xxx import *   (这个方法自己使用发现有问题，可能自己编写出现了问题) 
    
    包或者库
    对于一个包，就是多个模块组成的，也就是一个目录而已，如何对目录的模块进行集中的引用 解决方案是爱目录下面建立一个__init__.py文件 是一个空文件

"""
# 数据存储
"""
    pickle 用来实现数据的序列化操作
    简单的使用
    import pickle
    integers=[1,2,3,4,5,65]
    f = open("/home/fang/Desktop/22901.dat", "wb")  这里使用的后缀是dat,我尝试使用了txt,发现根本写不进去，不会报错，但是打开文件没有东西
    pickle.dump(integers,f,True) 第三个参数设置为True，可以节约存储
    f.close()
    读取文件
    f=open("/home/fang/Desktop/22901.dat","rb")
    pickle.load(f)
    [1, 2, 3, 4, 5, 65] 打印的内容
    
    对于复杂的数据结构，我们可以使用 shelve来解决问题
    s=shelve.open("/home/fang/Desktop/22901.db") 这里使用的是db类型 我们不能在使用bat,执行会保存，原因是不支持
    s["name"]="fang"
    s["age"]=12
    s["name"] == 'fang' 打印内容
    
    同样也可以对插入的类型进行添加或者修改，但是在打开文件时需要添加一个参数
    s=shelve.open("/home/fang/Desktop/22901.db",writeback=True)
    s["name"]+=" zhiyue"
    我们知道s是一个dict,所以读取里面的内容，可以使用下面的方式
    for key in s:
        print(key,s[key])
    
    mysql数据库操作
    简单的查询
    import mysql.connector
    conn = mysql.connector.connect(user="root", password="123", database="BlogTest")
    cur = conn.cursor()
    cur.execute("select id,title,content from article")
    articles = cur.fetchall()
    插入
    cur.execute("insert into article(title,content) values(%s,%s)", params=("小小芳", "你的理由很多"))
    conn.commit()
    执行多条
    cursor.executemany("insert into article(title,content) values(%s,%s)",
                   [("xiaoxia", "安全"), ("xiaoxia", "安全"), ("xiaoxia", "安全"), ("xiaoxia", "安全"), ("xiaoxia", "安全"),
                    ("xiaoxia", "安全")])
    conn.commit()
    更新操作
    cursor.execute("update article set title=%s where id=2", params=("明天"))
    cursor.fetchone()
    conn.commit()
    其他
    cursor.close
    conn.close
        
"""
