#Mary Kate SHeehan
#10/6/2023
#Quiz #2, Question #1

females = eval(input("How many females are registed in a class?"))
males = eval(input("How many males are registered in a class?"))

total= females + males
percent_females = round((females / total) * 100, 0)
percent_males = round((males / total) * 100, 0)

print("The class is registered of", percent_females, "percent females and", percent_males, "percent males.")
