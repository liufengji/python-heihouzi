# Author:黑猴子

import os

# 执行命令，不保存结果
cmd_res1 = os.system("dir")
print("---->",cmd_res1)

# 可以理解为，存在内存的一个临时位置，必须读取一下，才能出来
cmd_res2 = os.popen("dir").read()
print("---->",cmd_res2)

#创建一个目录
os.mkdir("new_dir")