def max_diff(k, l=[]):
    # stores the max elements
    max_out = []

    # stores the minimum elements
    min_out = []

    # temporary lists
    maxi = l
    mini = l
    
    while k > 0:
        # get max
        maximum = max(maxi)
        max_out.append(maximum)
        maxi = maxi[maxi.index(maximum)+1:]

        # get min
        minimum = min(mini)
        min_out.append(minimum)
        mini = mini[mini.index(minimum)+1:]
        k -= 1

    if max_out and min_out:
        print(sum(max_out)-sum(min_out))
    else:
        print (-1)

# Input test cases
t = int(input())
while t > 0:
    # Input number of integers
    n = int(input())
    inp = []

    # Input integers
    while n > 0:
        inp.append(int(input()))
        n -= 1

    # Input length of subsequence
    k = int(input())
    max_diff(k, inp)
    t -= 1
