import random
import datetime


def merge_sort(lst, start, end):
    if start >= end:
        return
    mid = int((end+start)/2)
    # print(f'start:{start}')
    # print(f'end:{end}')
    merge_sort(lst, start, mid)
    merge_sort(lst, mid+1, end)
    merge_sort_do(lst, start, mid, mid+1, end)


def merge_sort_do(lst, start1, end1, start2, end2):
    reg = []
    k = start1
    while start1 <= end1 and start2 <= end2:
        if lst[start1] < lst[start2]:
            reg.append(lst[start1])
            start1 += 1
        else:
            reg.append(lst[start2])
            start2 += 1
    while start1 <= end1:
        reg.append(lst[start1])
        start1 += 1
    while start2 <= end2:
        reg.append(lst[start2])
        start2 += 1
    for i in range(len(reg)):
        lst[k+i] = reg[i]


if __name__ == '__main__':
    start = datetime.datetime.now()
    a = []
    for i in range(9):
        a.append(int(random.random()*10))
    print(a)
    merge_sort(a, 0, len(a)-1)
    print(a)
    end = datetime.datetime.now()
    print(f'program runs for {(end-start).seconds} seconds')
