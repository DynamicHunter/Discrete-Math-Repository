# Notes 1/30
"""
Two main data structures used in this class:
1. Sets - unordered, items can appear at maximum once. In other words, no duplicates.
    You can't directly access elements/items in a set, you need to loop through the
    set to access it.
    Set uses curly braces" {}
2. Lists - you can have duplicates, and it is ordered.
    You can directly access elements/items in a list, you just need to indicate the index.
    List uses brackets: []
"""

setExample = {"a", "b", "c"}
# It knows setExample is a set because of the curly braces
listExample = ["a", "b", "c"]
setExample2 = {"c", "b", "a"}
listExample2 = ["c", "b", "a"]

setExample3 = {"c", "b", "a", "c"} # it just removes the duplicate "c"
print setExample
print listExample
print setExample2
print listExample2
print setExample3

for x in setExample3:
    print x

print "d" in setExample3 # Prints yes/no if "d" is in setExample3

print listExample[-1]
print "Length of setExample3:", len(setExample3)

"""
Python Comprehension: An expression that lets you build a collection from other collections
"Collection" refers to a grouping of items (such as a set or a list)
"""

# TODO - Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of the squares of each integer
# comprehension - iterating over the list elements
print {x*x for x in {1, 2, 3, 4, 5}} # This is FUCKED !

print [x*x for x in [1, 2, 3, 4, 5]]

print [x*x for x in {1, 2, 3, 4, 5}]

# TODO - Write a comprehension over {0, 1, 2, 3, 4} whose value is the set consisting of the first five powers starting
# at 2^0

print [2 ** x for x in {0, 1, 2, 3, 4}]

# TODO - The value of the previous comprehension, {x * y for x in {1, 2, 3} for y in {2, 3, 4}}
# is a seven element set. Replace {1, 2, 3} and {2, 3, 4} with two other 3 element sets so that the
# value becomes a 9 element set
print {x * y for x in {1, 2, 3} for y in {2, 3, 4}} # OG
print {x * y for x in {1, 2, 3} for y in {5, 7, 11}} # MINE

L = [1, 2, 3]
M = {2, 3, 4}
print sum(L)
print sum(M)
