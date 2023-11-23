from collections import Counter
text = """
This is a sample text. It contains some words , and some words are repeated. 
The goal is to calculate the frequency distribution of words in this text.
"""
text = text.lower()
words = text.split()
freq = Counter(words)
print("Word Frequency Distribution:")
for word, frequency in freq.items():
print(f"{word}: {frequency}")
