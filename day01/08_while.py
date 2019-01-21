# Author:黑猴子

age_of_heihouzi = 18

count = 0
while count < 3:
    guess_age = int(input("guess age:") )
    if guess_age == age_of_heihouzi :
        print("yes, you got it. ")
        break
    elif guess_age > age_of_heihouzi:
        print("think smaller...")
    else:
        print("think bigger!")
    count +=1
else:
    print("you have tried too many times..fuck off")

'''
往大了想，靠物质满足欲望，只能挺半年，人呢？ 还是要往精神层面想
有一句英文，意思就是说
欲望的奴隶，你以为你拥有的更多的物质，其实是物质拥有了你，你是物质的奴隶
我喜欢，我就要当奴隶，真逗了，哪些当不了奴隶的都是自我安慰
'''