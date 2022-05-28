#ask for a text
text = input("Please enter a text: ")
#strip the text of extra spaces
stripped_text = text.strip(" ")
#split text into words
split_text = stripped_text.split(" ")
print(split_text)
#count the number of words in the list
length_of_text = len(split_text)
print("Your text has", length_of_text, "words")