def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    converted_chars_dict = convert_chars_dict(chars_dict)
    sorted_chars_dict = sort_converted_chars_dict(converted_chars_dict)
    sorted_master_dict = convert_back_to_dict(sorted_chars_dict)
    print_book_stats(book_path, sorted_master_dict, num_words)

# This function extracts the text out of the document stored in the location 
# indicated in the "path" variable.
def get_book_text(path):
    with open(path) as f:
        return f.read()

# This function gets the total number of words within the text.
def get_num_words(text):
    words = text.split()
    return len(words)

# This function iterates over the individual characters within the text, removes any punctuation, 
# counts and then pairs them within a dictionary with their respective counts.
def get_chars_dict(text):
    chars={}
    for c in text:
        if c.isalpha() == True:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

# This function will convert the 'chars_dict' dictionary into a list of dictionaries,
# applying keys to the character value and the count value ex {"Char": "a", "Count": 133412}.
# This is necessary to apply the sorting functions which follow...  It will be converted
# back into a normal dictionary with another function.
def convert_chars_dict(chars_dict):
    dict_list = []
    for c in chars_dict:
        ds = {"Char": c ,"Count" : chars_dict[c]}
        dict_list.append(ds)
    return dict_list

# This function is referred to by the sort function below - it is needed for it to work properly.
def sort_on(dict):
    return dict["Count"]

# This function does the actual sorting - take note of the key=sort_on - this refers to the function
# above to work properly.
def sort_converted_chars_dict(converted_chars_dict):
    converted_chars_dict.sort(reverse=True, key=sort_on)
    return converted_chars_dict

# This function converts the sorted characters dictionary (the one with "Char" and "Count" pairs)
# back into a normal dictionary with the contents actually in order.
def convert_back_to_dict(sorted_chars_dict):
    sorted_master_dict = {}
    for x in sorted_chars_dict:
        sorted_master_dict.update({x['Char']: x['Count']})
    return sorted_master_dict

#This function generates the final report.
def print_book_stats(book_path, sorted_master_dict, num_words):
    print(f"========== Begin report of '{book_path}' ==========")
    print(f"{num_words} words were found in the document...")
    for item in sorted_master_dict:
        print(f"The '{item}' character was found {sorted_master_dict[item]} times...")
    print("==================== End Report ====================")
    return

main()