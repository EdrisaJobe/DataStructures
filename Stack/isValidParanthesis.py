# check to see if '{} () []' in a hashmap and have open/close pairings
def isValid(s):

    # store the given values
    hm = {'{':'}',
          '(':')',
          '[':']'
    }

    # empty stack (LIFO)
    stack = []

    # iterate thru the string
    for i in s:

        # if we find open paranthesis we add it to stack
        if i in '({[':
            stack.append(i)
        
        # if either the stack is empty or we couldn't append, return False
        elif len(stack)==0 or i != hm[stack.pop()]:
            return False
    
    # return True if we found a closing paranthesis after loop
    return len(stack)==0

print(isValid('{[]}'))