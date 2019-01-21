# Author:黑猴子

import sys

# 打印环境变量
print(sys.path)
# 打印当前脚本的相对路径
print(sys.argv)

# 传入参数
# cmd -> python -> python 12_sys_mode.py 1 2 3
#print(sys.argv[2])
print(sys.path[2])

'''
[
'E:\\workspace\\python\\sk14\\day01', 
'E:\\workspace\\python\\sk14', 
'C:\\myanzhuang\\python\\python3.7\\python37.zip', 
'C:\\myanzhuang\\python\\python3.7\\DLLs', 
'C:\\myanzhuang\\python\\python3.7\\lib', 
'C:\\myanzhuang\\python\\python3.7', 
'C:\\myanzhuang\\python\\python3.7\\lib\\site-packages'
]
'''
'''
第三方库地址
C:\\myanzhuang\\python\\python3.7\\lib\\site-packages'
标准库地址
C:\\myanzhuang\\python\\python3.7\\lib
sys.py
C:\myanzhuang\PyCharm Community Edition 2017.1\helpers\python-skeletons
'''
