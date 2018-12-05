if __name__ == "__main__":

    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    def loop():
        two_letter = 0
        three_letter = 0

        with open('input.txt') as lines:
            for line in lines:
                for letter_test2 in alphabet:
                    if line.count(letter_test2) == 2:
                        two_letter += 1
                        break

        with open('input.txt') as lines:
            for line in lines:
                for letter_test3 in alphabet:
                    if line.count(letter_test3) == 3:
                        three_letter += 1
                        break
        print(two_letter * three_letter)

loop()


