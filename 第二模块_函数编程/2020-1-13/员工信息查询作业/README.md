# 程序的实现的功能

一个简单的员⼯信息增删改查程序

# 程序的启动方式

python3 code.py

# 流程

1.以字典的形式读入并存储文件内容在内存中

2.对用户输入的命令进行解析，分析出是增删改查中的哪条命令

    （1）增
        
        以add为开头，然后紧接一个空格，随后是staff_table和一个空格，再之后就是员工信息，分别是员⼯名称、员⼯年龄、员⼯⼿机号、员⼯部⻔、员⼯⼊职时间
    
    （2）删
    
        以del为开头，最后是以id = ?的形式输入要删除员工的序号
    
    （3）改
    
        以update为开头，要修改的信息为以set开头，其后是信息名称，被修改人的信息为以where开头，其后是信息名称
    
    （4）查
    
        以find为开头，其后接要输出的信息，如果是*表示全部输出，最后是查询信息，筛选信息+筛选标准
    
3.实现增删改查相应的模块

首先分割字符串，获得第一个单词确定增删改查

    （1）增
    
        将staff_table后的信息以逗号为分割，获得手机号，判断手机号是否在员工信息内，如果存在则报错，如果不存在则存入员工信息
    
    （2）删
    
        获得要删除的员工id，在员工信息内删除该员工
    
    （3）改
    
        分割命令获得要修改的信息，在员工信息内更改该信息
    
    （4）查
    
        分割字符串获得筛选信息，在员工信息内筛选
        
# 程序运行效果

```
Welcome to the employee information inquiry program！


1	Alex Li		22	13651054608	IT				2013-04-01	
2	Jack Wang	28	13451024608	HR				2015-01-07	
3	Rain Wang	21	13451054608	IT				2017-04-01	
4	Mack Qiao	44	15653354208	Sales			2016-02-01	
5	Rachel Chen	23	13351024606	IT				2013-03-16	
6	Eric Liu	19	18531054602	Marketing		2012-12-01	
7	Chao Zhang	21	13235324334	Administration	2011-08-08	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	
9	Shit Wen	20	13351024602	IT				2017-07-03	
10	Shanshan Du	26	13698424612	Operation		2017-07-02	

Please input command (q to quit): find name,age from staff_table where age > 22
Jack Wang	28	
Mack Qiao	44	
Rachel Chen	23	
Shanshan Du	26	

Please input command (q to quit): find * from staff_table where dept = "IT"
1	Alex Li		22	13651054608	IT				2013-04-01	
3	Rain Wang	21	13451054608	IT				2017-04-01	
5	Rachel Chen	23	13351024606	IT				2013-03-16	
9	Shit Wen	20	13351024602	IT				2017-07-03	

Please input command (q to quit): find * from staff_table where enroll_date like "2013"
1	Alex Li		22	13651054608	IT				2013-04-01	
5	Rachel Chen	23	13351024606	IT				2013-03-16	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	

Please input command (q to quit): add staff_table Mosson,18,13678789527,IT,2018-12-11
1	Alex Li		22	13651054608	IT				2013-04-01	
2	Jack Wang	28	13451024608	HR				2015-01-07	
3	Rain Wang	21	13451054608	IT				2017-04-01	
4	Mack Qiao	44	15653354208	Sales			2016-02-01	
5	Rachel Chen	23	13351024606	IT				2013-03-16	
6	Eric Liu	19	18531054602	Marketing		2012-12-01	
7	Chao Zhang	21	13235324334	Administration	2011-08-08	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	
9	Shit Wen	20	13351024602	IT				2017-07-03	
10	Shanshan Du	26	13698424612	Operation		2017-07-02	
11	Mosson		18	13678789527	IT				2018-12-11	

Please input command (q to quit): del from staff_table where id = 10
1	Alex Li		22	13651054608	IT				2013-04-01	
2	Jack Wang	28	13451024608	HR				2015-01-07	
3	Rain Wang	21	13451054608	IT				2017-04-01	
4	Mack Qiao	44	15653354208	Sales			2016-02-01	
5	Rachel Chen	23	13351024606	IT				2013-03-16	
6	Eric Liu	19	18531054602	Marketing		2012-12-01	
7	Chao Zhang	21	13235324334	Administration	2011-08-08	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	
9	Shit Wen	20	13351024602	IT				2017-07-03	
10	Mosson		18	13678789527	IT				2018-12-11	

Please input command (q to quit): update staff_table set dept="Market" where dept = "IT"
1	Alex Li		22	13651054608	Market			2013-04-01	
2	Jack Wang	28	13451024608	HR				2015-01-07	
3	Rain Wang	21	13451054608	Market			2017-04-01	
4	Mack Qiao	44	15653354208	Sales			2016-02-01	
5	Rachel Chen	23	13351024606	Market			2013-03-16	
6	Eric Liu	19	18531054602	Marketing		2012-12-01	
7	Chao Zhang	21	13235324334	Administration	2011-08-08	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	
9	Shit Wen	20	13351024602	Market			2017-07-03	
10	Mosson		18	13678789527	Market			2018-12-11	

Please input command (q to quit): update staff_table set age=25 where name = "Alex Li"
1	Alex Li		25	13651054608	Market			2013-04-01	
2	Jack Wang	28	13451024608	HR				2015-01-07	
3	Rain Wang	21	13451054608	Market			2017-04-01	
4	Mack Qiao	44	15653354208	Sales			2016-02-01	
5	Rachel Chen	23	13351024606	Market			2013-03-16	
6	Eric Liu	19	18531054602	Marketing		2012-12-01	
7	Chao Zhang	21	13235324334	Administration	2011-08-08	
8	Kevin Chen	22	13151054603	Sales			2013-04-01	
9	Shit Wen	20	13351024602	Market			2017-07-03	
10	Mosson		18	13678789527	Market			2018-12-11	

Please input command (q to quit): q

Process finished with exit code 0

```