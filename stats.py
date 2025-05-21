def count_words(text):
        words = text.split()
        return len(words)

def count_char(text):
        characters = {}
        text = text.lower()
        for char in text:
                if char in characters:
                     characters[char] += 1
                else:
                       characters[char] = 1
        return characters

def sort_on(d):
       return d["num"]

def sorted_dict(dict):
        char_list = [{"char": char, "num": count} for char, count in dict.items()]
        char_list.sort(reverse=True, key=sort_on)
        return char_list
