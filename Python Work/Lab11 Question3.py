#Mary Kate Sheehan
#11/28/2023
#Lab 11 Question 3

def isAnagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        if sorted_s1 == sorted_s2:
            return True
        else:
            return False
    else:
        return False

def main():
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")

    print("The two words you picked are:", word1, "and", word2)
    print("These two are anagrams:", isAnagram(word1, word2))
        
main()
