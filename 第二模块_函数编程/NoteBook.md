# Bytes类型

2进制——》10进制——》ASCII/GBK/UTF-8/   Unicode

数据要存到硬盘上，但是硬盘只能存储2进制，要以相应的编码转成2进制后存储，相当于上述过程反过来。

```
b'Alex  \xcc\xec\xbd\xf2\xbf\xc6\xbc\xbc\xb4\xf3\xd1\xa7'
```

就是bytes类型，以16进制形式表示，两个16进制数构成一个byte，以b来标识。

python3文件和pycharm的默认编码时UTF-8。

b binary

优势：
    
    1.字符存硬盘要变成bytes
    2.网络传输字符要变成bytes
    
# 深浅copy

dict, list, set

```python
data = {
    "name":"Alex",
    "age":"20",
    "score":{
        "离散数学":100,
        "大学物理":100,
        "概率论与数理统计":100,
    }
}

data2 = data
```

此时data2和data共享同一份数据的

```python
data3 = data.copy()
data3["name"] = "Mike"
data3["score"]["离散数学"] = 90
```

copy一份新的数据，但只是copy了第一层的浅copy

```python
import copy

data4 = copy.deepcopy(data)
data4["name"] = "Tom"
data4["score"]["离散数学"] = 80
```

完全复制一份新的数据

# 字符编码的转换

## 编码与解码

```python
s.encode("utf-8")   # 以utf-8编码成2进制

s.decode("utf-8")   # 从2进制解码称unicode
```

![](/media/alex/新加卷/PythonProject/PythonFullStack/第二模块_函数编程/images/编码与解码.png)

## 编码转换

把文字从一种编码转成另外一种

windows : gbk

linux/mac : utf-8

# 函数

## 函数的返回值

如果有多个返回值，使用逗号分割，将返回元组的形式

## 函数的作用域

## 全局变量与局部变量



```python
name = "Alex"

def change():
    name = "Coco"
    age = 19
    global name2		# 在函数的局部作用域内部声明一个全局变量（不建议使用）
    print(locals())     	# 打印所有的局部变量
    print(globals())    	# 打印所有的全局变量
    print(name, id(name))

change()
print(name, id(name))

```

```
{'name': 'Coco', 'age': 19}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fc3f4ab3e90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '全局变量与局部变量1.py', '__cached__': None, 'name': 'Alex', 'change': <function change at 0x7fc3f4a084d0>}
Coco 140479599755632
Alex 140479599755696
```

## 嵌套

函数里不仅可以写代码，还可以写其它的函数。

## 匿名

### 语法

lambda 参数列表 : 表达式

1.将创建好的匿名函数通过一个变量来去接收。

2.使用变量再去调用匿名函数。

## 高阶函数

## 递归函数

自己调用自己

## 内置函数

# 名称空间

又名namespace，就是存放名字的地方。

名称空间正是存放名字与变量绑定关系的地方。

---

名称空间有4种：LEGB

## L

locals：函数内部的名称空间，一般包括函数的局部变量以及形式参数。

## E

enclosing function：在嵌套函数中外部函数的名称空间。

## G

globals：当前的模块空间，模块就是一些py文件。

也就是说，globals()类似全局变量。

## B

\_\_builtins__：内置模块空间，也就是内置变量或者内置函数的名字空间。

---

不同变量的作用域不同就是由这个变量所在的名称空间决定的。

作用域即范围：

    全局范围：全局存活，全局有效
    
    局部范围：临时存活，局部有效
    
查看作用域方法：globals(),locals()

## 作用域查找顺序

当程序引用某个变量的名字时，就会从当前名字空间开始搜索。

搜索顺序规则便是：LEGB。

# 闭包

关于闭包，即函数定义和函数表达式位于另一个函数的函数体内（嵌套函数）。

而且，这些内部函数可以访问它们所在的外部函数中声明的所有局部变量、参数。

当其中一个这样的内部函数在包含它们的外部函数之外被调用时，就会形成闭包。

也就是说，内部函数会在外部函数返回后被执行。

而当这个内部函数执行时，它仍然必需访问其外部函数的局部变量、参数以及其它内部函数。

这些局部变量、参数和函数声明（最初时）的值时外部函数返回时的值，但也会受到内部函数的影响。

**闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外包裹了一层作用域，这使得该函数无论在何处调用，优先使用自己外层包裹的作用域。**

# 函数进阶——装饰器

软件开发中的一个原则：“开放——封闭”原则：

    封闭：已实现的功能代码块不应该被修改
    
    开放：对现有功能的扩展开放
   
# 列表生成式

# 生成器 generator

## 函数生成器

# 迭代器

# 模块

## 模块介绍与引入

### 什么是模块

为了编写可维护的代码，把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少。

很多编程语言都采用这种组织代码的方式，在python中,一个.py文件就可以称之为一个模块(Model)。

### 模块的好处

1.提高了代码的可维护性

2.模块可以被其它地方引用

3.模块可以避免函数名和变量名冲突

### 模块的分类

#### 标准内置模块

#### 第三方模块

#### 自定义模块

### 模块的导入

```python
import module

from module import function

from bag.module import function
```

**注意：模块一旦被调用，即相当于执行了另一个py文件里的代码。**

### 模块查找路径

```python
import sys

sys.path
```

```python
[
'',    # 代表当前目录
'/media/alex/新加卷/PythonProject/PythonFullStack/environment/lib/python37.zip', 
'/media/alex/新加卷/PythonProject/PythonFullStack/ement/lib/python3.7',    # 标准内置模块
'/media/alex/新加卷/PythonProject/PythonFullStack/environment/lib/python3.7/lib-dynload', 
'/media/alex/新加卷/Pythont/PythonFullStack/environment/lib/python3.7/site-packages'   # 第三方模块
]
```

## 第3方开源模块的安装使用

https://pypi.org/

### 源码编译安装

从官网上下载源码，解压并进入目录，执行以下命令：

```python
编译源码：python setup.py bulid

安装源码：python setup.py install
```

### 直接通过pip安装



## 系统调用os模块



## 系统调用sys模块



## time &  datetime模块

时间处理模块：

    1.时间的显示：在屏幕显示、记录日志等
    
    2.时间的转换：
    
    3.时间的运算：计算两个日期的差值等

### time模块

python中时间的表示方式：

    1.时间戳(timestamp)，表示的是从1970年1月1日00:00:00开始按妙计算的偏移量
    
    2.格式化的时间字符串
    
    3.元组(struct_time)用九个元素表示时间

#### UTC时间

UTC亦即格林威治天文时间，世界标准时间。

在中国为UTC+8，又称东8区。

#### time模块的各种方法

time.localtime

#### datetime模块



## random随机模块



## 序列化pickle&json模块



## hashlib加密

Hash，一般翻译作“散列”，就是把任意长度的输入（又叫做预映射，pre-image），通过散列算法，变换称固定长度的输出，该输出就是散列值。

这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，而不是从散列值来唯一的确定输入值。

简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。

### MD5

#### 什么是MD5算法

MD5讯息摘要演算法(MD5 Message-Digest Algorithm)，一种被广泛使用的密码杂凑函数，可以产出一个128位的散列值(hash value)，用于确保信息传输完整一致。

#### MD5功能

输入任意长度的信息，经过处理，输出为128位的信息（数字指纹）

不同的输入得到的不同的结果

#### MD5算法的特点

1.压缩性：任意长度的数据，算出的MD5值的长度都是固定的

2.容易计算：从原数据计算出MD5的值很容易

3.抗修改性：对原数据进行任何改动，修改一个字节生成的MD5值区别也会很大

4.强抗碰撞：已知原数据和MD5，想找到一个具有相同的MD5值的数据是非常困难的

#### MD5算法是否可逆？

MD5不可逆的原因是其是一种散列函数，使用的是hash算法，在计算过程中原文的部分信息是丢失了的。

#### MD5用途

1.防止被篡改

2.防止直接看到明文

3.防止抵赖

## 文件copy模块shutil

## 正则表达式re模块

## 软件开发目录设计规范

## 包&模块代码调用