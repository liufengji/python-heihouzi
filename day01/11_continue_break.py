# Author:黑猴子


#break
'''
count = 0
while True:
    print("count:",count)
    count = count +1  #count +=1
    if count == 1000:
        break
'''

#continue
'''
for i in range(0,10):
    if i <3:
        print("loop ",i)
    else :
        continue
    print("hehe...")
'''

#嵌套循环
for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j >5:
            break
