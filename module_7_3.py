class WordFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for f_name in self.file_names:
            with open(f_name, 'r', encoding='utf-8') as file:
                word = []
                for line in file:
                    line = line.lower()
                    punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for char in punct:
                        line = line.replace(char, '')
                    word.extend(line.split())
                all_words[f_name] = word
        return all_words

    def find(self, word):
        f_res = {}
        word = word.lower()
        f_words = self.get_all_words()
        for name, words in f_words.items():
            if word in words:
                f_res[name] = words.index(word)
        return f_res

    def count(self, word):
        c_res = {}
        word = word.lower()
        c_words = self.get_all_words()
        for file_name, words in c_words.items():
            c_res[file_name] = words.count(word)
            return c_res


finder1 = WordFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
