#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. 
#Then you can use the in operator
#as a fast way to check whether a string is in the dictionary.

fhand = open('/Users/mamduhhalawa/Desktop/repetition/test2.txt')

dict = {}

for line in fhand:
    words = line.strip().split() 
    for word in words:
        dict[word] = None

if "is" in dict:
    print("Is is in dict")
else:
    
    print('not in dict')