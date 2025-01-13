def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_contents_from_path(file_path)
    print(file_contents)

def read_contents_from_path(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()