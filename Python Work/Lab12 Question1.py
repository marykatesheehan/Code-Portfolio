#Mary Kate Sheehan
#12/5/2023
#Lab 12 Question 1

import random
numbers_dict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"8":0,"9":0,"10":0}

for i in range(100):
    num = str(random.randint(1, 10))
    if num == "1":
        numbers_dict["1"] += 1
    if num == "2":
        numbers_dict["2"] += 1
    if num == "3":
        numbers_dict["3"] += 1
    if num == "4":
        numbers_dict["4"] += 1
    if num == "5":
        numbers_dict["5"] += 1
    if num == "6":
        numbers_dict["6"] += 1
    if num == "7":
        numbers_dict["1"] += 1
    if num == "8":
        numbers_dict["1"] += 1
    if num == "9":
        numbers_dict["1"] += 1
    if num == "10":
        numbers_dict["1"] += 1

print(numbers_dict)   
    
    
