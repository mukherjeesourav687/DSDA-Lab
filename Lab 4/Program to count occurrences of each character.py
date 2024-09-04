input_string = "abcdefgabc"
char_count = {}
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in sorted(char_count.items()):
    print(f"{char},{count}")
