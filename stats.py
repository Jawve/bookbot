def get_book_wc(f):
    wlist = f.split()
    size = len(wlist)
    return size

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_char(f):
    f = f.lower()
    char_counts = {}
    for char in f:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
    

def sort_on(dict):
    return dict["count"]
    
def get_sort_dict(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # optional: filter non-letters here
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"{item['char']}: {item['count']}")

    return char_list

