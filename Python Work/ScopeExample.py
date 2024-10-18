#scope of variables:

def add(num1, num2):
    #result, num1, num2 are part from add function
    result = num1 + num2
    return result

def main():
    #x, y, k are part from main function
    #no one outside main() is going to see them
    x = 5
    y = 7
    k = add(x, y) #add(x, y) = add(5, 7) in add function add(num1 = 5, num2 = 7)
    print(x, "+", y, "=", k)

#x, y here are out of the scope of main
x = 11
y = 21
main()
