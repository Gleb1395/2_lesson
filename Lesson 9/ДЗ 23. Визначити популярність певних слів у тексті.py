def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    dct = {}
    for item in words:
        for word in text.split():
            if item == word:
                if word in dct:
                    dct[word] += 1
                else:
                    dct[word] = 1
        if not item in dct:
            dct[item] = 0

    dct = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
    return dct
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
