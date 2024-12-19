# This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.


text = "Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber."

# counter set to zero
lowerCase = 0
upperCase = 0

# for loop to cycle through the letters
for letters in text:
    if letters.isupper():
        upperCase += 1
    elif letters.islower():
        lowerCase += 1

totalLetters = lowerCase + upperCase

# print statements for upper and lower case letters
print("The number of uppercase letters is: ", upperCase)
print("The number of lowercase letters is: ", lowerCase)
print("Total amount of letters is: ", totalLetters)