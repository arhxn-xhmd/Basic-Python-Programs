# Secret Code Language

import random
import string

user_choice = int(input("You want to code or decode\n\nPress 1 to code\nPress 2 to decode\n\n>>> "))

if (user_choice == 1):
    coding = input("\nEnter the information you want to code : ")
    list = coding.split(" ")
    for i in range(0, len(list)):
        lists = list[i]
        rndm_words1 = ''.join(random.choice(string.ascii_letters.lower()) for i in range(3))
        rndm_words2 = ''.join(random.choice(string.ascii_letters.lower()) for i in range(3))
        if (lists == "A" or lists == "a") :
            print(1,end='*_*')
        elif (lists == "I") :
            print(9,end='*_*')
        elif(len(lists) == 2 or  len(lists) == 3):
            print(lists[::-1],end='*_*') 
        else :
            print(rndm_words1+lists[1:]+lists[0]+rndm_words2,end='*_*')

elif (user_choice == 2) :    
    matter = input("Enter the matter you want to decode : ")
    list = matter.split("*_*")
    for i in range(0, len(list)):
        lists = list[i]
        if (lists == "1") :
            print("a",end=' ')
        elif (lists == "9") :
            print("I",end=' ')
        elif (len(lists) <= 3) :
            print(lists[::-1],end=' ')
        elif (len(lists) > 3) :
            print(lists[-4]+lists[3:-4],end=' ')   
            
else :
    print("Kindly enter a valid number")