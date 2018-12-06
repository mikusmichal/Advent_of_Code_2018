if __name__ == "__main__":

    words = []
    answer = []

    def search():
        counter = 0
        with open('input.txt') as lines:
            for line in lines:
                words.append(line)

        for word1 in words:
            for word2 in words:
                for letter1, letter2 in zip(word1, word2):
                    if letter1 != letter2:
                        counter += 1

                if counter == 1:
                    answer.append(word1)
                    answer.append(word2)
                    print("The answer is:" + str(answer))
                    return cut()
                counter = 0


    def cut():
        word = answer[0]
        word2 = answer[1]
        cut_word = ''
        for letter1, letter2 in zip(word, word2):
            if letter1 == letter2:
                cut_word += letter1
        return cut_word

    print(search())
    


