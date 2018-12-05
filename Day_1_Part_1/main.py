if __name__ == "__main__":
    freq = []
    with open('input.txt') as lines:
        for line in lines:
            freq.append(int(line.replace('\n', '')))
    print(sum(freq))