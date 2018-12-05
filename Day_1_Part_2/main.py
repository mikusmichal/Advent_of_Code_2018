if __name__ == "__main__":

    list_freq = [0]

    def loop(new_freq):
        while True:
            with open('D:/škola/AoC/D1C1/input.txt') as lines:
                for line in lines:
                    change = int(line.replace('\n', ''))
                    curr_freq = new_freq
                    new_freq += change
                    print("Current frequency " + str(curr_freq) + ", change of " + str(change) + " resulting frequency  " + str(new_freq))
                    if new_freq in list_freq:
                        return new_freq
                    list_freq.append(new_freq)

    print(str(loop(0)))