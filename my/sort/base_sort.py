
def bubble_sort(array):
    length = len(array)
    isEnd  = None
    tmp    = None
    for i in range(length):
        # 每一轮都去判断
        isEnd = True
        for j in range(length - i - 1):
            # 只要不相等交换，相等值得先后顺序是不变的
            if array[j] > array[j + 1]:
                tmp          = array[j + 1]
                array[j + 1] = array[j]
                array[j]     = tmp
                isEnd        = False
        if isEnd:
            return


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)