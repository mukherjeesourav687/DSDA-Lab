input_sentence = "hello world! 123"
letters = sum(c.isalpha() for c in input_sentence)
digits = sum(c.isdigit() for c in input_sentence)
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
