def main():
    alphabet_path = "books/alphabet.txt"
    book_path = "books/frankenstein.txt"
    alphabet = get_alphabet(alphabet_path)
    init_alphabet(alphabet)
    words_count = count_words(book_path)
    letters_book = read_book(book_path)
    count_alphas(letters_book)
    print_alpha_count(alpha_count, words_count)
    return

def get_alphabet(alphabet_path):
    with open(alphabet_path) as txt:    
        return txt.read().lower().split()
    
def count_words(book_path):
    with open(book_path) as book_txt:
        words = len(book_txt.read().split())
    return words

def read_book(book_path):
    letter_list = []
    with open(book_path) as book_txt:
        book_words = book_txt.read().lower().split()
        for word in book_words:
            for c in word:
                letter_list.append(c)
    return letter_list
    
def init_alphabet(alphabet):
    for letter in alphabet:
        alpha_count.update({letter: 0})
    return

def count_alphas(alphas):
    for alpha in alphas:
        alpha_amt = alpha_count[alpha] + 1
        alpha_count.update({alpha: alpha_amt})
    return

def print_alpha_count(alpha_count, words_count):
    for item in alpha_count:
        print(f"Amount of {item}'s in text = {alpha_count[item]}.")
    print(f"The total number of words contained within the text are: {words_count}.")

alpha_count = {}
main()