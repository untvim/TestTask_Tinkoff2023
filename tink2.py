s = input()
word = "sheriff"
letter_counts = {letter: 0 for letter in word}
for letter in s:
    if letter in letter_counts:
        letter_counts[letter] += 1
max_word_count = min(letter_counts.values())
print(max_word_count)