#Mary Kate Sheehan
#11/28/2023
#Lab 11 Question 1

#4 NUMBERS INSTEAD OF 7!

lst_2 = ["A", "B", "C"]
lst_3 = ["D", "E", "F"]
lst_4 = ["G", "H", "I"]
lst_5 = ["J", "K", "L"]
lst_6 = ["M", "N", "O"]
lst_7 = ["P", "R", "S"]
lst_8 = ["T", "U", "V"]
lst_9 = ["W", "X", "Y"]

def get_num_list(n):
    if n == 2:
        return lst_2
    elif n == 3:
        return lst_3
    elif n == 4:
        return lst_4
    elif n == 5:
        return lst_5
    elif n == 6:
        return lst_6
    elif n == 7:
        return lst_7
    elif n == 8:
        return lst_8
    elif n == 9:
        return lst_9
    else:
        return []

def main():
    num = input("Enter a four-digit number without 0 or 1: ")
    
    if num.isdigit() and 1000 <= int(num) <= 9999:
        string_num = str(num)

        if "0" in string_num or "1" in string_num:
            num = input("No 0's or 1's. Enter a new four-digit number: ")
        else:
            letter_combos = [get_num_list(int(digit)) for digit in string_num]
            full_letter_combos = [''.join(combos) for combos in letter_combos]
            
            print("Here are all your possible word combinations: ")
            print(full_letter_combos)


main()




