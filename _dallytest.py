def custom_sort(candidates):
    for right in range(len(candidates)):
        left = right - 1
        if left <= len(candidates) and candidates[left] > candidates[left + 1]:
            candidates[left], candidates[left + 1] = candidates[left + 1], candidates[left]
            left -= 1
    print(candidates) 