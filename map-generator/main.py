import random

class Map:
    #
    def __init__(self):
        #
        self.x = 15
        self.y = 15
    def generate(self):
        #
        map = [[0 for x in range(0, self.x)] for x in range(0, self.y)]

        swaprow = random.randint(0, self.x-1)
        swapcolumn = random.randint(0, self.y-1)

        print('\n', swaprow, swapcolumn, '\n')
        for row in range(0, self.y):
            if swaprow != row:
                for point in range(0, self.x):
                    if swapcolumn != point:
                        print(map[row][point], end='  ')
                    else:
                        map[row][point] += 1
                        print(map[row][point], end='  ')
            else:
                for point in range(0, self.x):
                    map[row][point] += 1
                    if swapcolumn != point:
                        print(map[row][point], end='  ')
                    else:
                        map[row][point] += 1
                        print(map[row][point], end='  ')
            print()


a = Map()
a.generate()