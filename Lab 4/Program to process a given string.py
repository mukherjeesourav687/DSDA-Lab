# Input string
text = "India is my motherland. I love my country. Capital of India is New Delhi."

# Length of the string
length = len(text)
print("Length of the string:", length)

# Finding substring 'country'
if "country" in text:
    print("The substring 'country' is found in the string.")

# Counting occurrences of each word
import re
words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Occurrences of each word:")
for word, count in word_count.items():
    print(f"{word}: {count}")
