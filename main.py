from stats import *
import sys

def get_book_text(book_path):
  with open(book_path, 'r', encoding='utf-8') as file:
    return file.read()
  
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  book_text = get_book_text(sys.argv[1])
  num_words = get_num_words(book_text)
  print(f'Found {num_words} total words')
  print("--------- Character Count -------")
  for char, freq in get_num_characters(book_text):
    print(f'{char}: {freq}')