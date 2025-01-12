def count_words(book):
    words = book.split()
    return len(words)

def unique_characters(book):
    number_uniques = {}
    for character in book:
        lowered = character.lower()
        if lowered not in number_uniques:
            number_uniques[lowered] = 1
        else:
            number_uniques[lowered] += 1 
    return number_uniques


def main():
    source = "books/frankenstein.txt"
    with open(source) as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(unique_characters(file_contents))
        print(f"--- Begin report of {source} ---")
        print(f"{count_words(file_contents)} words found in the document")
        characters = unique_characters(file_contents)
        for c in characters:
            print(f"The {c} character was found {characters[c]} times")
        print("--- End report ---")


main()
