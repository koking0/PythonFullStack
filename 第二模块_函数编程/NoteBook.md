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