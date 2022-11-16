def reverseArr(n):

    # start and end pointers
    start = 0
    end = len(n)-1

    # check to see if start index is less than end before we swap
    while start < end:

        # swapping the elements
        n[start], n[end] = n[end], n[start]

        # move as we swap checking start and end
        start = start + 1
        end = end - 1

    return n

print(reverseArr([1,2,3,4,5]))