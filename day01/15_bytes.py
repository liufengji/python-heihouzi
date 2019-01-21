# Author:黑猴子

msg = "我爱黑猴子的家"
print(msg)

#转成二进制
print(msg.encode(encoding="utf-8"))

#转成文本字符串
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))