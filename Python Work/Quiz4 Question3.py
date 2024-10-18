#Mary Kate Sheehan
#11/6/2023
#Quiz 4 Question 3

def shout(sentence):
    count = 0
    while count != 5:
        print(sentence)
        count = count + 1

def main():
    sentence = input("Enter a random sentence: ")
    shout(sentence)

main()
