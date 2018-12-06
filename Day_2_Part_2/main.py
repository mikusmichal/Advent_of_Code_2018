from Levenshtein import *
if __name__ == "__main__":

    words = []
    answer = ["dude", "dwde"]

    def search():
        with open('input.txt') as lines:
            for line in lines:
                words.append(line)

        for word1 in words:
            for word2 in words:
                if Levenshtein.distance(word1, word2) == 1:
                    answer.append(word1)
                    answer.append(word2)
                    return

    def cut():
        word = answer[0]
        word2 = answer[1]
        cut_word = ''
        for letter1, letter2 in zip(word, word2):
            if letter1 == letter2:
                cut_word += letter1
        print(cut_word)

search()
cut()


