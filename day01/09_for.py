# Author:黑猴子

for i in range(10):
    print("loop",i)

print("--------------")
#步长 2
for i in range(0,10,2):
    print("loop",i)
print("--------------")

age_of_heihouzi = 18

for i in range(3):
    guess_age = int(input("guess age:") )
    if guess_age == age_of_heihouzi :
        print("yes, you got it. ")
        break
    elif guess_age > age_of_heihouzi:
        print("think smaller...")
    else:
        print("think bigger!")
else:
    print("you have tried too many times..fuck off")