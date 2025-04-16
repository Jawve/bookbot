from stats import get_book_wc
from stats import get_book_char
from stats import get_book_text
from stats import get_sort_dict
import sys
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    f = sys.argv[1] 
    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {f}...")
    print("-------- Word Count --------")
    print(f"Found {get_book_wc(get_book_text(f))} total words")
    print("-------- Character Count --------")
    get_sort_dict(get_book_char(get_book_text(f)))
    
main()
