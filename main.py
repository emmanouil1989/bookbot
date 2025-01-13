def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_contents_from_path(file_path)
    num_words = count_words_in_file(file_contents)
    characters_count = count_characters_in_file(file_contents)
    report = generate_report(file_path, num_words, characters_count)
    print(report)
    

def read_contents_from_path(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words_in_file(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters_in_file(file_contents):
    count_dictionary = {}
    input = ''.join(filter(str.isalnum, file_contents))
    for char in input:
        lower_char = char.lower()
        if lower_char in count_dictionary:
            count_dictionary[lower_char] += 1
        else:
            count_dictionary[lower_char] = 1
    return count_dictionary

def sort_on(dict):
    return dict["num"]

def generate_report(path, total_worlds, chars_dictionary):
        beggining_of_report = f"---Begin report of {path}---"
        end_of_report = f"--- End report ---"
        total_worlds= f"{total_worlds} words found in the document\n"
        list_of_dictionaries = []
        count_array = []
        for char, count in chars_dictionary.items():
            list_of_dictionaries.append({"char": char, "num": count})
        sorted_list = sorted(list_of_dictionaries, key=sort_on, reverse=True)
        for word_dictionary in sorted_list:
            char = word_dictionary["char"]
            count = word_dictionary["num"]
            count_array.append(f"The character {char} was found {count} times")
        count_string = "\n".join(count_array)
        report = f"{beggining_of_report}\n{total_worlds}\n{count_string}\n{end_of_report}"
        return report             

main()