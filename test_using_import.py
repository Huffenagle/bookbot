import string

def main():
    alphabet_path = "books/alphabet.txt"
    #book_path = "books/frankenstein.txt"
    test_path = "books/test.txt"
    alphabet = get_alphabet(alphabet_path)
    test_book = read_book(test_path)
    init_alphabet(alphabet)
    #print(f"TEST BOOK: {test_book}")
    #print(f"ALPHABET: {alphabet}")
    count_alphas(test_book)
    print(f"ALPHABET COUNT: {alpha_count}")
    #book_words = read_book(book_path)
    return

def get_alphabet(alphabet_path):
    with open(alphabet_path) as txt:    
        return txt.read().lower().split()

def read_book(book_path):
    letter_list = []
    with open(book_path) as book_txt:
        book_words = book_txt.read()
        print(f"BOOK WORDS: {book_words}")
        print(string.punctuation)
        new_words = book_words.translate(str.maketrans("", "", string.punctuation))
        book_words = new_words.lower()
        book_words = book_words.split()
        for word in book_words:
            for c in word:
                letter_list.append(c)
    print(f"LETTERS IN BOOK: {letter_list}")
    return letter_list
    
def init_alphabet(alphabet):
    for letter in alphabet:
        alpha_count.update({letter: 0})
    return alpha_count

def count_alphas(alphas):
    for alpha in alphas:
        alpha_amt = alpha_count[alpha] + 1
        #print(alpha)
        alpha_count.update({alpha: alpha_amt})
    return alpha_count

alpha_count = {}
main()