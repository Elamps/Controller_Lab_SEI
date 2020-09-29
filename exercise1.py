consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')

user_letter = input('Enter a letter: ')
letter = user_letter[0]
letter = str(letter)
letter=letter.upper()
if letter in consonant:
    print(letter,'is a consonant')
elif letter in vowel:
    print(letter,'is a vowel')

else:
    print('I dont know what',user_letter,'is!')
    
# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':