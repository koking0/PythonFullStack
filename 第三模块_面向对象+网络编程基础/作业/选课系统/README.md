# 基础需求：85%

角色：学员、讲师、管理员

## 需求分析:

1. 创建北京、上海 2 所学校

2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

3. 课程包含，周期，价格，通过学校创建课程
 
4. 通过学校创建班级， 班级关联课程、讲师

5. 创建学员时，选择学校，关联班级

5. 创建讲师角色时要关联学校

6. 提供三个角色接口

    6.1 学员视图， 可以注册， 交学费， 选择班级

    6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩

    6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里

|名称|属性|方法|
|---|---|---|
|学校|地点、课程|创建班级|
|课程|名称、价格、周期|显示当前课程学生|
|讲师|姓名、年龄、性别、ID(202001??)、密码、学校、课程|管理班级、上课时选择班级、查看班级学员列表、学员打分|
|学员|姓名、年龄、性别、ID(202010??)、密码、学校、班级、课程|注册、缴费、选课|
|管理员|姓名、年龄、性别、ID(202000??)、密码|创建学校、创建班级、创建课程、创建老师|



# 程序运行效果

```

			总菜单
		1.老师登录
		2.学生登录
		3.学生注册
		4.管理员登录
		5.退出

Please input (1,2,3,4) to select login or register: 4
Please input Manager id: 0001
Please input Manager password: 0001
Manager Run
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 1
Please input course's name: python
Please input course's price: 12999
Please input course's cycle: 6
Please input course's place: 北京
Please input course's teacher: alex
python create successful!
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 1
Please input course's name: linux
Please input course's price: 6999
Please input course's cycle: 6
Please input course's place: 北京
Please input course's teacher: alex
linux create successful!
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 1
Please input course's name: go
Please input course's price: 4999
Please input course's cycle: 4
Please input course's place: 上海
Please input course's teacher: egon
go create successful!
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 2
Please input teacher's name: alex
Please input teacher's age: 28
Please input teacher's sex: female
Please input teacher's id: 0101
Please input teacher's password: 0101
alex create successful!
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 2
Please input teacher's name: peiqi
Please input teacher's age: 38
Please input teacher's sex: female
Please input teacher's id: 0102
Please input teacher's password: 0102
peiqi create successful!
管理员菜单：
1 创建课程
2 创建老师
3 退出
Please input order: 3

			总菜单
		1.老师登录
		2.学生登录
		3.学生注册
		4.管理员登录
		5.退出

Please input (1,2,3,4) to select login or register: 3
Please input student's name: alex
Please input student's age: 18
Please input student's sex: female
Please input student's(must start with 10) id: 1001
Please input student's password: 1001
Student Run
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 1
课程名		价格		周期
python		12999		6
linux		6999		6
go			4999		4
Please input course name (quit to exit): python
Please enter ID for payment: 1001
Please enter password for payment: 1001
Successful payment!
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 1
课程名		价格		周期
python		12999		6
linux		6999		6
go			4999		4
Please input course name (quit to exit): linux
Please enter ID for payment: 1001
Please enter password for payment: 1001
Successful payment!
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 2
python 6 个月  北京 ['alex']
linux 6 个月  北京 ['alex']
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 3

			总菜单
		1.老师登录
		2.学生登录
		3.学生注册
		4.管理员登录
		5.退出

Please input (1,2,3,4) to select login or register: 2
Please input Student id: 1001
Please input Student password: 1001
Student Run
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 2
python 6 个月  北京 ['alex']
linux 6 个月  北京 ['alex']
学员菜单：
1 选择课程
2 显示课程
3 退出
Please input order: 3

			总菜单
		1.老师登录
		2.学生登录
		3.学生注册
		4.管理员登录
		5.退出

Please input (1,2,3,4) to select login or register: 1
Please input Teacher id: 0101
Please input Teacher password: 0101
Teacher Run
讲师菜单：
1 学员列表
2 学员打分
3 退出
Please input order: 1
学员列表:
alex
alex
讲师菜单：
1 学员列表
2 学员打分
3 退出
Please input order: 2
学员列表:
alex
alex
学员打分:
Please enter the student ID to be scored: 1001
Please input score: 100
Student not found！
讲师菜单：
1 学员列表
2 学员打分
3 退出
Please input order: 3

			总菜单
		1.老师登录
		2.学生登录
		3.学生注册
		4.管理员登录
		5.退出

Please input (1,2,3,4) to select login or register: 5

Process finished with exit code 0
```