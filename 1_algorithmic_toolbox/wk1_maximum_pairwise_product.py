"""Week 1, Assignment 2 for coursera course algorithmic toolbox."""


def mpp(li):
    max1 = 0
    max2 = 0

    for i in range(0, len(li), 2):
        try:
            if li[i+1] > max1:
                max2, max1 = max1, li[i+1]
            elif li[i+1] > max2:
                max2 = li[i+1]
        except IndexError:  # if the list doesn't go that far.
            pass
        if li[i] > max1:
            max2, max1 = max1, li[i]
        elif li[i] > max2:
            max2 = li[i]
        else:
            pass

    return max1 * max2

# Here's another solution:

# high = max(li)
# li.pop(li.index(max(li)))
# second_high = max(li)
# return high * second_high
#
# I think the above is more pythonic, but I imagine it breaks the spirit of an
# algorithms class in which you're supposed to do everything by hand.
#
# this is the coursera boilerplate.
# n = int(input())
# li = [int(x) for x in input().split()]
# assert(len(li) == n)
#
