def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    
    def word_count(text):
        count = 0
        words = text.split()
        for word in words:
            count +=1
        return count

    def count_characters(text):
        characters = {}
        for char in text:
            lowered = char.lower()
            if lowered in characters:
                characters[lowered] +=1
            else:
                characters[lowered] = 1
        sorted_by_keys = dict(sorted(characters.items()))
        return sorted_by_keys

    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(file_contents), " words found in the document")
    character_count = count_characters(file_contents)
    #print(character_count)
    for item in character_count:
        print(f"The ' {item} ' character was found {character_count[item]} times")



main()