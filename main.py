def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_contents_from_path(file_path)
    num_words = count_words_in_file(file_contents)
    characters_count = count_characters_in_file(file_contents)
    print(file_contents)
    print(f"{num_words} words found in the document")
    print(characters_count)
    

def read_contents_from_path(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words_in_file(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters_in_file(file_contents):
    count_dictionary = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in count_dictionary:
            count_dictionary[lower_char] += 1
        else:
            count_dictionary[lower_char] = 1
    return count_dictionary
             

main()