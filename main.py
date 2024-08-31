def count_words(content):
    return len(content.split())

def new_characters_dict(content):
    words = content.split()

    characters = {}

    for word in words:
        for character in word: 
            ch = character.lower()
            if ch in characters:
                characters[ch] += 1
            else:
                characters[ch] = 1

    return characters

def characters_dict_to_list(characters_dict):
    sorted_list = []

    for ch in characters_dict:
        sorted_list.append({"name": ch, "count": characters_dict[ch]})

    def sort_on(d):
        return d['count']

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")

    content = read_book(book_path)
    characters_dict = new_characters_dict(content)
    characters_dict_list = characters_dict_to_list(characters_dict)

    print(f"{count_words(content)} words found in the document")

    print("\n")

    for character in characters_dict_list:
        if (not character["name"].isalpha()):
            continue
        print(f"the '{character['name']}' character was found {character['count']} times")

    print("--- End report ---")

def read_book(path):
    with open(path) as f:
        content = f.read()
        return content

def main():
    print_report("books/frankenstein.txt")

main()
