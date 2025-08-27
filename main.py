from stats import (
    get_num_words, 
    count_characters, 
    sort_num,
)

def main():   
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = count_characters(text)
    Stat_out = sort_num(char_count)
    print_report(book_path, word_count, Stat_out)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, word_count, Stat_out):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in Stat_out:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()