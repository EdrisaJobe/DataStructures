def isFirstBadVersion(n):
    # Initialize two pointers for binary search
    # left starts at 0, right starts at n (the maximum version number)
    left, right = 0, n

    # Continue the search as long as left is less than right
    while left < right:
        # Calculate the middle version to check
        mid = (left + right) // 2

        # Check if the middle version is bad
        # Note: isBadVersion() is assumed to be a predefined API function
        if isBadVersion(mid):
            # If mid version is bad, the first bad version must be mid or earlier
            # So we narrow our search to the left half including mid
            right = mid
        else:
            # If mid version is good, the first bad version must be after mid
            # So we narrow our search to the right half excluding mid
            left = mid + 1
    
    # When left == right, we've found the first bad version
    # The 'or' operator here is redundant since left and right are equal
    return right or left
