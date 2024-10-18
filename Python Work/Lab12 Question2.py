#Mary Kate Sheehan
#12/5/2023
#Lab 12 Question 2


capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
'Arizona':'Phoenix', 'Arkansas':'Little Rock',
'California':'Sacramento', 'Colorado':'Denver',
'Connecticut':'Hartford', 'Delaware':'Dover',
'Florida':'Tallahassee', 'Georgia':'Atlanta',
'Hawaii':'Honolulu', 'Idaho':'Boise',
'Illinois':'Springfield', 'Indiana':'Indianapolis',
'Iowa':'Des Moines', 'Kansas':'Topeka',
'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
'Maine':'Augusta', 'Maryland':'Annapolis',
'Massachusetts':'Boston', 'Michigan':'Lansing',
'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
'Missouri':'Jefferson City', 'Montana':'Helena',
'Nebraska':'Lincoln', 'Nevada':'Carson City',
'New Hampshire':'Concord', 'New Jersey':'Trenton',
'New Mexico':'Santa Fe', 'New York':'Albany',
'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
'Rhode Island':'Providence', 'South Carolina':'Columbia',
'South Dakota':'Pierre', 'Tennessee':'Nashville',
'Texas':'Austin', 'Utah':'Salt Lake City',
'Vermont':'Montpelier', 'Virginia':'Richmond',
'Washington':'Olympia', 'West Virginia':'Charleston',
'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}


correct_count = 0
incorrect_count = 0
quiz_continue = "yes"

print("Today, you will be quizzed on how well you know your state capitals.")
while quiz_continue == "yes":
    state, capital = capitals.popitem()
    answer = input("What is the capital of "+state+": ")
    if answer == capital:
        correct_count += 1
        print("Correct!")
    else:
        incorrect_count += 1
        print("Incorrect! The capital was", capital)
    quiz_continue = input("Do you wish to continue? Enter yes or no: ")

print("You got a total of", correct_count, "correct.")
print("You got a total of", incorrect_count, "incorrect.")
    

    
        
    
