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

