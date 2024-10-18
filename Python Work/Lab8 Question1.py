#Mary Kate Sheehan
#10/31/2023
#Lab 8 Question 1


def all_same(x,y,z):
    if x == y and x == z and y == z:
        return True
    else:
        return False

def all_different(x,y,z):
    if x != y and x != z and y!= z:
        return True
    else:
        return False

def sorted(x,y,z):
    if x < y and y < z and z > x:
        return True
    else:
        return False

print("True Statements Tested:")
print("All the numbers are the same:", all_same(7,7,7))
print("All the numbers are different:", all_different(8,9,11))
print("All the numbers are sorted from smallest to largest:", sorted(10,13,15))


print("-------------------------------------------------------------------------------")


print("False Statements Tested:")
print("All the numbers are the same:", all_same(7,9,7))
print("All the numbers are different:", all_different(8,8,8))
print("All the numbers are sorted from smallest to largest:", sorted(14,13,12))
