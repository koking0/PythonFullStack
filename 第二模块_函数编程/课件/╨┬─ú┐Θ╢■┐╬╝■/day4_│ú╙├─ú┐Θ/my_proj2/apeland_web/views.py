import sys

# import os
# #base_dir = "xxxxxxxxxxxx/my_proj2"
# base_dir = os.path.abspath(os.path.dirname(os.path.dirname( __file__) ))
# print("file:::",base_dir)
#
# sys.path.append(base_dir)

from my_proj import settings

def home_page():
    print("welcome to Apeland...")
    print(settings.DATABASES)

home_page()


