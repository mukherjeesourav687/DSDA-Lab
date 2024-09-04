input_string = "hello world and practice makes perfect and hello world again"
words = input_string.split()
unique_sorted_words = sorted(set(words))
output_string = ' '.join(unique_sorted_words)
print(output_string)
