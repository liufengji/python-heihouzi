# Author:黑猴子

age_of_heihouzi = 18

count = 0
while count <3:
    guess_age = int(input("guess age:") )
    if guess_age == age_of_heihouzi :
        print("yes, you got it. ")
        break
    elif guess_age > age_of_heihouzi:
        print("think smaller...")
    else:
        print("think bigger!")
    count +=1
    if count == 3:
        countine_confirm = input("do you want to keep guessing..?")
        if countine_confirm != 'n':
            count =0