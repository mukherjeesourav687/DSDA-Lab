# I. Reverse a string
def reverse_string(s):
    return s[::-1]

# II. Check if palindrome
def is_palindrome(s):
    return s == s[::-1]

# III. Check if ends with a specific substring
def ends_with(s, substring):
    return s.endswith(substring)

# IV. Capitalize the first letter of each word
def capitalize_words(s):
    return s.title()

# V. Check if a string is an anagram of another
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# VI. Remove vowels from string
def remove_vowels(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

# VII. Find length of the longest word in a sentence
def longest_word_length(s):
    words = s.split()
    return len(max(words, key=len))

# Example usage:
string = "A man a plan a canal Panama"
print("Reversed:", reverse_string(string))
print("Is palindrome:", is_palindrome(string.replace(" ", "").lower()))
print("Ends with 'Panama':", ends_with(string, "Panama"))
print("Capitalized words:", capitalize_words(string))
print("Anagram check with 'amanaPlanacanalPanama':", is_anagram(string.replace(" ", "").lower(), "amanaPlanacanalPanama"))
print("Without vowels:", remove_vowels(string))
print("Longest word length:", longest_word_length(string))
