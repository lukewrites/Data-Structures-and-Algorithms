# encoding=utf8
"""
Week 1, Assignment 2 for coursera course "algorithmic toolbox."
"""

# this is the coursera boilerplace; take it out for now.
# n = int(input())
# li = [int(x) for x in input().split()]
# assert(len(li) == n)


def mpp(li):
    max1 = 0
    max2 = 0

    for i in range(0, len(li), 2):
        try:
            if li[i+1] > max1:
                max1 = li[i+1]
            elif li[i+1] > max2:
                max2 = li[i+1]
        except IndexError:
            pass
        if li[i] > max1:
            max2, max1 = max1, li[i]
        elif li[i] > max2:
            max2 = li[i]
        else:
            pass

    return max1 * max2

mpp([1, 2, 3, 4, 5])
