import string

words_list = 'word, sdjjf, net, ska net net net'

def clean_text(words_list):
    result = []
    for word in words_list:
        new_word = ''
        has_punctuation_mark = False
        for ch in string.punctuation:
            if ch in word:
                pos = word.find(ch)
                if pos == len(word) - 1:
                    new_word = word[:pos]
            elif pos < len(word):
                new_word = word[:pos] + word[pos + 1:]
            has_punctuation_mark = True
        if not has_punctuation_mark:
            new_word = word
        result.append(new_word.lower())
    return result

def count_words(words_list):
    set_words = set(words_list)
    words_dict = {word : words_list.count(word) for word in set_words}
    return words_dict

def top_10(words_dict):
    print('The top-10 words: ')
    items = words_dict.items()
    items = sorted(items, key=lambda x : x[1], reverse= True)
    for word, counter in items[:10]:
        print(word, ': ', counter)
print(top_10(words_list    ))