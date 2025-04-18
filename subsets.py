def subsets(nums):
    """
    Generate all subsets of the given list using DFS.
    
    Args:
        nums: List of integers
    Returns:
        List of all possible subsets
    """
    result = []
    
    def dfs(i, curr):
        # Base case: if we've processed all numbers
        if i >= len(nums):
            result.append(curr[:])  # Make a copy of current subset
            return
            
        # Decision 1: Include nums[i]
        curr.append(nums[i])
        dfs(i + 1, curr)
        
        # Decision 2: Exclude nums[i] (backtrack)
        curr.pop()
        dfs(i + 1, curr)
    
    dfs(0, [])  # Start DFS from index 0 with empty subset
    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"All subsets of {nums}:")
    for subset in result:
        print(subset) 