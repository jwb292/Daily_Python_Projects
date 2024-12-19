# The program prompts the user to enter a sentence. Then, the program returns a message followed by the number of words in the sentence given by the user. In the last line, the program also displays the word that contains more letters in the given sentence.

sent = input("Enter a sentence for evaluation: ")

words = sent.split()

word_count = len(words)

# Find the longest word
longest_word = max(words, key=len)
length_longest_word = len(longest_word)

print("============================================================")
print("The number of words in the sentence: ",word_count)
print(f"The longest word is: {longest_word}")
print(f"The longest word is {length_longest_word} letters long")
print(" ")