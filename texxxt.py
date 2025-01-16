import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        punctuation = string.punctuation.replace('-', '')
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for char in punctuation:
                        line = line.replace(char, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        search_word = word.lower()
        results = {}
        for filename, words in self.all_words.items():
            try:
                index = words.index(search_word) + 1
                results[filename] = index
            except ValueError:
                # Слово не найдено в файле
                pass
        return results

    def count(self, word):
        search_word = word.lower()
        results = {}
        for filename, words in self.all_words.items():
            results[filename] = words.count(search_word)
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))