import sys

while True:
    word = input("Please enter a word or phrase: ")
    phrase = str(word)
    count = 0
    for s in phrase:
        count = count+1

    print('What you entered is', count , 'characters long!')
    
    try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    if try_again.lower() == "n":
        sys.exit()


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
