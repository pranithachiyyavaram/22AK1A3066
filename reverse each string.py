def reverse_each_word(s):
    words = s.split()
    reversed_words = ' '.join(word[::-1] for word in words)
    return reversed_words
input_string = "my name is pranitha"
result = reverse_each_word(input_string)
print(result)
