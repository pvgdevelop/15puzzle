import random

def generate():
    range_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    grid = []
    random.shuffle(range_of_num)
    for i in range(16):
        if i % 4 == 0:
            grid.append(range_of_num[i:i+4])
    return grid


if __name__ == '__main__':
    print generate()
    print generate()