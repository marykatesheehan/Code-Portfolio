#function print some sentences for n times


def print_something(sent, n):
    for i in range(n):
        print(sent)

def main():
    print_something("Hello World", 10) #"Hello World" is an argument, 10 is an argument


main()


def student_info(name, age, id, college_name):
    print(name)
    if age > 18:
        print("greater than 18")
    print(id)
    if college_name == "JCU":
        print("JCU")
        
student_info("Bob", 19, 123456789, "JCU") #follow the first parameter to the last parameter listed
