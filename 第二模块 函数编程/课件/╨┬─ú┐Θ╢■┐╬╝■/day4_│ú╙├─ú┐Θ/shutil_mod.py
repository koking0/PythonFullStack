
import shutil
import os
#shutil.copyfileobj(open("json_mod.py"),open("json2_mod.py","w"))

#shutil.copyfile("json_mod.py","json3_mod.py")


#shutil.copymode("time_mod.py","json3_mod.py")
#shutil.copystat("time_mod.py","json3_mod.py")

#shutil.copy("time_mod.py","time2_mod.py")

#shutil.copy2("time_mod.py","time3_mod.py")

#shutil.copytree("../day4_常用模块","day4_代码",ignore=shutil.ignore_patterns("__init__.py","result.*"))

# shutil.make_archive(base_name="/Users/alex/Downloads/day4_code",
#                     format="zip",root_dir="../",
#                     owner="root")


import zipfile
#
# z = zipfile.ZipFile("test_compress.zip","w")
# z.write("os_mod.py")
# z.write("pickle_load.py")
#
# filelist = []
# for root_dir ,dirs, files in os.walk("备课用/my_proj"):
#     for filename in files:
#         filelist.append( os.path.join(root_dir,filename) )
#
# for i in filelist:
#     print(i)
#     z.write(i)
#
# z.close()

z = zipfile.ZipFile('test_compress.zip', 'r')
z.extractall(path='/Users/alex/Documents/tt')

z.close()