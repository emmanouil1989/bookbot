def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_contents_from_path(file_path)
    words_count = count_words_in_file(file_contents)
    print(file_contents)
    print(f"{num_words} words found in the document")

def read_contents_from_path(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words_in_file(file_contents):
    words = file_contents.split()
    return len(words)

main()