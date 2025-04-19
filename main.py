from stats import count_words_in_file, count_characters_in_file, read_contents_from_path, generate_report
def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_contents_from_path(file_path)
    num_words = count_words_in_file(file_contents)
    characters_count = count_characters_in_file(file_contents)
    report = generate_report(file_path, num_words, characters_count)
    print(report)
    
main()