# Input
input_sequence = "without,hello,bag,world"
words = input_sequence.split(',')
sorted_words = sorted(words)
output_sequence = ','.join(sorted_words)
print(output_sequence)
