import numpy as np
import re

if __name__ == "__main__":

    count_height = 0
    count_width = 0

    with open('input.txt') as lines:
        for line in lines:
            e = re.split('@ |,|: |x|\*', line.replace('\n', ''))
            e[0] = '0'
            e = list(map(int, e))
            if (e[1]+e[3]) > count_width:
                count_width = (e[1]+e[3])
            if (e[2]+e[4]) > count_height:
                count_height = (e[2]+e[4])
        arr = np.zeros((count_width, count_height))
        ans = np.zeros((count_width, count_height))

    answer = 0
    e = []
    x = False

    with open('input.txt') as lines:
        for line in lines:
            e = re.split('@ |,|: |x|\*', line.replace('\n', ''))
            e[0] = '0'
            e = list(map(int, e))
            arr[e[1]:(e[1] + e[3]), e[2]:(e[2] + e[4])] = 1
            ans += arr
            for number1, number2 in zip(np.nditer(ans[e[1]:(e[1] + e[3]), e[2]:(e[2] + e[4])]), (np.nditer(arr[e[1]:(e[1] + e[3]), e[2]:(e[2] + e[4])]))):
                if (number1 == 1) & (number2 == 1):
                    x = True
            if x:
                print(line)
            x = False
            arr = np.zeros((count_width, count_height))



