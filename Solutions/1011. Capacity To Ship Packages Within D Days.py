from typing import List


def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    for single_row in box:
        dot = -1
        stone = -1
        for i in range(len(single_row) - 1, 0, -1):

            if single_row[i] == '.' and single_row[i - 1] == '#':

                if single_row[i] == '.':
                    dot = i

                if single_row[i] == '#':
                    stone = i

                if dot != -1 and stone != -1:
                    single_row[dot], single_row[stone] = single_row[stone], single_row[dot]
                    dot = stone
                    stone = -1


    for a in box:
        print(a)


rotateTheBox(box=[["#", "#", "#", ".", "#", "."]])

#
# A stone '#'
# A stationary obstacle '*'
# Empty '.'
