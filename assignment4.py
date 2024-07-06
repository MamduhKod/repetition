user_text = input('Input any sentence here.')

#Print the amount of characters
n_of_characters = len(user_text)
print('The amount of characters are', n_of_characters)

#Print the amount of words
word_list =user_text.split()
n_of_words = len(word_list)
print('There are ', n_of_words, 'words in the user input.')


vowels = ['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


vowel_count = 0
consonant_count = 0

for word in word_list:
    for character in word:
        if character in vowels:
            vowel_count +=1
        else:
            consonant_count += 1
print(f'The amount of consonants here are {consonant_count} and the amount of vowels are {vowel_count}')
            
            
        
            
    
    
    

    