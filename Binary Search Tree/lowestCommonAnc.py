# 
# Time:
def lowestCommonAncestor(self, root, p, q):

    if p == q:
        return p
    if not root or not p or not q:
        return None
    
    min_val = min(p.val, q.val)
    max_val = max(p.val, q.val)

    current = root

    if current.val >= min_val and current.val <= max_val:
        return current
    elif current.val < min_val and current.val < max_val:
        current = current.right
    elif current.val > min_val and current.val > max_val:
        current = current.left

    return None

print(lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5])) 
        
        