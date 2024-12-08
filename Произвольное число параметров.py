def single_root_words(root_words, *other_words):
    same_words = []

    for i in range(len(list(other_words))):
        if root_words.lower() in other_words[i].lower() or other_words[i].upper() in root_words.upper():
            same_words.append(other_words[i])
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
