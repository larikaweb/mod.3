def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        l_word = word.lower()
        if root_word in l_word or l_word in root_word:
            same_words.append(word)
    print(same_words)
    print("Проверочное слово:",root_word,". " "Однокоренные слова из списка:",*same_words)


single_root_words("Disablement","Able","Mable","Disable","Badel")