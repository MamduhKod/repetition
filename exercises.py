#Exercise 1:
# Write a function called chop that takes a list and modifies it,
# removing the first and last elements,
# and returns None. Then write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.

list = [1,3,6,98,3]
def chop(l):
    remove = l[1:-1]
    return remove

print(chop(list))


# Exercise 2:
# Rewrite the guardian code in the below example without 
# two if statements. 
# Instead, use a compound logical expression using 
# the or logical operator with a single if statement.
#fhand = open('mbox-short.txt') 
# count = 0
#for line in fhand:
#words = line.split()
# print('Debug:', words)
#if len(words) == 0 : continue
#if words[0] != 'From' : continue print(words[2])

fhand = open('mbox-short.txt') 
count = 0
for line in fhand:
 words = line.split()
 print('Debug:', words)
 if len(words) == 0 and words[0] != 'From':
  print(words[2])
