def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letter = {}
    for c in text:
        low = c.lower()
        if low in letter:
            letter[low] += 1
        else:
            letter[low] = 1
    return letter

def sort_on(d):
    return d["num"]

def sort_num(char_count):
    sort_dat = []
    for ch in char_count:
        sort_dat.append({"char": ch, "num": char_count[ch]})
    sort_dat.sort(reverse=True, key=sort_on)
    return sort_dat