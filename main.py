def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars = get_book_characters(text)
    for char in chars:  
      if char.isalpha():  
        print(f"The '{char}' character was found {chars[char]} times")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_characters(text):
    char_dict = {}
    for char in text:
      char_exists = char_dict.get(char.lower())
      if char_exists is None:
          char_dict[char.lower()] = 1
      else:
          char_dict[char.lower()] += 1
    return char_dict

main()