def get_num_words():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(f"{len(words)} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
