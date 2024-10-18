#Mary Kate Sheehan
#11/28/2023
#Lab 11 Question 2

lst = []
count = 0
letter = ""
acceptable_letters = ["a", "b", "c", "d", "e", "f"]

while count != 20:
    letter = input("Enter a letter a through f: ")
    if letter in acceptable_letters:
        lst.append(letter)
        count += 1
    else:
        print("Only enter letters a through f!")

unique_lst = list(set(lst))

ascend_lst = sorted(lst)

descend_lst = sorted(lst, reverse=True)

unique_ascend_lst = sorted(unique_lst)

print("Original List:", lst)
print("Unique List:", unique_lst)
print("Ascending List:", ascend_lst)
print("Descending List:", descend_lst)
print("Unique Ascending List:", unique_ascend_lst)

    
