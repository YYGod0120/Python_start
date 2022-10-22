'''
import os
得到当前⼯作⽬录，即当前Python脚本⼯作的⽬录路径: os.getcwd()
返回指定⽬录下的所有⽂件和⽬录名:os.listdir()
函数⽤来删除⼀个⽂件:os.remove()
删除多个⽬录：os.removedirs（r“c：\python”）
检验给出的路径是否是⼀个⽂件：os.path.isfile()
检验给出的路径是否是⼀个⽬录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否真地存:os.path.exists()
返回⼀个路径的⽬录名和⽂件名:os.path.split()
获取路径名：os.path.dirname()
获得绝对路径: os.path.abspath()
获取⽂件名：os.path.basename()
运⾏shell命令: os.system()
重命名：os.rename（old,new）
创建多级⽬录：os.makedirs（r“c：\python\test”）
创建单个⽬录：os.mkdir（“test”）
获取⽂件属性：os.stat（file）

import sys
sys.path 获取系统环境变量
sys.argv 获取脚本参数


'''
import sys
print(sys.path)