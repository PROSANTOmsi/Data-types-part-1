# Data-types-part-1.py

#list = []
fruits = ["mango", "apple", "banana", "orange"]

print(fruits) 
#or to print a specific index 
print(fruits[2]) 
#or to print a amount of indexes
print(fruits[0:2]) 
#or to print a index and skip another index and print another index
print(fruits[::2]) 
#or to print them in reverse
print(fruits[::-1]) 
#or to replace any index or value of the fruits variable type
fruits[0] = "pineapple"
#or you can also add an element
fruits.append("guava") 
#or to remove
fruits.remove("apple")
#or to add an element at a specific index
fruits.insert(1, "rasberry") 
#or you can also arrange in assending order
fruits.sort()
#or you can also do it in reverse order but it will arrange randomly
fruits.reverse()
#or you can also arrange them in order by 
fruits.sort(reverse = true)
#to clear a list
fruits.clear()
#to find out an specific index
print(fruits.index(0))
#to count any element 
print(fruits.count("banana"))
#you can also pop out a random value
fruits.pop()

#tuple {}
#we can add and remove elements of a tuple but we cannot change a value

fishes = {"salmon", "tuna", "sardines"}
#to add 
fishes.add("pufferfish")
#to remove
fishes.remove("tuna")
#we cannot change any element
fishes[0] = "rockfish"
you can also pop out random value
fishes.pop()
#to clear
fishes.clear()
#you cannot duplicate
fishes.add("tuna")

#tuple ()
#tuple are unchangeable and works FASTER
#well there are only two operators we can use on tuple

games = ("call of duty", "ghost of tushima", "asplahalt 8 airborne")
#count
games.count("ghost of tushima")
#index
games.index("asplahalt 8 airborne")
