from collections import Counter

def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_characters(text):
  text = text.lower()
  counter = Counter(c for c in text if c.isalpha())
  return counter.most_common()